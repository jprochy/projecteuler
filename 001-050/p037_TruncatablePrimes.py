def isPrime(num):
    if num > 1:
        for i in range(2,int(num**(1/2.0))+1):
            if (num % i) == 0:
                return False
        return True
    else:
        return False


def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
        
def isTruncatablePrime(n):
    if not isPrime(n):
        return False
    for i in range(1,len(str(n))):
        if not isPrime(int(str(n)[:i])):
            return False
        if not isPrime(int(str(n)[-i:])):
            return False
    return True
    

baseSet = [1,2,5,3,7,9]
trunc = []
sum = 0
count = 0
rep = 1

while (count < 11):
    out = []
    rep = rep + 1
    for item in list(product(baseSet, repeat=rep)):
        out.append(int(''.join(str(x) for x in item)))
    for item in out:
        if isTruncatablePrime(item):
            trunc.append(item)
            sum = sum + item
            count = count + 1
            if (count == 11):
                break    
        if (count == 11):
            break           
    if (count == 11):
        break
print(trunc)

print(isPrime(9))