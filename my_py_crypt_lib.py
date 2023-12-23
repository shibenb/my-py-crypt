from cryptography.fernet import Fernet

def create_key(filename):
    key = Fernet.generate_key()
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key(filename):
    return open(filename, "rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("Invalid token")
        return
    with open(filename, "wb") as file:
        file.write(decrypted_data)
