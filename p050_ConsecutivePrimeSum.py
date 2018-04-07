# prime: 997651  sum of 543 primes

def compress(data, selectors):
    return (d for d, s in zip(data, selectors) if s)

def listOfPrimesBelow(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]
    
def listOfCumulativePrimes(primes):
    cum = []
    for i in range(1,len(primes)):
        sum = 0
        for j in range(0,i):
            sum+=primes[j]
        cum.append(sum)
    return cum
    
def main():
    primes = listOfPrimesBelow(100)
    cum = listOfCumulativePrimes(primes)
    
    for i in range(len(primes)):
        p = len(primes) - i
        for j in range():
    
    return cum
    
print(main())