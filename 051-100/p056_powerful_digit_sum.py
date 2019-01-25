import time
start = time.time()


result = max(sum(map(int, str(a**b))) for a in
             range(90, 100) for b in range(90, 100))

print(f"Result: {result}")
end = time.time()
print("Time: {0:.2f} ms".format((end - start)*1000))
