import time
import numpy
from sympy.ntheory.primetest import isprime
from sympy import primerange
start = time.time()


def pair(num1, num2):
    if isprime(int(f"{str(num1)}{str(num2)}")):
        if isprime(int(f"{str(num2)}{str(num1)}")):
            return True
    return False


def find(n):
    primes = list(primerange(1, n))
    lprimes = len(primes)
    for i in range(lprimes):
        for j in range(i + 1, lprimes):
            if pair(primes[i], primes[j]):
                for k in range(j+1, lprimes):
                    if pair(primes[i], primes[k]) and \
                       pair(primes[j], primes[k]):
                        for l in range(k+1, lprimes):
                            if pair(primes[i], primes[l]) and \
                               pair(primes[j], primes[l]) and \
                               pair(primes[k], primes[l]):
                                for m in range(l+1, lprimes):
                                    if pair(primes[i], primes[m]) and \
                                       pair(primes[j], primes[m]) and \
                                       pair(primes[k], primes[m]) and \
                                       pair(primes[l], primes[m]):
                                        return primes[i] + primes[j] + \
                                               primes[k] + primes[l] + \
                                               primes[m]
    return None

print(f"Result: {find(10000)}")
end = time.time()
print(f"{round((end - start)*1000)} ms")
