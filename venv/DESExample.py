# DES (Data Encryption Standard) is a Block Cipher

# Benefits-Drawbacks:
# - if one bit flips(error) really matters - this block is randomized

# triple DES is often used

from pyDes import *

def modify(cipher):
    mod = [0] * len(cipher)
    mod[10] = ord(' ') ^ ord('1')
    mod[11] = ord(' ') ^ ord('0')
    mod[12] = ord('1') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])


message = "Give Bob:    10$"
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
# k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)


# Alice sending the encrypted message
cipher = k.encrypt(message)
print("Length of plain text:", len(message))
print("Length of cipher text:", len(cipher))
print("Encrypted:", cipher)


# Eve Modification
cipher = modify(cipher)


# Bob decrypting the cipher text
message = k.decrypt(cipher)
print("Decrypted:", message)