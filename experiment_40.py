import collections

ENGLISH_FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def solve_monoalphabetic_attack(ciphertext, top_n=10):
    letters_only = [c.upper() for c in ciphertext if c.isalpha()]
    counts = collections.Counter(letters_only)
    sorted_cipher_chars = [char for char, _ in counts.most_common()]
    
    mapping = {}
    for i, char in enumerate(sorted_cipher_chars):
        if i < len(ENGLISH_FREQ):
            mapping[char] = ENGLISH_FREQ[i]
            
    candidates = []
    base_mapping = mapping.copy()
    
    decrypted_base = "".join(base_mapping.get(c.upper(), c) if c.isalpha() else c for c in ciphertext)
    candidates.append(decrypted_base)
    
    return candidates[:top_n]

ciphertext = "VTAA HFTX! MABL BL T LXTKXM FXLLTZX."
results = solve_monoalphabetic_attack(ciphertext, top_n=10)
print(f" Frequency Attack Candidate 1: {results[0]}")
