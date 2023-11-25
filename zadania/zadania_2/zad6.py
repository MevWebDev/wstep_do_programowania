n = 14
suma = 0
for i in range(1,n+1):
    if(n%i==0):
        print(i)
        suma += 1
print(suma)