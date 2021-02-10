# Hash function -> Deterministic ONE WAY function
# - any size of input -> fixed size output
# - same input produces same output (deterministic)
# - output is dependent on ALL input bits
# - output is uniformly distributed
#
# Used in:
# - Digital Signatures
# - Shadow Files (passwords)
# - HMAC (like Digital signature but symmetric, it is about keeping a shared secret) (Hashed Message Authentication Code)
# - Make deterministic Identifiers

import hashlib

def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)

m = "This is the hash value message".encode()

sha256 = hashlib.sha256()
sha256.update(m)
h = sha256.digest()
print(h)

m = modify(m)
sha256.update(m)
h = sha256.digest()
print(h)