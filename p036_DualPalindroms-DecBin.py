def toBinary(decNum):
    return int(bin(decNum)[2:])

def testPalindrom(num):
    for i in range(0,len(str(num))//2+1):
        if (str(num)[i] != str(num)[len(str(num))-1-i]):
            return False
    return True

def reverse(num):
    new = ""
    for i in range(0,len(str(num))):
        new = new+str(num[len(str(num))-1-i])
    return new
    
def genPalindroms(n):
    mid=len(str(n))%2
    end=int(str(n)[:len(str(n))//2+1])
    out = []
    for k in range(1,10):
        out.append(int(k))
    for num in range(1,end+1):       
        out.append(int(str(num)+reverse(str(num))))
        if (len(str(num)+reverse(str(num))) < len(str(n))):
            for k in range(10):
                out.append(int(str(num)+str(k)+reverse(str(num))))
    return out
    
    
sum = 0
decPal = genPalindroms(1000000)
print(decPal)
for num in decPal:
    if (testPalindrom(toBinary(num)) and (num <= N)):
        sum = sum + num
print(sum)