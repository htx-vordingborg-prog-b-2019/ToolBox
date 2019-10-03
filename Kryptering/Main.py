import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt(filename, inputPassword):

    file = open(filename, "r")
    content = file.read()
    file.close()

    salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    password = inputPassword.encode()

    print(str(password))

    key = base64.urlsafe_b64encode(kdf.derive(password))

    print("Key: " + str(key))

    #message = content.encode()

    fernet = Fernet(key)

    encrypted = fernet.encrypt(b'Nej')

    file = open(filename, "w")
    file.write(str(encrypted) + '\n')
    file.close()

def decrypt(filename, inputPassword):

    salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    password = inputPassword.encode()

    key = base64.urlsafe_b64encode(kdf.derive(password))

    print("Key: " + str(key))

    fernet = Fernet(key)

    file = open(filename)
    content = file.read()
    file.close()

    content = content.replace("b'","")
    content = content.replace("'","")

    content = content.encode()

    print(content)

    decrypted = fernet.decrypt(content)

    print(decrypted)

encrypt("test.txt", "hej")
decrypt("test.txt", "hej")
