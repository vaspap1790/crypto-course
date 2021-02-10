import base64
import hashlib

# SALTED-SHA512-PBKDF2

iterations = 45454
# salt is used to avoid the same entropy for same passwords - has to be unique and usually uses timestamp
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
password = "password".encode()
value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
# the actual value that is being saved
entropy = base64.b64encode(value)
print(entropy)


# Brute force crack password attempt - slow - this is why we add many iterations so that time to crack becomes infinite
def guess_pasword(salt, iteration, entropy):
    # assuming ONLY TWO alphabetical characters
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c1 in alphabet:
        for c2 in alphabet:
            password = str.encode(c1+c2)
            value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
            if value == entropy:
                return password
    return "".encode()
