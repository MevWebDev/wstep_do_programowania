import random
matrix = []
list1 = []
list2 = []
start = random.randint(1,20)
l = random.randint(1,20)
print(start)
for x in range (l):
    list1.append(start + x)
toAppend = list1[-1]
for y in range(l):
    list2.append(toAppend +1 + y)
matrix = [list1, list2]
print(matrix)
