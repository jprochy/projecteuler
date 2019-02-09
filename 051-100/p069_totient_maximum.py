import time
import numpy
from sympy.ntheory.primetest import isprime
from sympy import primerange
start = time.time()

LIMIT = 1000000
PRIMES = list(primerange(1,1000))

i = 0
result = 1

while (result * PRIMES[i] < LIMIT):
    result *= PRIMES[i]
    i += 1

print("Result: {}".format(result))
end = time.time()
print("{} ms".format(round((end - start)*1000)))
