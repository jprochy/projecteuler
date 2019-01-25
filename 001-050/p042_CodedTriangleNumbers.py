import os
path = os.path.abspath(os.path.dirname(__file__))
with open (path+"\\p042_words.txt", "r") as myfile:
    data=myfile.readlines()    
words = data[0].replace('"','').split(",")

triN = []
count = 0
cnum = 1
i = 2
while (cnum < 26*(len(max(words, key=len)))):
    triN.append(cnum)
    cnum = int(1/2.0 * i * (i + 1))
    i+=1

for word in words:
    sum = 0
    for char in word:
        sum+=ord(char)-64
    if sum in triN:
        count+=1

print(count)