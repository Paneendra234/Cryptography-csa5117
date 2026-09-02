def clean_text(text):
    return ''.join([c.lower() for c in text if c.isalpha()])

def matrix_mult_vector(matrix, vector):
    return [
        (matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % 26,
        (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % 26
    ]

def hill_encrypt(plaintext, key):
    cleaned = clean_text(plaintext)
    
    if len(cleaned) % 2 != 0:
        cleaned += 'x'
    
    ciphertext = []
    for i in range(0, len(cleaned), 2):
        p_vec = [ord(cleaned[i]) - ord('a'), ord(cleaned[i + 1]) - ord('a')]
        c_vec = matrix_mult_vector(key, p_vec)
        ciphertext.append(chr(c_vec[0] + ord('a')).upper())
        ciphertext.append(chr(c_vec[1] + ord('a')).upper())
        
    return ''.join(ciphertext)

def get_inverse_key(key):
    """Calculate the inverse matrix K^-1 mod 26."""
    det = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    det_mod = det % 26
    
    inv_det = pow(det_mod, -1, 26)
    
    adj = [
        [ key[1][1] % 26, (-key[0][1]) % 26],
        [(-key[1][0]) % 26,  key[0][0] % 26]
    ]
    
    inv_key = [
        [(inv_det * adj[i][j]) % 26 for j in range(2)]
        for i in range(2)
    ]
    return inv_key

def hill_decrypt(ciphertext, key):
    inv_key = get_inverse_key(key)
    cleaned = ciphertext.lower()
    
    plaintext = []
    for i in range(0, len(cleaned), 2):
        c_vec = [ord(cleaned[i]) - ord('a'), ord(cleaned[i + 1]) - ord('a')]
        p_vec = matrix_mult_vector(inv_key, c_vec)
        plaintext.append(chr(p_vec[0] + ord('a')))
        plaintext.append(chr(p_vec[1] + ord('a')))
        
    return ''.join(plaintext)

plaintext = "meet me at the usual place at ten rather than eight oclock"
key = [
    [9, 4],
    [5, 7]
]

ciphertext = hill_encrypt(plaintext, key)
decrypted = hill_decrypt(ciphertext, key)

print(f"Original Plaintext : {plaintext}")
print(f"Encrypted Ciphertext: {ciphertext}")
print(f"Decrypted Plaintext : {decrypted}")
