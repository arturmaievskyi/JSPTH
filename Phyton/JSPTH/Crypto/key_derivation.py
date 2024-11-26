from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

def derive_key(password: str, salt: bytes = None, iterations: int = 100000) -> bytes:
    """Derives a key using PBKDF2-HMAC."""
    if salt is None:
        salt = os.urandom(16)  # Generate a random salt if not provided
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=default_backend(),
    )
    return kdf.derive(password.encode()), salt
