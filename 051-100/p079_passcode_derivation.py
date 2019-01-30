import time
import os
start = time.time()


def isfirst(keylog, num, known):
    for key in keylog:
        pos = key.find(num)
        if pos >= 1:
            for i in range(pos):
                if known.find(key[i]) == -1:
                    return False
    return True


keylog_file = f"{os.path.dirname(os.path.realpath(__file__))}/p079_keylog.txt"
with open(keylog_file, 'rt') as f:
    keylog = [line.rstrip('\n') for line in f.readlines()]

appearing = []
possible_key = ""

for key in keylog:
    for num in key:
        if num not in appearing:
            appearing.append(num)

while len(appearing) > 0:
    for key in appearing:
        if isfirst(keylog, key, possible_key):
            possible_key += key
            appearing.remove(key)
            break

print(f"Result: {''.join(possible_key)}")
end = time.time()
print(f"{round((end - start)*1000)} ms")
