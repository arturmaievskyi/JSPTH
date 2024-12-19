const crypto = require('crypto');

class CryptoUtils {
  constructor() {
    // Default settings
    this.algorithm = 'aes-256-cbc'; // Symmetric encryption algorithm
    this.key = crypto.randomBytes(32); // Secret key (256-bit for AES-256)
    this.iv = crypto.randomBytes(16); // Initialization vector
  }

  // Generate a secure random key
  generateKey(length = 32) {
    return crypto.randomBytes(length).toString('hex');
  }

  // Hash a string using SHA-256
  hashStringSHA256(data) {
    return crypto.createHash('sha256').update(data).digest('hex');
  }

  // Hash a string using SHA-512
  hashStringSHA512(data) {
    return crypto.createHash('sha512').update(data).digest('hex');
  }

  // Encrypt a string
  encrypt(data) {
    const cipher = crypto.createCipheriv(this.algorithm, this.key, this.iv);
    const encrypted = Buffer.concat([cipher.update(data, 'utf8'), cipher.final()]);
    return {
      iv: this.iv.toString('hex'),
      encryptedData: encrypted.toString('hex'),
    };
  }

  // Decrypt an encrypted string
  decrypt(encryptedData, ivHex) {
    const decipher = crypto.createDecipheriv(this.algorithm, this.key, Buffer.from(ivHex, 'hex'));
    const decrypted = Buffer.concat([
      decipher.update(Buffer.from(encryptedData, 'hex')),
      decipher.final(),
    ]);
    return decrypted.toString('utf8');
  }

  // Generate a HMAC (Hash-Based Message Authentication Code)
  generateHMAC(data, secret) {
    return crypto.createHmac('sha256', secret).update(data).digest('hex');
  }
}
