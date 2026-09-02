def pad_iso7816(data, block_size=8):
    padded = bytearray(data) + b"\x80"
    while len(padded) % block_size != 0:
        padded.append(0x00)
    return bytes(padded)

data = b"12345678"  
print(f" Always-Padded Output: {pad_iso7816(data).hex()}")
