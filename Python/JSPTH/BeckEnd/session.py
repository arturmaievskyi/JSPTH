import uuid
import time
from .securecoockies import SecureCookieManager

class SessionManager:
    """Manages user sessions with secure cookie storage."""
    def __init__(self, secret_key=None, key_file='secret.key', session_lifetime=3600):
        """
        Initialize the SessionManager.

        Args:
            secret_key (bytes): A 32-byte key for encryption (optional).
            key_file (str): Path to the key file for persistent storage.
            session_lifetime (int): Lifetime of a session in seconds.
        """
        self.sessions = {}
        self.session_lifetime = session_lifetime
        self.cookie_name = "SESSION_ID"
        self.cookie_manager = SecureCookieManager(secret_key, key_file)

    def create_session(self):
        """Generate a new session ID and return session data."""
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = {"created_at": time.time(), "data": {}}
        return session_id, self.sessions[session_id]

    def get_session(self, encrypted_session_id):
        """Retrieve session data using an encrypted session ID."""
        try:
            session_id = self.cookie_manager.decrypt(encrypted_session_id)
            session = self.sessions.get(session_id)
            if not session:
                raise ValueError("Session not found.")
            if time.time() > session["created_at"] + self.session_lifetime:
                del self.sessions[session_id]  # Remove expired session
                raise ValueError("Session has expired.")
            return session_id, session
        except ValueError:
            return None, None

    def save_session(self, session_id, session_data):
        """Save updated session data."""
        self.sessions[session_id] = session_data
