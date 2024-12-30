import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import redis
import logging
from elasticsearch import Elasticsearch
import json
from geopy.geocoders import Nominatim
from geopy import geolocator

# Elasticsearch client
es_client = Elasticsearch([{"host": "localhost", "port": 9200}])

# Logging configuration
def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("session_audit.log"),
            logging.StreamHandler(),
        ],
    )
    return logging.getLogger(__name__)

logger = configure_logging()

class EmailNotifier:
    def __init__(self, smtp_server, smtp_port, email, password, max_retries=3, retry_backoff=2):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password
        self.max_retries = max_retries
        self.retry_backoff = retry_backoff

    def send_email(self, recipient, subject, body):
        attempt = 0
        while attempt < self.max_retries:
            try:
                message = MIMEMultipart()
                message["From"] = self.email
                message["To"] = recipient
                message["Subject"] = subject
                message.attach(MIMEText(body, "plain"))

                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    server.starttls()
                    server.login(self.email, self.password)
                    server.sendmail(self.email, recipient, message.as_string())

                logger.info(f"Email sent to {recipient} with subject '{subject}'")
                return True  # Success
            except Exception as e:
                attempt += 1
                delay = self.retry_backoff ** attempt
                logger.error(
                    f"Failed to send email (attempt {attempt}/{self.max_retries}). "
                    f"Retrying in {delay} seconds. Error: {e}"
                )
                time.sleep(delay)

        logger.critical(f"All retries failed for email to {recipient}.")
        return False  # Failed after retries

class EnhancedRedisSessionStore:
    def __init__(self, redis_host, redis_port, session_lifetime, email_notifier):
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        self.session_lifetime = session_lifetime
        self.email_notifier = email_notifier

    def _generate_session_id(self):
        return f"session-{int(time.time() * 1000)}"

    def _log_to_elasticsearch(self, action, session_id, metadata=None):
        log_entry = {
            "timestamp": int(time.time()),
            "action": action,
            "session_id": session_id,
            "metadata": metadata or {},
        }
        es_client.index(index="session_logs", document=log_entry)
        logger.info(f"Logged to Elasticsearch: {log_entry}")

    def create_session(self, data, metadata=None):
        session_id = self._generate_session_id()
        session_data = {
            "created_at": int(time.time()),
            "data": data,
        }
        self.redis.setex(session_id, self.session_lifetime, json.dumps(session_data))
        self._log_to_elasticsearch("create", session_id, metadata)
        return session_id

    def get_session(self, session_id):
        session_data = self.redis.get(session_id)
        if not session_data:
            self._log_to_elasticsearch("access_failed", session_id)
            self.email_notifier.send_email(
                "admin@example.com",
                "Unauthorized Access Attempt",
                f"Unauthorized access attempt detected for session ID: {session_id}",
            )
            return {}
        self._log_to_elasticsearch("access", session_id)
        return json.loads(session_data)

    def delete_session(self, session_id, metadata=None):
        result = self.redis.delete(session_id)
        if result:
            self._log_to_elasticsearch("delete", session_id, metadata)
        else:
            logger.warning(f"Attempted to delete non-existent session: {session_id}")

    def rotate_session(self, old_session_id, metadata=None):
        old_session_data = self.get_session(old_session_id)
        if not old_session_data:
            self._log_to_elasticsearch("rotation_failed", old_session_id, metadata)
            self.email_notifier.send_email(
                "admin@example.com",
                "Session Rotation Failed",
                f"Session rotation failed for session ID: {old_session_id}.",
            )
            return None

        new_session_id = self._generate_session_id()
        self.create_session(old_session_data["data"], metadata)
        self.delete_session(old_session_id, metadata)
        self._log_to_elasticsearch("rotate", new_session_id, metadata)
        return new_session_id

class EnhancedElasticsearchSessionStore:
    def __init__(self, session_lifetime=1800):
        self.session_lifetime = session_lifetime

    def _generate_session_id(self):
        return f"session-{int(time.time() * 1000)}"

    def _log_to_elasticsearch(self, action, session_id, session_data=None, metadata=None):
        """
        Store session logs directly in Elasticsearch.
        """
        log_entry = {
            "timestamp": int(time.time()),
            "action": action,
            "session_id": session_id,
            "session_data": session_data or {},
            "metadata": metadata or {},
        }
        es_client.index(index="session_logs", document=log_entry)
        logger.info(f"Logged to Elasticsearch: {log_entry}")

    def _get_geolocation(self, ip_address):
        """
        Fetch geolocation data for the given IP address.
        """
        try:
            location = geolocator.geocode(ip_address)
            if location:
                return {"latitude": location.latitude, "longitude": location.longitude}
            return None
        except Exception as e:
            logger.warning(f"Failed to fetch geolocation for IP {ip_address}: {e}")
            return None

    def create_session(self, data, metadata=None):
        session_id = self._generate_session_id()
        session_data = {
            "created_at": int(time.time()),
            "data": data,
        }

        # Enhance metadata with geolocation
        if metadata and "ip_address" in metadata:
            metadata["geolocation"] = self._get_geolocation(metadata["ip_address"])

        # Log session creation in Elasticsearch
        self._log_to_elasticsearch("create", session_id, session_data, metadata)
        return session_id

    def get_session(self, session_id):
        """
        Query Elasticsearch to retrieve session logs for access.
        """
        query = {
            "query": {
                "bool": {
                    "must": [
                        {"term": {"session_id": session_id}},
                        {"term": {"action": "create"}},
                    ]
                }
            }
        }
        response = es_client.search(index="session_logs", body=query)
        hits = response.get("hits", {}).get("hits", [])
        if not hits:
            logger.warning(f"Session not found: {session_id}")
            self._log_to_elasticsearch("access_failed", session_id)
            return None

        # Return the session data from Elasticsearch
        session_data = hits[0]["_source"]["session_data"]
        logger.info(f"Accessed session: {session_id}")
        self._log_to_elasticsearch("access", session_id)
        return session_data

    def delete_session(self, session_id, metadata=None):
        """
        Log session deletion in Elasticsearch.
        """
        self._log_to_elasticsearch("delete", session_id, metadata=metadata)
        logger.info(f"Deleted session: {session_id}")

