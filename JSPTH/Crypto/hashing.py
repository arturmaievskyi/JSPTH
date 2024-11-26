import hashlib
import hmac

class Hash():
    def create_hash(data: str, algorithm: str = "sha256") -> str:
        """Creates a hash using the specified algorithm."""
        hash_func = getattr(hashlib, algorithm)
        return hash_func(data.encode()).hexdigest()

    def create_hmac(key: bytes, data: str, algorithm: str = "sha256") -> str:
        """Creates an HMAC using the specified algorithm."""
        hash_func = getattr(hashlib, algorithm)
        return hmac.new(key, data.encode(), hash_func).hexdigest()
