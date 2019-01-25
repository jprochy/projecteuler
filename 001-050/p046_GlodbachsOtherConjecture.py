def compress(data, selectors):
    return (d for d, s in zip(data, selectors) if s)

def listOfPrimesBelow(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

def conject(primes, c):
    for n in range(1, 100):
        for ii in primes:
            conject = ii + (2 * (n ** 2))
            if conject == c:
                return True
            else:
                continue
    return False

N = 100000
def main():
    x = list(listOfPrimesBelow(N))
    composites = []
    for y in range(1, N, 2):
        if y not in x:
            composites.append(y)
        else:
            continue
    for c in composites:
        if c > 33:
            x2 = conject(x, c)
            if x2 == False:
                return c
         
print(main())