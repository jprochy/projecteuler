import time
from gmpy2 import mpz
start = time.time()

MOD = 10000000000
EXP_MAX = 7830456
EXP = 2
MULT = 28433

base = 2
for i in range(EXP_MAX):
    base = (base * EXP) % MOD

result = (base * MULT + 1) % MOD

print(f"Result: {result}")
end = time.time()
print(f"{round((end - start)*1000)} ms")
