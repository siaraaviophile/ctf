import zlib
import binascii

data = binascii.unhexlify(b'789cf30c71f60975aa362c298ecf3328894f2eaa2c283188cf2c8eafcac94c8a4f2a32282fcfc8a805000ced0e72')
res = zlib.decompress(data)

print(res)
