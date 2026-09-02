import math

def break_rsa_common_factor(n, e, ciphertext_with_common_factor):
    # Compute greatest common divisor
    p = math.gcd(ciphertext_with_common_factor, n)
    if 1 < p < n:
        q = n // p
        phi = (p - 1) * (q - 1)
        d = pow(e, -1, phi)
        return p, q, d
    return None

p_true, q_true, e = 61, 53, 17
n = p_true * q_true
M = 61 * 2 
C = pow(M, e, n)

found_p, found_q, d = break_rsa_common_factor(n, e, C)
print(f"Attack: Found p={found_p}, q={found_q}, Private Key d={d}")
