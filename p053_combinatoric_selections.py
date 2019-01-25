from math import factorial   # 4075
LIMIT = 1000000


def combinations(population, sample_set):
    return factorial(population) / (factorial(sample_set) *
                                    factorial(population - sample_set))


def more_than_million(base):
    return [combinations(base, subset) > LIMIT
            for subset in range(0, base)].count(True)


print(sum([more_than_million(num) for num in range(1, 101)]))
