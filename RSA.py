# Asymmetric encryption - used today for Key Distribution
# https://en.wikipedia.org/wiki/RSA_(cryptosystem)

import math
import random


def is_prime(p):
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0 :
            return False
    return True


def get_prime(size):
    while True:
        p = random.randrange(size, 2*size)
        if is_prime(p):
            return p


def lcm(a, b):
    return a*b//math.gcd(a,b)


def get_e(lamda_n):
    for e in range(2, lamda_n):
        if math.gcd(e, lamda_n) == 1:
            return e
    return False


def get_d(e, lamda_n):
    for d in range(2, lamda_n):
        if d*e % lamda_n == 1:
            return d
    return False

# Key generation done by Alice (secret):
# Step 1: Generate two distinct primes
size = 300
p = get_prime(size)
while True:
    temp = get_prime(size)
    if temp != p:
        q = temp
        break
print("Generated Primes:", p, q)

# Step 2: Compute n = p*q that will be used as a modulus
n = p*q
print("Modulus n:", n)

# Step 3: Compute λ(n) = lcm(λ(p),λ(q)) = lcm(p − 1, q − 1) , λ(p)= p-1
lambda_n = lcm(p-1, q-1)
print("lambda_n :", lambda_n)

# Step 4: Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime
e = get_e(lambda_n)
print("Public exponent e:", e)

# Step 5: Determine d as d = 1/e (mod λ(n)); that is, d is the modular multiplicative inverse of e modulo λ(n)
d = get_d(e, lambda_n)
print("Secret exponent d:", d)

# Done with key generation
print("Public key (e,n):", e, n)
print("Secret key d:", d)

# This is Bob anting to send a message
m = 117
c = m**e % n
print("Bob sends: ", c)

# This is Alice decrypting the cipher
m = c**d % n
print("Alice message: ", m)