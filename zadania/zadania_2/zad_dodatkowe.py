a = 23
suma = 0
b = 15
while a != 1:
    a>>= 1
    b<<=1
    if (a%2!=0):
        suma += b
    print(a,b)
    

print(suma)