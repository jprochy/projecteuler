out = []

for p in range(1,1001):
    sum = 0
    for a in range(1,int(p*0.6)):
        for b in range(a,int(p*0.6)):
            c = (a*a + b*b)**(1/2.0)
            if ((c == int(c)) and (a+b+c == p)):
                sum = sum + 1
    out.append([p,sum])
print(out)
print(sorted(out,key=lambda x: x[1], reverse=True)[0])