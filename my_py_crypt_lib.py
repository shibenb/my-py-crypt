from cryptography.fernet import Fernet

def create_and_load_key(filename):
    key = Fernet.generate_key()
    with open(filename, "wb") as key_file:
        key_file.write(key)
    return key

def load_key(filename):
    return open(filename, "rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

from cryptography import fernet

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except fernet.InvalidToken:
        print("Invalid token")
        return
    with open(filename, "wb") as file:
        file.write(decrypted_data)

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import secrets
import base64

import os

def generate_key(password, salt_size = 16, length = 32, n = 16384, r = 8, p = 1):
    salt_size = 16
    salt = secrets.token_bytes(salt_size)
    if(os.path.exists("salt.salt")):
        salt = open("salt.salt", "rb").read()
    else:
        with open("salt.salt", "wb") as file:
            file.write(salt)

    kdf = Scrypt(salt=salt, length=length, n=n, r=r, p=p)
    derived_key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(derived_key)
