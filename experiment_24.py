import math

def solve_rsa_q24(e=31, n=3599):
    p, q = None, None
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            p, q = i, n // i
            break
            
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return p, q, phi, d

p, q, phi, d = solve_rsa_q24()
print(f" Result: p={p}, q={q}, phi(n)={phi}, Private Key d={d}")
