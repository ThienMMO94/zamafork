print("Hello FHE World! This is a basic script for Zama crypto project.")
from cryptography.fernet import Fernet

def basic_encrypt(message):
    key = Fernet.generate_key()
    f = Fernet(key)
    return f.encrypt(str(message).encode())
    def basic_decrypt(encrypted, key):
    f = Fernet(key)
    return f.decrypt(encrypted).decode()