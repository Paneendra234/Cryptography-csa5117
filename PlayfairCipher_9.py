def create_playfair_matrix(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    matrix_str = ""
    for char in keyword.upper():
        if char == 'J': char = 'I'
        if char not in matrix_str and char in alphabet:
            matrix_str += char
    for char in alphabet:
        if char not in matrix_str:
            matrix_str += char
    return [list(matrix_str[i:i+5]) for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == letter:
                return r, c

def playfair_decrypt(ciphertext, keyword):
    matrix = create_playfair_matrix(keyword)
    ciphertext = ciphertext.replace(" ", "")
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        r1, c1 = find_position(matrix, ciphertext[i])
        r2, c2 = find_position(matrix, ciphertext[i+1])
        
        if r1 == r2:
            plaintext += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            plaintext += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        else:
            plaintext += matrix[r1][c2] + matrix[r2][c1]
            
    return plaintext

cipher = "KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO BOTEI ZONTX BYBNT GONEY CUZWR GDSON SXBOU YWRHE BAAHY USEDQ"
cipher = cipher.replace('J', 'I') 
key = "ROYAL NEW ZEALAND NAVY"
print(playfair_decrypt(cipher, key))
