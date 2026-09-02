import math

def check_affine_validity(a, b, m=26):
    is_valid = math.gcd(a, m) == 1
    mapping = {}
    collisions = False
    
    for p in range(m):
        c = (a * p + b) % m
        if c in mapping:
            collisions = True
        mapping[c] = p
        
    return is_valid, not collisions

print(f" Affine (a=2, b=3) Valid: {check_affine_validity(2, 3)}")
print(f" Affine (a=7, b=3) Valid: {check_affine_validity(7, 3)}")
