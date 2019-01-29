import math
import time
start = time.time()


limit = 1000
numerator = 3
denominator = 2
counter = 0

for x in range(2, limit + 1):
    numerator, denominator = numerator + 2*denominator, numerator + denominator
    if int(math.log10(numerator)) > int(math.log10(denominator)):
        counter += 1


print(f"Result: {counter}")
end = time.time()
print("Time: {0:.4f} ms".format((end - start)*1000))
