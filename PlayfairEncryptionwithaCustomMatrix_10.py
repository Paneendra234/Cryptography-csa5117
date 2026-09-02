def get_position(matrix, char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c
    return None

def playfair_encrypt(plaintext):
    matrix = [
        ['M', 'F', 'H', 'I', 'K'],
        ['U', 'N', 'O', 'P', 'Q'],
        ['Z', 'V', 'W', 'X', 'Y'],
        ['E', 'L', 'A', 'R', 'G'],
        ['D', 'S', 'T', 'B', 'C']
    ]
    
    plaintext = plaintext.upper()
    cleaned_text = ""
    for char in plaintext:
        if char.isalpha():
            if char == 'J':
                cleaned_text += 'I'
            else:
                cleaned_text += char
                
    pairs = []
    i = 0
    while i < len(cleaned_text):
        char1 = cleaned_text[i]
        if i + 1 < len(cleaned_text):
            char2 = cleaned_text[i+1]
            if char1 == char2:
                pairs.append(char1 + 'X')
                i += 1
            else:
                pairs.append(char1 + char2)
                i += 2
        else:
            pairs.append(char1 + 'X') 
            i += 1
            
    ciphertext = ""
    for pair in pairs:
        r1, c1 = get_position(matrix, pair[0])
        r2, c2 = get_position(matrix, pair[1])
        
        if r1 == r2:
            ciphertext += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            ciphertext += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:
            ciphertext += matrix[r1][c2] + matrix[r2][c1]
            
    formatted_cipher = " ".join([ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)])
    
    return pairs, formatted_cipher

message = "Must see you over Cadogan West. Coming at once."
pairs, encrypted_message = playfair_encrypt(message)

print(f"Original Text: {message}")
print(f"Digraph Pairs: {' '.join(pairs)}")
print(f"Ciphertext   : {encrypted_message}")
