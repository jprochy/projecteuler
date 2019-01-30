import time
start = time.time()

result = 0
for i in range(1, 100):
    for j in range(1, 100):
        if len(str(i**j)) == j:
            result += 1

print(f"Result: {result}")
end = time.time()
print("Time: {0:.4f} ms".format((end - start)*1000))
