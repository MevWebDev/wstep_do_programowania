import random
list = []
for i in range(10):
    list.append(random.randint(1,10))
list.sort()

toDelete = max(list)
while toDelete in list:
    list.remove(toDelete)
print(list[-1])