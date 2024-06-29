import os
import multiprocessing

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

def decrypt(file):
    print(file)
    path = "bundles/" + file
    data = open(path,'rb').read()
    with open("bundles-decrypt/" + file, "wb") as f:
        f.write(xordata(xorhead(data)))

if __name__ == "__main__":
    if not os.path.isdir("bundles"):
        print("copy bundle folders here")
    if not os.path.isdir("bundles-decrypt"):
        os.mkdir("bundles-decrypt")

    os.system("mkdir -p bundles-decrypt")
    pool = multiprocessing.Pool()
    pool.map(decrypt, os.listdir("bundles"))
    pool.close()
    pool.join()