# Type of One Time Pad - not as Secure - not recommended anymore

# Differences-compromises:
# - No requirements on Key stream (not TRUE randomness - possible to regenerate)
# - Key stream can be reused

# Used in
# - A5/1(G2 encryption)  - 54 bits (early Mobile phones)
# - A5/2(export version) - 17 bits (early Mobile phones)
# - RC4(WEP, SSL)        - 40-2048 bits (early)

# Benefits-Drawbacks:
# - if one bit flips(error) doesn't really matter - but this is NOT AUTHENTICITY (ex. bank transactions)

# Challenges
# - Authenticity - MAC (Message Authentication Code) (Modification in following code)
# - Reuse the same key - if Eve has a message and its cipher, she may find the key and
# if Alice reuses the key Eve will be able to steal other messages (Reused key in following code)
# - Low Entropy (randomness) (Brute force in following code)

# An implementation of not TRUE randomness - possible to regenerate:
# A linear congruential generator (LCG) is an algorithm that yields a sequence
# of pseudo-randomized numbers calculated with a discontinuous piecewise linear equation
# Wiki: https://en.wikipedia.org/wiki/Linear_congruential_generator
# ANSI C implementation of LCG algorithm

# Pseudo randomness - Don't use that library in real life scenario!
import random

class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (134775813 * self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return (self.rand()//2**23) % 256


def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])


# Transmission with possible errors
def transmit(cipher, likely):
    b = []
    for c in cipher:
        if random.randrange(0, likely) == 0:
            c = c ^ 2 ** random.randrange(0, 8)
        b.append(c)
    return bytes(b)


# Modification - if Eve knows the message, she can change it
def modification(cipher):
    mod = [0] * len(cipher)
    mod[10] = ord(' ') ^ ord('1')
    mod[11] = ord(' ') ^ ord('0')
    mod[12] = ord('1') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])


# Reused Key
def get_key(message, cipher):
    return bytes([message[i] ^ cipher[i] for i in range(len(cipher))])

def crack(key_stream, cipher):
    length = min(len(key_stream), len(cipher))
    return bytes([key_stream[i] ^ cipher[i] for i in range(length)])


# Brute Force Attack
def brute_force(plain, cipher):
    for k in range(2**31):
        bf_key = KeyStream(k)
        for i in range(len(plain)):
            xor_value = plain[i] ^ cipher[i]
            if xor_value != bf_key.get_key_byte():
                break
        else:
            return k
    return False


# Encrypt
secret_key = 10
header = "MESSAGE: "
key = KeyStream(secret_key)
print("ENCRYPTION KEY:", key.get_key_byte())
message = header + "Send Bob:   10$"
message = message.encode()
cipher = encrypt(key, message)
print("CIPHER:", cipher)

# Transmission
# cipher = transmit(cipher, 5)

# Modification
# cipher = modification(cipher)

# Brute force Attack
# bf_key = brute_force(header.encode(), cipher)
# key = KeyStream(bf_key)
# message = encrypt(key, cipher)
# print("BRUTE FORCE ATTACK", message)

# Decrypt
dkey = KeyStream(secret_key)
print("DECRYPTION KEY:", dkey.get_key_byte())
message = encrypt(dkey, cipher)
print("MESSAGE:",message)