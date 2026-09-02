def clean_text(text):
    return "".join([c.lower() for c in text if c.isalpha()])

def char_to_num(c):
    return ord(c) - ord('a')

def num_to_char(n):
    return chr((n % 26) + ord('a'))

def encrypt_otp(plaintext, key_stream):
    p_clean = clean_text(plaintext)
    ciphertext = []
    
    for i in range(len(p_clean)):
        p_val = char_to_num(p_clean[i])
        k_val = key_stream[i]
        c_val = (p_val + k_val) % 26
        ciphertext.append(num_to_char(c_val).upper())
        
    return "".join(ciphertext)

def decrypt_otp(ciphertext, key_stream):
    c_clean = clean_text(ciphertext)
    plaintext = []
    
    for i in range(len(c_clean)):
        c_val = char_to_num(c_clean[i])
        k_val = key_stream[i]
        p_val = (c_val - k_val) % 26
        plaintext.append(num_to_char(p_val))
        
    return "".join(plaintext)

def find_key_for_target(ciphertext, target_plaintext):
    c_clean = clean_text(ciphertext)
    p_clean = clean_text(target_plaintext)
    key_stream = []
    
    for i in range(len(c_clean)):
        c_val = char_to_num(c_clean[i])
        p_val = char_to_num(p_clean[i])
        k_val = (c_val - p_val) % 26
        key_stream.append(k_val)
        
    return key_stream


pt1 = "send more money"
key1 = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

ciphertext = encrypt_otp(pt1, key1)

pt2 = "cash not needed"
key2 = find_key_for_target(ciphertext, pt2)
decrypted_pt2 = decrypt_otp(ciphertext, key2)

print("=== Part (a) ===")
print(f"Plaintext : {pt1}")
print(f"Key Stream: {key1}")
print(f"Ciphertext: {ciphertext}\n")

print("=== Part (b) ===")
print(f"Ciphertext      : {ciphertext}")
print(f"Target Plaintext: {pt2}")
print(f"New Key Stream  : {key2}")
print(f"Decryption Test : {decrypted_pt2}")
