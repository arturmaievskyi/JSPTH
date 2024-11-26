from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
import os


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
