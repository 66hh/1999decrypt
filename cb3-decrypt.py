import os

def xor(data):
    result = bytearray(data)
    key = result[0] ^ 0x55
    if not key == result[1] ^ 0x6e:
        print("解密错误!")
        return
    for i in range(0, len(result)):
        result[i] ^= key
    return bytes(result)

def decrypt(path):
    data = open(path,'rb').read()
    with open(path + "-dec", "wb") as f:
        f.write(xor(data))

for file in os.listdir("bundles"):
    print(file)
    decrypt("bundles\\" + file)