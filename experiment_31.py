def generate_cmac_subkeys(L_bytes, block_size_bits=128):
    const = 0x87 if block_size_bits == 128 else 0x1B
    num_bytes = block_size_bits // 8
    
    def shift_left(b):
        overflow = (b[0] & 0x80) != 0
        shifted = bytearray(num_bytes)
        for i in range(num_bytes - 1):
            shifted[i] = ((b[i] << 1) & 0xFF) | ((b[i+1] & 0x80) >> 7)
        shifted[-1] = (b[-1] << 1) & 0xFF
        if overflow:
            shifted[-1] ^= const
        return bytes(shifted)
        
    K1 = shift_left(L_bytes)
    K2 = shift_left(K1)
    return K1, K2

L = b"\x00" * 16
k1, k2 = generate_cmac_subkeys(L, 128)
print(f" CMAC K1 (Hex): {k1.hex()}, K2 (Hex): {k2.hex()}")
