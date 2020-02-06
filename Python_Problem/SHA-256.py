import hashlib

data = input()
output = hashlib.sha256(data.encode())

print(output.hexdigest())
