import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

class EncryptionManager:
    def __init__(self):
        load_dotenv()
        key = os.getenv("ENCRYPTION_KEY")
        if not key:
            raise ValueError("ENCRYPTION_KEY not set in environment.")
        self.fernet = Fernet(key.encode())

    def encrypt(self, plaintext: str) -> bytes:
        return self.fernet.encrypt(plaintext.encode())

    def decrypt(self, ciphertext: bytes) -> str:
        return self.fernet.decrypt(ciphertext).decode()

def set_encryption_key():
    load_dotenv()
    if not os.getenv("ENCRYPTION_KEY"):
        key = Fernet.generate_key().decode()
        with open(".env", "a") as f:
            f.write(f"\nENCRYPTION_KEY={key}")
