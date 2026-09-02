def solve_caesar_attack(ciphertext, top_n=10):
    scores = []
    english_freq_map = {'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0, 'N': 6.7, 'S': 6.3}
    
    for shift in range(26):
        decrypted = []
        score = 0
        for char in ciphertext.upper():
            if char.isalpha():
                dec_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                decrypted.append(dec_char)
                score += english_freq_map.get(dec_char, 0)
            else:
                decrypted.append(char)
        scores.append((score, shift, "".join(decrypted)))
        
    scores.sort(reverse=True, key=lambda x: x[0])
    return [text for _, shift, text in scores[:top_n]]

cipher = "WKH VHFUHW PHVVDJH"
top_plaintexts = solve_caesar_attack(cipher, top_n=10)
print(f" Additive Cipher Top Candidate: {top_plaintexts[0]}")
