from collections import Counter

ENGLISH_FREQS = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702,
    'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153,
    'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
    'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974,
    'z': 0.00074
}

def decrypt_additive(ciphertext: str, key: int) -> str:
    """Decrypts additive/Caesar ciphertext given a shift key."""
    plaintext = []
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - key) % 26 + base)
            plaintext.append(decrypted_char)
        else:
            plaintext.append(char)
    return "".join(plaintext)

def calculate_chi_squared(text: str) -> float:
    """Calculates the Chi-Squared statistic against standard English letter frequencies."""
    letters_only = [c.lower() for c in text if c.isalpha()]
    total_letters = len(letters_only)
    
    if total_letters == 0:
        return float('inf')
        
    counts = Counter(letters_only)
    chi_squared = 0.0
    
    for char, expected_freq in ENGLISH_FREQS.items():
        observed = counts[char]
        expected = total_letters * expected_freq
        chi_squared += ((observed - expected) ** 2) / expected
        
    return chi_squared

def frequency_attack(ciphertext: str, top_n: int = 10):
    """Attempts all 26 keys and outputs the top_n results with lowest Chi-Squared scores."""
    results = []
    
    for key in range(26):
        candidate_pt = decrypt_additive(ciphertext, key)
        score = calculate_chi_squared(candidate_pt)
        results.append((score, key, candidate_pt))
    
    # Sort candidates by Chi-Squared score (lowest score = best fit for English)
    results.sort(key=lambda x: x[0])
    
    print(f"\n{'Rank':<5} | {'Key':<4} | {'Score':<8} | {'Candidate Plaintext'}")
    print("-" * 75)
    
    for rank, (score, key, text) in enumerate(results[:top_n], start=1):
        preview = text[:55] + "..." if len(text) > 55 else text
        print(f"{rank:<5} | {key:<4} | {score:<8.2f} | {preview}")

if __name__ == "__main__":
    print("=== Automated Additive Cipher Frequency Attack ===")
    
    sample_cipher = "Khoor Zruog, wklv lv dq dxwrpdwhg ohwwhu iuhtxhqfb dwwdfn!"
    print(f"Sample Ciphertext: {sample_cipher}")
    
    user_input = input("\nEnter ciphertext (or press Enter to use sample above): ").strip()
    if not user_input:
        user_input = sample_cipher
        
    top_n_input = input("How many top candidates would you like to see? [Default 10]: ").strip()
    top_n = int(top_n_input) if top_n_input.isdigit() else 10
    
    frequency_attack(user_input, top_n)
