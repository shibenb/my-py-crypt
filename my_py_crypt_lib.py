from cryptography import fernet

def create_key(keyfile):
    key = fernet.Fernet.generate_key()
    with open(keyfile, 'wb') as file:
        file.write(key)

def load_key(keyfile):
    return open(keyfile, 'rb').read()

def encrypt(infile, key, outfile):
    f = fernet.Fernet(key)
    with open(infile, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(outfile, 'wb') as file:
        file.write(encrypted_data)

def decrypt(infile, key, outfile):
    f = fernet.Fernet(key)
    with open(infile, 'rb') as file:
        encrypted_data = file.read()
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except fernet.InvalidToken:
        import sys
        sys.stderr.write('Error: The key/password/salt is incorrect.\n')
        return
    with open(outfile, 'wb') as file:
        file.write(decrypted_data)

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import secrets
import base64

def create_salt(saltfile, salt_size = 16):
    salt = secrets.token_bytes(salt_size)
    with open(saltfile, 'wb') as file:
        file.write(salt)

def load_salt(saltfile):
    return open(saltfile, 'rb').read()

def generate_key(salt, password, length = 32, n = 16384, r = 8, p = 1):
    kdf = Scrypt(salt=salt, length=length, n=n, r=r, p=p)
    derived_key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(derived_key)
