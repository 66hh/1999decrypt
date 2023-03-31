import os

def xorhead(data):
    result = bytearray(data)
    for i in range(0, 32):
        result[i] ^= (len(data) + i).to_bytes(4, 'big')[3]
    return bytes(result)

def xordata(data):
    result = bytearray(data)
    for i in range(0, len(data) - 32):
        result[i + 32] ^= (i + 32).to_bytes(4, 'big')[3]
        if i + 32 >= 4096:
            return bytes(result)
    return bytes(result)

def decrypt(path):
    data = open(path,'rb').read()
    with open(path + "-dec", "wb") as f:
        f.write(xordata(xorhead(data)))

for file in os.listdir("bundles"):
    print(file)
    decrypt("bundles\\" + file)
