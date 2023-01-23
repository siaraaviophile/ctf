from pwn import *
import binascii


enc = binascii.unhexlify("202020202020120c531e2a531a2b05191b3d0b060c1b020a14")
plain = "ITCLUB"
key = xor(enc, plain)
key = key[0:6]
res = xor(enc, key)
print(res) 
