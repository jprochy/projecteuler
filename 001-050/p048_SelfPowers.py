def main(n):
    suma = 0
    for i in range(1,n+1):
        suma+=i**i
    return str(suma)[-10:]
    
print(main(1000))