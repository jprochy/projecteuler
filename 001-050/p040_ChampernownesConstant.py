const = ""
i = 0
out = 1

while  (len(const) < 1000002):
    const=str(const)+str(i)
    i=i+1
    
for i in range(7):
    out = out * int(const[10**i])
    print(const[10**i])

print(out)