import numpy as np

def hill_cipher_known_plaintext_attack(P_matrix, C_matrix, m=26):
    """
    Solves C = P * K (mod m) for Key Matrix K = P^(-1) * C (mod m)
    """
    det = int(np.round(np.linalg.det(P_matrix))) % m
    det_inv = pow(det, -1, m)
    
    # Matrix Adjugate for 2x2
    adj = np.array([[P_matrix[1, 1], -P_matrix[0, 1]], [-P_matrix[1, 0], P_matrix[0, 0]]]) % m
    P_inv = (det_inv * adj) % m
    
    K = np.dot(P_inv, C_matrix) % m
    return K.astype(int)

# Plaintext "HELP" -> [[7, 4], [11, 15]]
P = np.array([[7, 4], [11, 15]])
# True Key Matrix [[3, 3], [2, 5]]
K_true = np.array([[3, 3], [2, 5]])
C = np.dot(P, K_true) % 26

K_recovered = hill_cipher_known_plaintext_attack(P, C)
print(" Hill Cipher Recovered Key Matrix:\n", K_recovered)
