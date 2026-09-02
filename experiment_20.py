from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

BLOCK_SIZE = 16  
def split_blocks(data, block_size=16):
    return [data[i:i + block_size] for i in range(0, len(data), block_size)]

def encrypt_cbc(plaintext_blocks, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    data = b"".join(plaintext_blocks)
    return encryptor.update(data) + encryptor.finalize()

def decrypt_cbc(ciphertext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext) + decryptor.finalize()
    return split_blocks(decrypted, BLOCK_SIZE)

P = [
    b"AAAA_BLOCK_1_AAA",
    b"BBBB_BLOCK_2_BBB",
    b"CCCC_BLOCK_3_CCC",
    b"DDDD_BLOCK_4_DDD"
]

key = os.urandom(16)
iv = os.urandom(16)

ciphertext = encrypt_cbc(P, key, iv)
C = split_blocks(ciphertext, BLOCK_SIZE)


corrupted_C1 = bytearray(C[0])
corrupted_C1[0] ^= 0xFF 
C_corrupted_trans = [bytes(corrupted_C1), C[1], C[2], C[3]]

P_decrypted = decrypt_cbc(b"".join(C_corrupted_trans), key, iv)

print("--- DEMO 20.a: Transmission Bit Error in C1 ---")
for i in range(4):
    status = "OK" if P_decrypted[i] == P[i] else "CORRUPTED"
    print(f"P{i+1} Decrypted: {P_decrypted[i]} [{status}]")


P1_source_err = bytearray(P[0])
P1_source_err[0] ^= 0xFF
P_source_corrupted = [bytes(P1_source_err), P[1], P[2], P[3]]

ciphertext_source_err = encrypt_cbc(P_source_corrupted, key, iv)
C_source = split_blocks(ciphertext_source_err, BLOCK_SIZE)

print("\n--- DEMO 20.b: Source Bit Error in P1 ---")
print("Ciphertext propagation comparison:")
for i in range(4):
    diff = "CHANGED" if C_source[i] != C[i] else "UNCHANGED"
    print(f"Ciphertext Block C{i+1}: {diff}")

P_rec = decrypt_cbc(ciphertext_source_err, key, iv)
print("\nReceiver decryption result:")
for i in range(4):
    matches_original = "ORIGINAL" if P_rec[i] == P[i] else "DIFFERENT"
    print(f"Decrypted P{i+1}: {P_rec[i]} ({matches_original})")
