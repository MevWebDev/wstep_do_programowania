import random
matrix = []
list = []
sum = []
suma = 0

for i in range(4):
    list = []
    suma = 0
    for x in range(4):
        
        rand = random.randint(1,10)
        list.append(rand)
        suma += rand
    matrix.append(list)
    sum.append(suma)


print(matrix)
print (min(sum))
print (max(sum))

