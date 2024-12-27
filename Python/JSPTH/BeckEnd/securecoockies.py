# secure_cookie.py

from cryptography.fernet import Fernet
from http.cookies import SimpleCookie
import base64
import json

class SecureCookieManager:
    """Handles encryption and decryption of cookies."""
    def __init__(self, secret_key=None):
        """
        Initialize the SecureCookieManager with a secret key.
        
        Args:
            secret_key (bytes): A 32-byte key for encryption. Generates a random one if None.
        """
        if secret_key is None:
            self.secret_key = Fernet.generate_key()
        else:
            if len(secret_key) != 32:
                raise ValueError("Secret key must be 32 bytes long.")
            self.secret_key = secret_key
        self.fernet = Fernet(self.secret_key)

    def encrypt(self, value):
        """Encrypts a string value."""
        if isinstance(value, dict):
            value = json.dumps(value)  # Serialize dictionaries to JSON
        return self.fernet.encrypt(value.encode('utf-8')).decode('utf-8')

    def decrypt(self, encrypted_value):
        """Decrypts an encrypted string value."""
        try:
            return self.fernet.decrypt(encrypted_value.encode('utf-8')).decode('utf-8')
        except Exception as e:
            raise ValueError("Failed to decrypt cookie value.") from e
