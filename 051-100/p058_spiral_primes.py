import time
from sympy import isprime
start = time.time()

num_of_primes = 3
side_lenght = 2
corner_num = 9

while num_of_primes / (2 * side_lenght + 1) > 0.10:
    side_lenght += 2
    for i in range(3):
        corner_num += side_lenght
        if isprime(corner_num):
            num_of_primes += 1
    corner_num += side_lenght

print((2*side_lenght+1))
print(num_of_primes)

print(f"Result: {side_lenght + 1}")
end = time.time()
print("Time: {0:.4f} ms".format((end - start)*1000))
