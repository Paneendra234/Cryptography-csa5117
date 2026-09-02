def simulate_cbc_mac_forgery(X, T):
    block2 = bytes([X[i] ^ T[i] for i in range(len(X))])
    forged_message = X + block2
    expected_mac = T
    return forged_message, expected_mac

X = b"12345678" 
T = b"MAC_TAG_"  
forged_msg, forged_tag = simulate_cbc_mac_forgery(X, T)
print(f" CBC MAC Forgery: Message={forged_msg}, Valid Tag={forged_tag}")
