import random

def otp_vigenere_encrypt(plaintext, key_stream):
    cipher = []
    for i, char in enumerate(plaintext.upper()):
        if char.isalpha():
            p_val = ord(char) - ord('A')
            c_val = (p_val + key_stream[i]) % 26
            cipher.append(chr(c_val + ord('A')))
        else:
            cipher.append(char)
    return "".join(cipher)

def otp_vigenere_decrypt(ciphertext, key_stream):
    plain = []
    for i, char in enumerate(ciphertext.upper()):
        if char.isalpha():
            c_val = ord(char) - ord('A')
            p_val = (c_val - key_stream[i]) % 26
            plain.append(chr(p_val + ord('A')))
        else:
            plain.append(char)
    return "".join(plain)

message = "HELLO OTP"
key_stream = [3, 19, 5, 12, 8, 21, 14, 2, 7]
cipher = otp_vigenere_encrypt(message, key_stream)
plain = otp_vigenere_decrypt(cipher, key_stream)

print(f" OTP Vigenere Cipher: {cipher}, Decrypted: {plain}")
