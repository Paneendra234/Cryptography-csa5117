SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def generate_des_subkeys(key_56_bit):
    """
    Demonstrates Q18 (28-bit split) and Q17 (Generating subkeys).
    key_56_bit should be a binary string of length 56.
    """
    C = key_56_bit[:28]
    D = key_56_bit[28:]
    
    subkeys = []
    
    for round_num in range(16):
        shifts = SHIFT_SCHEDULE[round_num]
        C = left_shift(C, shifts)
        D = left_shift(D, shifts)
        subkey = C[:24] + D[:24] 
        subkeys.append(subkey)
        
    return subkeys

dummy_key = "1" * 56
encryption_keys = generate_des_subkeys(dummy_key)

decryption_keys = encryption_keys[::-1]

print(f"Key 1 (Encrypt): {encryption_keys[0]}")
print(f"Key 1 (Decrypt): {decryption_keys[0]} (This is K16 from encryption)")
