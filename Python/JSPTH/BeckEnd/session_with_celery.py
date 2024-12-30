import redis
import json
import logging
from email_tasks import send_email_task
from elasticsearch import Elasticsearch
from geopy.geocoders import Nominatim
import time

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Elasticsearch client
es_client = Elasticsearch([{"host": "localhost", "port": 9200}])

# Geolocator for metadata
geolocator = Nominatim(user_agent="session_logger")

class EnhancedRedisSessionStore:
    def __init__(self, redis_host, redis_port, session_lifetime, email_config):
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        self.session_lifetime = session_lifetime
        self.email_config = email_config

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

    def _get_geolocation(self, ip_address):
        try:
            location = geolocator.geocode(ip_address)
            return {"latitude": location.latitude, "longitude": location.longitude}
        except Exception as e:
            logger.warning(f"Failed to get geolocation for IP {ip_address}: {e}")
            return None

    def create_session(self, data, metadata=None):
        session_id = self._generate_session_id()
        session_data = {
            "created_at": int(time.time()),
            "data": data,
        }
        self.redis.setex(session_id, self.session_lifetime, json.dumps(session_data))

        # Enhance metadata with geolocation
        if "ip_address" in metadata:
            metadata["geolocation"] = self._get_geolocation(metadata["ip_address"])

        self._log_to_elasticsearch("create", session_id, metadata)
        return session_id

    def get_session(self, session_id):
        session_data = self.redis.get(session_id)
        if not session_data:
            self._log_to_elasticsearch("access_failed", session_id)
            send_email_task.delay(
                smtp_server=self.email_config["smtp_server"],
                smtp_port=self.email_config["smtp_port"],
                email=self.email_config["email"],
                password=self.email_config["password"],
                recipient="admin@example.com",
                subject="Unauthorized Access Attempt",
                body=f"Unauthorized access attempt detected for session ID: {session_id}.",
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
            send_email_task.delay(
                smtp_server=self.email_config["smtp_server"],
                smtp_port=self.email_config["smtp_port"],
                email=self.email_config["email"],
                password=self.email_config["password"],
                recipient="admin@example.com",
                subject="Session Rotation Failed",
                body=f"Session rotation failed for session ID: {old_session_id}.",
            )
            return None

        new_session_id = self.create_session(old_session_data["data"], metadata)
        self.delete_session(old_session_id, metadata)
        self._log_to_elasticsearch("rotate", new_session_id, metadata)
        return new_session_id
