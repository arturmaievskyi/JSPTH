from JSPTH.Crypto import CryptoUtils
import os



crypto = CryptoUtils()

# 1. Hashing
print(crypto.create_hash('Hello, World!', 'sha256'))  # SHA-256 hash

# 2. HMAC
print(crypto.create_hmac('Hello, World!', 'secret-key', 'sha256'))  # HMAC-SHA-256

# 3. AES Encryption
key = os.urandom(32)  # AES-256 key
iv = os.urandom(16)   # Initialization vector
encrypted = crypto.encrypt_aes('Secret Data', key, iv)
print("Encrypted AES:", encrypted)
decrypted = crypto.decrypt_aes(encrypted, key, iv)
print("Decrypted AES:", decrypted)

# 4. RSA Encryption and Decryption
private_key, public_key = crypto.generate_rsa_keys()
rsa_encrypted = crypto.rsa_encrypt(public_key, 'Message to encrypt')
print("Encrypted RSA:", rsa_encrypted)
rsa_decrypted = crypto.rsa_decrypt(private_key, rsa_encrypted)
print("Decrypted RSA:", rsa_decrypted)

# 5. RSA Digital Signatures
signature = crypto.sign_data(private_key, 'Message to sign')
print("Signature:", signature)
print("Signature valid:", crypto.verify_signature(public_key, signature, 'Message to sign'))

# 6. Key Derivation
salt = os.urandom(16)
derived_key = crypto.derive_key('password', salt)
print("Derived key:", derived_key)