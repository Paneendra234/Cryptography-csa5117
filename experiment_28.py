def solve_modified_dh(a, A, B, q):
    inv_a = pow(a, -1, q)
    x_A = (A * inv_a) % q
    shared_key = (x_A * B) % q
    return x_A, shared_key

q, a = 10007, 456
x_A, x_B = 123, 789
A, B = (x_A * a) % q, (x_B * a) % q

recovered_x_A, shared_key = solve_modified_dh(a, A, B, q)
print(f" DH Vulnerability: Eve derived x_A={recovered_x_A}, Shared Key={shared_key}")
