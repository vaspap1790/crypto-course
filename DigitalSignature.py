import hashlib


def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)


# Taken by running RSA.py
# Public key (e,n): 5 167477
# Secret key d: 8333

n = 167477
e = 5
d = 8333

# This is the message Alice wants to send signed to Bob
message = "Bob you are awesome".encode()
# Step 1: Hash the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
# Real life no % n
h = int.from_bytes(h, "big") % n
print("Hash Value:", h)
# Step 2: Produce sign
sign = h**d % n
# Step 3: Send message with signature
print(message, sign)


# This is Eve modifying the message (Hash and Verification Code will not be the same for Bob)
# message = modify(message)
# print(message)


# Bob verifying the signature
# Step 1: Calculate the hash value of the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
# Real life no % n
h = int.from_bytes(h, "big") % n
print("Hash Value:", h)
# Step 2: Verify the signature (should be the same with the hash)
verification = sign**e % n
print("Verification code: ", verification)