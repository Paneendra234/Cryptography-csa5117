P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8  = [6, 3, 7, 4, 8, 5, 10, 9]

IP  = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]

EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

def permute(bits, table):
    return ''.join(bits[i - 1] for i in table)


def left_shift(bits, n):
    return bits[n:] + bits[:n]


def xor_bits(a, b):
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

def generate_keys(key):
    key = permute(key, P10)

    left = key[:5]
    right = key[5:]

    left = left_shift(left, 1)
    right = left_shift(right, 1)
    K1 = permute(left + right, P8)

    left = left_shift(left, 2)
    right = left_shift(right, 2)
    K2 = permute(left + right, P8)

    return K1, K2

def sbox(bits, box):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)

    return format(box[row][col], '02b')

def fk(bits, key):
    left = bits[:4]
    right = bits[4:]

    expanded = permute(right, EP)

    temp = xor_bits(expanded, key)

    left_sbox = sbox(temp[:4], S0)
    right_sbox = sbox(temp[4:], S1)

    combined = left_sbox + right_sbox

    combined = permute(combined, P4)

    left = xor_bits(left, combined)

    return left + right

def sdes_encrypt(plaintext, key):
    K1, K2 = generate_keys(key)

    bits = permute(plaintext, IP)

    bits = fk(bits, K1)

    bits = bits[4:] + bits[:4]

    bits = fk(bits, K2)

    ciphertext = permute(bits, IP_INV)

    return ciphertext

def sdes_decrypt(ciphertext, key):
    K1, K2 = generate_keys(key)

    bits = permute(ciphertext, IP)

    bits = fk(bits, K2)

    bits = bits[4:] + bits[:4]

    bits = fk(bits, K1)

    plaintext = permute(bits, IP_INV)

    return plaintext


def cbc_encrypt(plaintext, key, iv):
    ciphertext = ""
    previous = iv

    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i + 8]

        xored = xor_bits(block, previous)

        encrypted = sdes_encrypt(xored, key)

        ciphertext += encrypted

        previous = encrypted

    return ciphertext


def cbc_decrypt(ciphertext, key, iv):
    plaintext = ""
    previous = iv

    for i in range(0, len(ciphertext), 8):
        block = ciphertext[i:i + 8]

        decrypted = sdes_decrypt(block, key)

        original = xor_bits(decrypted, previous)

        plaintext += original

        previous = block

    return plaintext



print("===== S-DES CBC MODE =====")

key = "0111111101"
iv = "10101010"
plaintext = "0000000100100011"

print("Key       :", key)
print("IV        :", iv)
print("Plaintext :", plaintext)

ciphertext = cbc_encrypt(plaintext, key, iv)

print("Ciphertext:", ciphertext)

decrypted = cbc_decrypt(ciphertext, key, iv)

print("Decrypted :", decrypted)

if decrypted == plaintext:
    print("Decryption successful!")
else:
    print("Decryption failed!")
