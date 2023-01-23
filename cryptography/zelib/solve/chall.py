import zlib
import binascii

plain = "ITCLUB{1ts_n0t_crypt0_is_zlib_br0wwhh}"
data = plain.encode("ascii")
compress = zlib.compress(data)

res = binascii.hexlify(compress)
print(res)
