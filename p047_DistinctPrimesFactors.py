def compress(data, selectors):
    return (d for d, s in zip(data, selectors) if s)

def listOfPrimesBelow(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

def hasNfactors(N, num, primes):
    boo = True
    facs = 0
    for prime in primes:
        if prime > num//2:
            break
        elif ((num % prime) == 0):
            facs+=1
    if (facs == N):
        return True
    else:
        return False
    
def main(start,end, N):
    cons = 0
    primes = listOfPrimesBelow(end//(5**N))
    for num in range(start,end):
        if hasNfactors(N, num, primes):
            cons+=1
        else:
            cons=0
        if (cons == N):
            return num - N + 1
    return False
    
print(main(2*3*5*7,1000000, 4))
        
