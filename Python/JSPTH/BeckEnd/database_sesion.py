# database_session.py

import time
import json
import sqlite3
import secrets
from typing import Optional, Dict, Tuple


class DatabaseSessionStore:
    """A session store that persists sessions in a SQLite database."""

    def __init__(self, db_path: str = 'sessions.db', session_lifetime: int = 3600):
        """
        Initialize the session store.

        Args:
            db_path (str): Path to the SQLite database file.
            session_lifetime (int): Session expiration time in seconds.
        """
        self.db_path = db_path
        self.session_lifetime = session_lifetime
        self._initialize_database()

    def _initialize_database(self) -> None:
        """Set up the SQLite database with a sessions table."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS sessions (
                    session_id TEXT PRIMARY KEY,
                    data TEXT NOT NULL,
                    created_at INTEGER NOT NULL
                )
            ''')

    def _generate_session_id(self, length: int = 32) -> str:
        """
        Generate a secure random session ID.

        Args:
            length (int): Length of the session ID.

        Returns:
            str: A secure random session ID.
        """
        return secrets.token_urlsafe(length)

    def create_session(self) -> Tuple[str, Dict]:
        """
        Create and store a new session.

        Returns:
            tuple: The session ID and an empty session data dictionary.
        """
        session_id = self._generate_session_id()
        session_data = {"created_at": int(time.time()), "data": {}}
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO sessions (session_id, data, created_at) VALUES (?, ?, ?)",
                (session_id, json.dumps(session_data["data"]), session_data["created_at"])
            )
        return session_id, session_data

    def get_session(self, session_id: str) -> Optional[Dict]:
        """
        Retrieve session data by session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            Optional[Dict]: The session data, or None if not found or expired.
        """
        with sqlite3.connect(self.db_path) as conn:
            result = conn.execute(
                "SELECT data, created_at FROM sessions WHERE session_id = ?",
                (session_id,)
            ).fetchone()

        if not result:
            return None

        data, created_at = result
        current_time = int(time.time())

        if current_time > created_at + self.session_lifetime:
            self.delete_session(session_id)
            return None  # Session has expired

        return {"created_at": created_at, "data": json.loads(data)}

    def save_session(self, session_id: str, session_data: Dict) -> None:
        """
        Update an existing session with new data.

        Args:
            session_id (str): The session ID.
            session_data (Dict): The session data to save.
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "UPDATE sessions SET data = ?, created_at = ? WHERE session_id = ?",
                (json.dumps(session_data["data"]), session_data["created_at"], session_id)
            )

    def delete_session(self, session_id: str) -> None:
        """
        Delete a session by session ID.

        Args:
            session_id (str): The session ID to delete.
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "DELETE FROM sessions WHERE session_id = ?",
                (session_id,)
            )
