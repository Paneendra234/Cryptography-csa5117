
import random, math

def factor_n_with_d(n, e, d):
    """Factors n given (e, d)."""
    k = e * d - 1
    s = 0
    while k % 2 == 0:
        k //= 2
        s += 1
    
    while True:
        g = random.randint(2, n - 1)
        x = pow(g, k, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            y = pow(x, 2, n)
            if y == n - 1:
                break
            if y == 1:
                p = math.gcd(x - 1, n)
                return p, n // p
            x = y

n, e1, d1 = 3599, 31, 3031 
p, q = factor_n_with_d(n, e1, d1)
print(f" Security Vulnerability: Factored modulus using leaked key -> p={p}, q={q}")
