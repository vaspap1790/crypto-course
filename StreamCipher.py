# Type of One Time Pad - not as Secure - not recommended anymore
# Differences-compromises:
# - No requirements on Key stream (not TRUE randomness)
# - Key stream can be reused
# Used in
# - A5/1(G2 encryption)  - 54 bits (early Mobile phones)
# - A5/2(export version) - 17 bits (early Mobile phones)
# - RC4(WEP, SSL)        - 40-2048 bits (early)

# Pseudo randomness - Don't use that library in real life scenario!
import random