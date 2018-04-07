def isPandigital(num):
    if (len(str(num)) != 9):
        return False
    for i in range(len(str(num))):
        for j in range(i+1,len(str(num))):
            if ((str(num)[i] == str(num)[j]) or (int(str(num)[i]) == 0) or (int(str(num)[i]) == 0)):
                return False
    return True
    
N = 9999
for i in range(1,N):
    num = N - i
    sum = 0
    sumNew = 0
    j = 1
    while (len(str(sumNew)) < 10):        
        sum = sumNew
        sumNew = int(str(sum) + str(num*j))
        j = j + 1
    if isPandigital(sum):
        print(sum)
        break