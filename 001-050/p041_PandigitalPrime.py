# Cislo je delitelne 3, pokud je suma jeho cifer delitelna 3 =>
#   9:1+2+3+4+5+6+7+8+9 = 45
#   8:1+2+3+4+5+6+7+8 = 36
#   7:1+2+3+4+5+6+7 = 28
#   6:1+2+3+4+5+6 = 21
#   5:1+2+3+4+5 = 15
#   4:1+2+3+4 = 10
#   3:1+2+3 = 6
#   2:1+2 = 3
#   => resime pouze n = 7, 4

def isPandigital(num):
    for i in range(len(str(num))):
        if (int(str(num)[i]) > len(str(num))):
            return False
        if (int(str(num)[i]) == 0):
            return False
        for j in range(i+1,len(str(num))):
            if (int(str(num)[j]) > len(str(num))):
                return False
            if (int(str(num)[j]) == 0):
                return False
            if (str(num)[i] == str(num)[j]):
                return False
    return True
    
def isPrime(num):
    if num > 1:
        for i in range(2,int(num**(1/2.0))+1):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

boo = False
N = 8654321  
for i in range(1000000,N):
    num = N - i
    if isPandigital(num):
        if isPrime(num):
            print(num)
            boo = False
            break

if boo:
    N = 5321  
    for i in range(1000,N):
        num = N - i
        if isPandigital(num):
            if isPrime(num):
                print(num)
                break          