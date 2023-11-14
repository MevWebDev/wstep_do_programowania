import random
n = 4
suma1 = 0
suma2 = 0
suma = 0
for x in range(n):
    list = []
    index = 0
    for y in range(n):
        list.append(random.randint(1,10))
    
    suma1 += list[x]
    suma2 += list[-1 -x]
     
    print(list)
suma = suma1 + suma2
print(suma)

        

