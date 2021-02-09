# Pseudo randomness - Don't use that library in real life scenario!
import random


def generate_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cletters = list(letters)
    key = {}
    for c in letters:
        key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
    return key


def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


def get_decryption_key(key):
    dkey = {}
    for k in key:
        dkey[key[k]] = k
    return dkey


key = generate_key()
message = "YOU ARE AWESOME"

# Encrypt
cipher = encrypt(key, message)
print(cipher)

# Decrypt
dkey = get_decryption_key(key)
decrypted_message = encrypt(dkey, cipher)
print(message)

# Attack -> FrequenceAnalysis.py