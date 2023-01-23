from base64 import b64encode

flag = b"ITCLUB{cf3k_k4h_b4nh??}"
for i in range(20):
  flag = b64encode(flag)

print(flag)
