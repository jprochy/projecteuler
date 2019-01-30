import time
import operator
from functools import reduce
from itertools import combinations_with_replacement, permutations, combinations
from math import factorial
from collections import Counter

EXP_LIMIT = 7
NUMS = '0123456789'


def is_unhappy(num):
    while num > 1 and num != 89 and num != 4:
        num = sum([int(x) ** 2 for x in str(num)])
    return num > 1

start = time.time()

combos = []
for combo in combinations_with_replacement(NUMS, EXP_LIMIT):
    poss = ''.join(combo)
    if is_unhappy(int(poss)):
        combos.append(poss)

result = 0
for combo in combos:
    base = 1
    for i in range(len(NUMS)):
        base *= factorial(combo.count(str(i)))
    result += int(factorial(EXP_LIMIT)/base)


print(f"Result: {result}")
end = time.time()
print(f"{round((end - start)*1000)} ms")
