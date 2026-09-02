import math

grid_size = 30

total_keys = math.factorial(grid_size)

log2_exponent = math.log2(total_keys)
approx_power_of_2 = round(log2_exponent)

print("Playfair Key Space Analysis:")
print(f"Total possible keys (25!): {total_keys:,}")
print(f"Exact base-2 representation: 2^{log2_exponent:.2f}")
print(f"Approximate power of 2:      2^{approx_power_of_2}")
