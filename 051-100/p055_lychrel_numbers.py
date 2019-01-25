import time
start = time.time()


def is_lychrel(n):
    for i in range(50):
        number = n + int(str(n)[::-1])
        if str(number) == str(number)[::-1]:
            return False
        n = number
    return True

result = [is_lychrel(num) for num in range(10001)].count(True)

print(f"Result: {result}")
end = time.time()
print("Time: {0:.2f} ms".format((end - start)*1000))
