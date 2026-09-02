def generate_keyword_cipher(keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword = keyword.upper()
    
    cipher_seq = ""
    for char in keyword:
        if char not in cipher_seq and char in alphabet:
            cipher_seq += char
            
    for char in alphabet:
        if char not in cipher_seq:
            cipher_seq += char
            
    print(f"plain : {  ' '.join(list(alphabet))}")
    print(f"cipher: {  ' '.join(list(cipher_seq))}")

generate_keyword_cipher("CIPHER")
