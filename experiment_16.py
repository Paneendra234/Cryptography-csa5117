import re
from collections import Counter

ENGLISH_FREQS = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

DICTIONARY = {"THE", "BE", "TO", "OF", "AND", "A", "IN", "THAT", "HAVE", "I", "IT", "MESSAGE", "SECRET"}

def score_text(text):
    """Scores a text based on how many valid English words it contains."""
    words = re.findall(r'[A-Z]+', text.upper())
    return sum(1 for word in words if word in DICTIONARY)

def frequency_attack(ciphertext, top_n=10):
    filtered_cipher = [c for c in ciphertext.upper() if c.isalpha()]
    cipher_counts = Counter(filtered_cipher)
    
    sorted_cipher = [char for char, count in cipher_counts.most_common()]
    
    base_mapping = {}
    for i, char in enumerate(sorted_cipher):
        if i < len(ENGLISH_FREQS):
            base_mapping[char] = ENGLISH_FREQS[i]
  
    results = []
    
    pt_1 = "".join(base_mapping.get(c, c) for c in ciphertext.upper())
    results.append((score_text(pt_1), pt_1))
    
    if len(sorted_cipher) >= 2:
        map_2 = base_mapping.copy()
        map_2[sorted_cipher[0]], map_2[sorted_cipher[1]] = map_2[sorted_cipher[1]], map_2[sorted_cipher[0]]
        pt_2 = "".join(map_2.get(c, c) for c in ciphertext.upper())
        results.append((score_text(pt_2), pt_2))
        
    results.sort(reverse=True, key=lambda x: x[0])
    return [text for score, text in results[:top_n]]

sample = "WKH VHFUHW PHVVDJH" 
print("Top Guesses:")
for i, guess in enumerate(frequency_attack(sample, top_n=2), 1):
    print(f"{i}: {guess}")
