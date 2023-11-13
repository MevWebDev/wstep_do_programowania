import random
list = []
list_2 = []
for i in range(10):
    list.append(random.randint(1,10))
    
print(list)
for x in range(len(list)):
    if(x%2==0):
        list_2.append(list[x])
print(list_2)

    

