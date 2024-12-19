import hashlib
import hmac
import base64
import os
import requests
from hashlib import pbkdf2_hmac
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding, ec
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PrivateFormat,
    PublicFormat,
    NoEncryption,
    load_pem_private_key,
    load_pem_public_key,
)
from cryptography.hazmat.backends import default_backend


class CryptoUtils:
    def __init__(self):
        pass

    # ------------------------
    # AES Encryption / Decryption
    # ------------------------

    def encrypt_aes(self, plaintext: str, key: bytes) -> dict:
        """
        Encrypt data using AES with a randomly generated IV.
        :param plaintext: Plaintext string to encrypt.
        :param key: 16/24/32-byte key for AES.
        :return: Dictionary containing ciphertext and IV.
        """
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
        return {
            "ciphertext": base64.b64encode(ciphertext).decode(),
            "iv": base64.b64encode(iv).decode(),
        }

    def decrypt_aes(self, encrypted_data: dict, key: bytes) -> str:
        """
        Decrypt AES-encrypted data.
        :param encrypted_data: Dictionary containing ciphertext and IV.
        :param key: 16/24/32-byte key for AES.
        :return: Decrypted plaintext string.
        """
        iv = base64.b64decode(encrypted_data["iv"])
        ciphertext = base64.b64decode(encrypted_data["ciphertext"])
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()

    # ------------------------
    # Hashing and HMAC
    # ------------------------

    def create_hash(self, data: str, algorithm="SHA256") -> str:
        """
        Generate a hash of the given data.
        :param data: Input string to hash.
        :param algorithm: Hashing algorithm (default: SHA256).
        :return: Hexadecimal hash string.
        """
        if algorithm == "SHA256":
            return hashlib.sha256(data.encode()).hexdigest()
        elif algorithm == "SHA1":
            return hashlib.sha1(data.encode()).hexdigest()
        elif algorithm == "MD5":
            return hashlib.md5(data.encode()).hexdigest()
        else:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}")

    def create_hmac(self, key: str, data: str) -> str:
        """
        Generate an HMAC for the given data.
        :param key: Secret key for HMAC.
        :param data: Input data to sign.
        :return: Hexadecimal HMAC string.
        """
        return hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()

    # ------------------------
    # Key Derivation
    # ------------------------

    def derive_key(self, password: str, salt: bytes, iterations=100000, key_length=32) -> bytes:
        """
        Derive a cryptographic key from a password.
        :param password: Input password.
        :param salt: Random salt.
        :param iterations: Number of PBKDF2 iterations (default: 100,000).
        :param key_length: Desired key length (default: 32 bytes).
        :return: Derived key.
        """
        return pbkdf2_hmac("sha256", password.encode(), salt, iterations, key_length)

    # ------------------------
    # RSA Key Generation / Encryption / Decryption
    # ------------------------

    def generate_rsa_keys(self, key_size=2048) -> dict:
        """
        Generate an RSA key pair.
        :param key_size: Size of the RSA key in bits (default: 2048).
        :return: Dictionary containing 'private_key' and 'public_key'.
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend(),
        )
        public_key = private_key.public_key()
        return {
            "private_key": private_key.private_bytes(
                Encoding.PEM,
                PrivateFormat.PKCS8,
                NoEncryption(),
            ).decode(),
            "public_key": public_key.public_bytes(
                Encoding.PEM,
                PublicFormat.SubjectPublicKeyInfo,
            ).decode(),
        }

    def rsa_encrypt(self, public_key: str, plaintext: str) -> str:
        """
        Encrypt data using an RSA public key.
        :param public_key: PEM-encoded RSA public key.
        :param plaintext: Plaintext string to encrypt.
        :return: Base64-encoded ciphertext.
        """
        key = load_pem_public_key(public_key.encode(), backend=default_backend())
        ciphertext = key.encrypt(
            plaintext.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return base64.b64encode(ciphertext).decode()

    def rsa_decrypt(self, private_key: str, ciphertext: str) -> str:
        """
        Decrypt data using an RSA private key.
        :param private_key: PEM-encoded RSA private key.
        :param ciphertext: Base64-encoded ciphertext.
        :return: Decrypted plaintext string.
        """
        key = load_pem_private_key(private_key.encode(), password=None, backend=default_backend())
        plaintext = key.decrypt(
            base64.b64decode(ciphertext),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return plaintext.decode()

    # ------------------------
    # Digital Signatures (ECC or RSA)
    # ------------------------

    def ecc_sign(self, private_key: str, message: str) -> str:
        """
        Sign a message using an ECC private key.
        :param private_key: PEM-encoded ECC private key.
        :param message: Message to sign.
        :return: Base64-encoded signature.
        """
        key = load_pem_private_key(private_key.encode(), password=None, backend=default_backend())
        signature = key.sign(
            message.encode(),
            ec.ECDSA(hashes.SHA256()),
        )
        return base64.b64encode(signature).decode()

    def ecc_verify(self, public_key: str, message: str, signature: str) -> bool:
        """
        Verify a signature using an ECC public key.
        :param public_key: PEM-encoded ECC public key.
        :param message: Original message.
        :param signature: Base64-encoded signature to verify.
        :return: True if valid, False otherwise.
        """
        key = load_pem_public_key(public_key.encode(), backend=default_backend())
        signature = base64.b64decode(signature)
        try:
            key.verify(
                signature,
                message.encode(),
                ec.ECDSA(hashes.SHA256()),
            )
            return True
        except Exception:
            return False
