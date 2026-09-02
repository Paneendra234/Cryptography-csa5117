def dsa_leak_private_key(m1_hash, m2_hash, s1, s2, r, q):
    k = ((m1_hash - m2_hash) * pow(s1 - s2, -1, q)) % q
    x = ((s1 * k - m1_hash) * pow(r, -1, q)) % q
    return x

q = 101
r = 23
x_true = 42
k_secret = 15

m1, m2 = 50, 70
s1 = (pow(k_secret, -1, q) * (m1 + x_true * r)) % q
s2 = (pow(k_secret, -1, q) * (m2 + x_true * r)) % q

recovered_x = dsa_leak_private_key(m1, m2, s1, s2, r, q)
print(f" DSA Attack: Recovered Private Key x={recovered_x}")
