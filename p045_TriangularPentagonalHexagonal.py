import math
def cTriangularNumber(num):
    return num*(num+1)/2

def isPentagonalNumber(num):
    n = 1.0/6.0 * (1.0 + math.sqrt(24.0*num +1.0))
    return n == int(n)
    
def isHexagonalNumber(num):
    n = 1/4.0 * (1.0 + math.sqrt(8.0*num +1.0))
    return n == int(n)

def findNext(n):
    n+=1
    boo = True
    while boo and (n < 100000000):
        num = int(cTriangularNumber(n))
        if (isPentagonalNumber(num) and isHexagonalNumber(num)):
            return num
        n+=1
    return 0

print(findNext(285))