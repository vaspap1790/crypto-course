# One Time Pad is unbreakable(proven) - key space is infinite - it uses XOR
# Requirements:
# - Key stream should only used once
# - Key stream should only be known by sender and receiver
# - Key stream should be generated from true randomness
# - Key stream should be as large as the message

# Pseudo randomness - Don't use that library in real life scenario!
import random


def generate_key_stream(n):
    return bytes([random.randrange(0, 256) for i in range(n)])


def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])


# Encode Message
message = "YOU ARE AWESOME"
message = message.encode()
key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream, message)

print("KEY_STREAM: ", key_stream)
print("CIPHER: ", cipher)
print("MESSAGE: ", xor_bytes(key_stream, cipher))