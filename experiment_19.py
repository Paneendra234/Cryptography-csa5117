from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def encrypt_3des_cbc(plaintext_bytes, key, iv):
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext_bytes) + encryptor.finalize()

key = os.urandom(24) 
iv = os.urandom(8)
plaintext = b"This is exactly 16 bytes!!" 

ciphertext = encrypt_3des_cbc(plaintext, key, iv)
print(f"3DES-CBC Ciphertext (Hex): {ciphertext.hex()}")
