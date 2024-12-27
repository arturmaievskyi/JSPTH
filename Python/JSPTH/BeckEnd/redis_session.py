# redis_session.py

import time
import json
from secrets import token_urlsafe
from typing import Optional, Dict, tuple
import redis
import logging
logger = logging.getLogger(__name__)


class RedisSessionStore:
    """Session management using Redis."""

    def __init__(self, redis_host: str = 'localhost', redis_port: int = 6379, session_lifetime: int = 3600):
        """
        Initialize the Redis session store.

        Args:
            redis_host (str): Redis server hostname.
            redis_port (int): Redis server port.
            session_lifetime (int): Session expiration time in seconds.
        """
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        self.session_lifetime = session_lifetime

    def _generate_session_id(self, length: int = 32) -> str:
        """
        Generate a secure random session ID.

        Args:
            length (int): Length of the generated session ID.

        Returns:
            str: A secure session ID.
        """
        return token_urlsafe(length)

    def create_session(self) -> tuple[str, Dict]:
        """
        Create and store a new session.

        Returns:
            tuple: A tuple of session ID and initial session data.
        """
        session_id = self._generate_session_id()
        session_data = {"created_at": int(time.time()), "data": {}}

        # Store session in Redis
        self.redis.setex(session_id, self.session_lifetime, json.dumps(session_data))
        return session_id, session_data

    def get_session(self, session_id: str) -> Optional[Dict]:
        """
        Retrieve a session by its ID, checking expiration.

        Args:
            session_id (str): The session ID to retrieve.

        Returns:
            dict: The session data if valid, None otherwise.
        """
        session_data_json = self.redis.get(session_id)
        if not session_data_json:
            return None  # Session not found or expired

        session_data = json.loads(session_data_json)
        return session_data

    def save_session(self, session_id: str, session_data: Dict) -> None:
        """
        Save updated session data to Redis.

        Args:
            session_id (str): The session ID to update.
            session_data (dict): The new session data.
        """
        self.redis.setex(session_id, self.session_lifetime, json.dumps(session_data))

    def delete_session(self, session_id: str) -> None:
        """
        Delete a session by its ID.

        Args:
            session_id (str): The session ID to delete.
        """
        self.redis.delete(session_id)
    def rotate_session(self, old_session_id: str) -> str:
        old_session_data = self.get_session(old_session_id)
        if not old_session_data:
            logger.warning(f"Failed session rotation for invalid session: {old_session_id}")
            return None

        new_session_id = self._generate_session_id()
        self.create_session(old_session_data["data"])
        self.delete_session(old_session_id)
        logger.info(f"Rotated session: {old_session_id} -> {new_session_id}")
        return new_session_id
