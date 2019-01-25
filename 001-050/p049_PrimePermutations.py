def compress(data, selectors):
    return (d for d, s in zip(data, selectors) if s)

def listOfPrimesBelow(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]
    
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
            
            
def main(n):
    tPrimes = listOfPrimesBelow(10**n)
    primes = []
    for prime in tPrimes:
        if (prime > 10**(n-1)):
            primes.append(prime)
    # start algorithm
    for i in range(len(primes)):
        perms = []
        tPerms = list(permutations(str(primes[i])))
        nPerms = sorted(list(set([ int("%s%s%s%s" % x) for x in tPerms ])))
        for it in nPerms:
            if ((len(str(it)) == 4) and it in primes):
                perms.append(it)
        for j in range(i+1,len(primes)):
            if primes[j] in perms:                
                ni = 2*primes[j] - primes[i]
                if ((ni in primes) and (ni in perms) and (primes[i] != 1487)):
                    return str(primes[i])+str(primes[j])+str(ni)
    return "No match"
    
print(main(4))