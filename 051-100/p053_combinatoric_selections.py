from math import factorial
import time
start = time.time()

LIMIT = 1000000


def combinations(population, sample_set):
    return factorial(population) / (factorial(sample_set) *
                                    factorial(population - sample_set))


def more_than_million(base):
    return [combinations(base, subset) > LIMIT
            for subset in range(0, base)].count(True)


result = sum([more_than_million(num) for num in range(1, 101)])

print(f"Result: {result}")
end = time.time()
print("Time: {0:.2f} ms".format((end - start)*1000))
