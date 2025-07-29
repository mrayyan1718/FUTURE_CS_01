from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import os

def derive_key(password, salt=None):
    if not salt:
        salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=100_000)
    return key, salt

def encrypt_file(file_data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(file_data)
    return cipher.nonce + tag + ciphertext  # Store nonce & tag with encrypted data

def decrypt_file(blob, key):
    nonce = blob[:16]
    tag = blob[16:32]
    ciphertext = blob[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)
