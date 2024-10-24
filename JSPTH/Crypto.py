'''
The file written with ChatGPT help
'''


import hashlib
import hmac
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class CryptoUtils:
    def __init__(self):
        self.backend = default_backend()

    # Hashing Function
    def create_hash(self, data: str, algorithm: str = 'sha256') -> str:
        """Generates a hash of the input data using the specified algorithm."""
        hash_obj = hashlib.new(algorithm)
        hash_obj.update(data.encode())
        return hash_obj.hexdigest()

    # HMAC Function
    def create_hmac(self, data: str, key: str, algorithm: str = 'sha256') -> str:
        """Generates an HMAC using the specified key and algorithm."""
        hmac_obj = hmac.new(key.encode(), data.encode(), hashlib.new(algorithm).name)
        return hmac_obj.hexdigest()

    # AES Symmetric Encryption
    def encrypt_aes(self, data: str, key: bytes, iv: bytes) -> bytes:
        """Encrypts data using AES (256-bit key) in CBC mode."""
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        padded_data = data + (16 - len(data) % 16) * ' '  # Padding for AES block size
        return encryptor.update(padded_data.encode()) + encryptor.finalize()

    # AES Symmetric Decryption
    def decrypt_aes(self, encrypted_data: bytes, key: bytes, iv: bytes) -> str:
        """Decrypts AES-encrypted data."""
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
        return decrypted_data.decode().rstrip()  # Remove padding

    # RSA Key Generation
    def generate_rsa_keys(self):
        """Generates RSA public and private keys."""
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()
        return private_key, public_key

    # RSA Encryption
    def rsa_encrypt(self, public_key, data: str) -> bytes:
        """Encrypts data using RSA public key."""
        return public_key.encrypt(
            data.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    # RSA Decryption
    def rsa_decrypt(self, private_key, encrypted_data: bytes) -> str:
        """Decrypts data using RSA private key."""
        return private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()

    # Digital Signature (RSA Signing)
    def sign_data(self, private_key, data: str) -> bytes:
        """Signs data using an RSA private key."""
        return private_key.sign(
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

    # Digital Signature Verification
    def verify_signature(self, public_key, signature: bytes, data: str) -> bool:
        """Verifies a signature using an RSA public key."""
        try:
            public_key.verify(
                signature,
                data.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except:
            return False

    # Key Derivation (PBKDF2)
    def derive_key(self, password: str, salt: bytes, length: int = 32, iterations: int = 100000) -> bytes:
        """Derives a key using PBKDF2."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=length,
            salt=salt,
            iterations=iterations,
            backend=self.backend
        )
        return kdf.derive(password.encode())
