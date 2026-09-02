P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8  = [6, 3, 7, 4, 8, 5, 10, 9]

IP = [2, 6, 3, 1, 4, 8, 5, 7]
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

    sbox_result = (
        sbox(temp[:4], S0) +
        sbox(temp[4:], S1)
    )

    sbox_result = permute(sbox_result, P4)

    left = xor_bits(left, sbox_result)

    return left + right



def sdes_encrypt(plaintext, key):
    K1, K2 = generate_keys(key)

    bits = permute(plaintext, IP)

    bits = fk(bits, K1)

    bits = bits[4:] + bits[:4]

    bits = fk(bits, K2)

    return permute(bits, IP_INV)


def ctr_encrypt(plaintext, key, counter):
    result = ""

    counter_value = int(counter, 2)

    for i in range(0, len(plaintext), 8):

        block = plaintext[i:i + 8]

        current_counter = format(
            (counter_value + i // 8) % 256,
            '08b'
        )

        encrypted_counter = sdes_encrypt(
            current_counter,
            key
        )

        cipher_block = xor_bits(
            block,
            encrypted_counter
        )

        result += cipher_block

    return result


def ctr_decrypt(ciphertext, key, counter):
    return ctr_encrypt(ciphertext, key, counter)

print("===== S-DES COUNTER MODE =====")

key = "0111111101"
counter = "00000000"
plaintext = "000000010000001000000100"

print("Key       :", key)
print("Counter   :", counter)
print("Plaintext :", plaintext)

ciphertext = ctr_encrypt(
    plaintext,
    key,
    counter
)

print("Ciphertext:", ciphertext)

decrypted = ctr_decrypt(
    ciphertext,
    key,
    counter
)

print("Decrypted :", decrypted)

if decrypted == plaintext:
    print("Decryption successful!")
else:
    print("Decryption failed!")
