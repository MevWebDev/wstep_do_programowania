import random
list = []
def funkcja(n):
    
    for i in range (n):
        list.append(random.randint(1,10))
    return(list)

print(funkcja(15))
