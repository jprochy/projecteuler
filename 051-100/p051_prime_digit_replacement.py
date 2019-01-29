import time
start = time.time()


def sieve(limit):
    if limit < 2:
        return []
    if limit < 3:
        return [2]
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]


def is_family(p, d, primes):
    c = 0
    for r in '0123456789':
        np = int(p.replace(d, r))
        if(np > 100000 and np < 999999 and np in primes):
            c += 1
    return c == 8


primes = sieve(1000000)
n = 0
while True:
    n += 1
    p = primes[n]
    if p < 100000:
        continue
    if p > 999999:
        break
    ps = str(p)
    ld = ps[5:6]
    if (ps.count('0') == 3 and is_family(ps, '0', primes)) or\
       (ps.count('1') == 3 and ld != '1' and is_family(ps, '1', primes)) or\
       (ps.count('2') == 3 and is_family(ps, '2', primes)):
        print(f"Result: {n}  {ps}")
        break


end = time.time()
print("Time: {0:.4f} ms".format((end - start)*1000))
