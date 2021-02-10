import hashlib

def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)

# Alice and Bob SHARE a secret key
secret_key = "secret key".encode()

# Alice wants to send message to Bob with MAC - for Bob to be sure that it is Alice
m = "Hey Bob. You are still awesome.".encode()
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()
print(m, hmac)


# Eve wants to modify - Bob will figure out because HMAC is different
m = modify(m)


# Bob receives and validates
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()
print(m, hmac)