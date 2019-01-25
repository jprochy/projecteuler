import time
start = time.time()


def same_upto_6x(number):
    for multiplier in range(2, 7):
        if sorted(set(str(number))) != sorted(set(str(multiplier * number))):
            return False
    return True

num = 1
while not same_upto_6x(num):
    num += 1

print(f"Result: {num}")
end = time.time()
print("Time: {0:.4f} ms".format(end - start))
