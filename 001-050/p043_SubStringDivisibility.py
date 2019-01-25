def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

pans = list(permutations("0123456789",10))            
npans = [ "%s%s%s%s%s%s%s%s%s%s" % x for x in pans ]
suma = 0

for num in npans:
    if (num[0] != "0"):
        if ((int(num[1:4]) % 2) == 0 ):
            if ((int(num[2:5]) % 3) == 0 ):
                if ((int(num[3:6]) % 5) == 0 ):
                    if ((int(num[4:7]) % 7) == 0 ):
                        if ((int(num[5:8]) % 11) == 0 ):
                            if ((int(num[6:9]) % 13) == 0 ):
                                if ((int(num[7:10]) % 17) == 0 ):
                                    print(num)
                                    suma+=int(num)

print(suma)