import time
import os
from itertools import permutations
start = time.time()


def valid(char):
    char = ord(char)
    if 32 <= char <= 90:
        return True
    elif 97 <= char <= 122:
        return True
    return False

cipher_file = f"{os.path.dirname(os.path.realpath(__file__))}/p059_cipher.txt"
with open(cipher_file, 'rt') as f:
    cipher = [int(x) for x in f.read().strip().split(',')]

cl = len(cipher) // 3 + 1
ptexts = []

for ppassword in permutations('abcdefghijklmnoipqrstuvwxyz', 3):
    ptext = ''.join(chr(c ^ ord(p)) for c, p in zip(cipher, ppassword * cl))
    if sum(valid(c) for c in ptext) == len(ptext):
        ptexts.append(ptext)

for ptext in ptexts:
    print(ptext)
    print(f"Result: {sum(ord(c) for c in ptext)}")
end = time.time()
print("Time: {0:.4f} ms".format((end - start)*1000))
