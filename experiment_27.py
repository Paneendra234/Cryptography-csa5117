def generate_rsa_codebook(e, n):
    return {pow(m, e, n): chr(m + ord('A')) for m in range(26)}

def decrypt_codebook_attack(ciphertext_list, codebook):
    return "".join(codebook[c] for c in ciphertext_list)

n = 3233
e = 17
plaintext = "HELLO"
ciphertexts = [pow(ord(c) - ord('A'), e, n) for c in plaintext]

codebook = generate_rsa_codebook(e, n)
decrypted = decrypt_codebook_attack(ciphertexts, codebook)
print(f" Codebook Attack Recovered Plaintext: {decrypted}")
