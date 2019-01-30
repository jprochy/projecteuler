import time
start = time.time()


def match(n):
    print(n)
    pattern = '1_2_3_4_5_6_7_8_9'
    s = str(n)
    if len(s) != len(pattern):
        return False
    for i in range(len(pattern)//2):
        if s[i*2] != pattern[i*2]:
            return False
    return True

n = 138902663
while not match(n*n):
    n -= 2
result = n * 10

print(f"Result: {result}")
end = time.time()
print(f"{round((end - start)*1000)} ms")
