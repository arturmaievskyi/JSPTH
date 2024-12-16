from cryptography.hazmat.primitives import hashes
import hashlib
import hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7

class signature:
    def sign_data(private_key, data: str) -> bytes:
        """Signs data using the RSA private key."""
        return private_key.sign(
            data.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256(),
        )

    def verify_signature(public_key, data: str, signature: bytes) -> bool:
        """Verifies the signature of the given data."""
        try:
            public_key.verify(
                signature,
                data.encode(),
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256(),
            )
            return True
        except Exception:
            return False
        
class Hash():
    def create_hash(data: str, algorithm: str = "sha256") -> str:
        """Creates a hash using the specified algorithm."""
        hash_func = getattr(hashlib, algorithm)
        return hash_func(data.encode()).hexdigest()

    def create_hmac(key: bytes, data: str, algorithm: str = "sha256") -> str:
        """Creates an HMAC using the specified algorithm."""
        hash_func = getattr(hashlib, algorithm)
        return hmac.new(key, data.encode(), hash_func).hexdigest()

class Key():
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

class Rsa():
    def generate_rsa_keys(key_size: int = 2048):
        """Generates an RSA key pair."""
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
        public_key = private_key.public_key()
        return private_key, public_key

    def rsa_encrypt(public_key, plaintext: str) -> bytes:
        """Encrypts plaintext using an RSA public key."""
        return public_key.encrypt(
            plaintext.encode(),
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
        )

    def rsa_decrypt(private_key, ciphertext: bytes) -> str:
        """Decrypts ciphertext using an RSA private key."""
        return private_key.decrypt(
            ciphertext,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
        ).decode()

class Aes:
    def encrypt_aes(key: bytes, plaintext: str) -> bytes:
        """Encrypts plaintext using AES (CBC mode)."""
        iv = os.urandom(16)  # Generate a random initialization vector
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        # Pad plaintext to be block-aligned
        padder = PKCS7(128).padder()
        padded_data = padder.update(plaintext.encode()) + padder.finalize()

        return iv + encryptor.update(padded_data) + encryptor.finalize()

    def decrypt_aes(key: bytes, ciphertext: bytes) -> str:
        """Decrypts ciphertext using AES (CBC mode)."""
        iv = ciphertext[:16]  # Extract the initialization vector
        actual_ciphertext = ciphertext[16:]
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        # Remove padding
        unpadder = PKCS7(128).unpadder()
        padded_data = decryptor.update(actual_ciphertext) + decryptor.finalize()
        return unpadder.update(padded_data) + unpadder.finalize()

