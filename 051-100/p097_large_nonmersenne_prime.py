import time
start = time.time()

MOD = 10000000000
EXP_MAX = 7830456
BASE = 2
MULT = 28433

exp = 2
for i in range(EXP_MAX):
    exp = (BASE * exp) % MOD

result = (exp * MULT + 1) % MOD

print(f"Result: {result}")
end = time.time()
print(f"{round((end - start)*1000)} ms")
