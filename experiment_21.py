def pad_message(message_bytes, block_size=8):
    """
    Appends a '1' bit (0x80 in bytes) followed by '0' bits to fill the block.
    If the message is already a multiple, it adds a whole new block.
    """
    padded = bytearray(message_bytes)
    padded.append(0x80)
    
    while len(padded) % block_size != 0:
        padded.append(0x00)
        
    return bytes(padded)

def unpad_message(padded_bytes):
    """
    Removes zero bytes from the end until it hits 0x80, then removes the 0x80.
    """
    idx = padded_bytes.rfind(b'\x80')
    if idx == -1:
        raise ValueError("Invalid padding: No 0x80 found.")
    
    for byte in padded_bytes[idx+1:]:
        if byte != 0:
            raise ValueError("Invalid padding: Non-zero bytes found after padding indicator.")
            
    return padded_bytes[:idx]

block_size = 8
original_message = b"12345678" 

padded = pad_message(original_message, block_size)
print(f"Padded exactly aligned message (Hex): {padded.hex()}")

unpadded = unpad_message(padded)
print(f"Unpadded matches original: {unpadded == original_message}")
