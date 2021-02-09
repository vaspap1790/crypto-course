def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    counter = 0
    for c in letters:
        key[c] = letters[(counter + n) % len(letters)]
        counter += 1
    return key


def get_decryption_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey


def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

def attack(cipher):
    for i in range(26):
        dkey = generate_key(i)
        message = encrypt(dkey, cipher)
        print(message)


key = generate_key(3)
message = "YOU ARE AWESOME"

# Encrypt
cipher = encrypt(key, message)
print(cipher)

# Decrypt
dkey = get_decryption_key(key)
decrypted_message = encrypt(dkey, cipher)
print(message)

# Attack
attack(cipher)