import os
import multiprocessing

def xor(data):
    result = bytearray(data)
    key = result[0] ^ 0x55
    if not key == result[1] ^ 0x6e:
        print("解密错误!")
    for i in range(0, len(result)):
        result[i] ^= key
    return bytes(result)

def decrypt(file):
    print(file)
    path = "bundles/" + file
    data = open(path,'rb').read()
    with open("bundles-decrypt/" + file, "wb") as f:
        f.write(xor(data))

if __name__ == "__main__":
    if not os.path.isdir("bundles"):
        print("copy bundle folders here")
    if not os.path.isdir("bundles-decrypt"):
        os.mkdir("bundles-decrypt")
    pool = multiprocessing.Pool()
    pool.map(decrypt, os.listdir("bundles"))
    pool.close()
    pool.join()