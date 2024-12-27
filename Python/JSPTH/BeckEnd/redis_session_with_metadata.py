# redis_session_with_metadata.py

import json
import time
import redis
import logging
from elasticsearch import Elasticsearch

# Initialize Elasticsearch client
es_client = Elasticsearch([{"host": "localhost", "port": 9200}])

# Configure logging
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

class RedisSessionStore:
    def __init__(self, redis_host: str, redis_port: int, session_lifetime: int):
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        self.session_lifetime = session_lifetime

    def _generate_session_id(self) -> str:
        return f"session-{int(time.time() * 1000)}"

    def _log_to_elasticsearch(self, action: str, session_id: str, metadata: dict = None):
        """Log session activity to Elasticsearch."""
        log_entry = {
            "timestamp": int(time.time()),
            "action": action,
            "session_id": session_id,
            "metadata": metadata or {},
        }
        es_client.index(index="session_logs", document=log_entry)
        logger.info(f"Logged to Elasticsearch: {log_entry}")

    def create_session(self, data: dict, metadata: dict = None) -> str:
        session_id = self._generate_session_id()
        session_data = {
            "created_at": int(time.time()),
            "data": data,
        }
        self.redis.setex(session_id, self.session_lifetime, json.dumps(session_data))
        logger.info(f"Created new session: {session_id} with metadata: {metadata}")
        self._log_to_elasticsearch("create", session_id, metadata)
        return session_id

    def get_session(self, session_id: str) -> dict:
        session_data = self.redis.get(session_id)
        if not session_data:
            logger.warning(f"Session not found or expired: {session_id}")
            self._log_to_elasticsearch("access_failed", session_id)
            return {}
        logger.info(f"Accessed session: {session_id}")
        self._log_to_elasticsearch("access", session_id)
        return json.loads(session_data)

    def delete_session(self, session_id: str, metadata: dict = None):
        result = self.redis.delete(session_id)
        if result:
            logger.info(f"Deleted session: {session_id} with metadata: {metadata}")
            self._log_to_elasticsearch("delete", session_id, metadata)
        else:
            logger.warning(f"Attempted to delete non-existent session: {session_id}")

    def rotate_session(self, old_session_id: str, metadata: dict = None) -> str:
        old_session_data = self.get_session(old_session_id)
        if not old_session_data:
            logger.warning(f"Failed session rotation for invalid session: {old_session_id}")
            self._log_to_elasticsearch("rotation_failed", old_session_id, metadata)
            return None

        new_session_id = self._generate_session_id()
        self.create_session(old_session_data["data"], metadata)
        self.delete_session(old_session_id, metadata)
        logger.info(f"Rotated session: {old_session_id} -> {new_session_id} with metadata: {metadata}")
        self._log_to_elasticsearch("rotate", new_session_id, metadata)
        return new_session_id
