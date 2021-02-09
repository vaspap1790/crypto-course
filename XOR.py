# XOR(^) (excluding OR)
# 0 ^ 0 = 0
# 1 ^ 0 = 1
# 0 ^ 1 = 1
# 1 ^ 1 = 0
# message ^ random  = cipher
# cipher  ^ random  = message

def xor(x,s):
    print(bin(x), 'xor', bin(s), '=', bin(x^s))

xor(4,8)
xor(4,4)
xor(255,1)
xor(255,128)