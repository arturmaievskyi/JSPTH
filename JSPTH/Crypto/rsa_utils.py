from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


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
