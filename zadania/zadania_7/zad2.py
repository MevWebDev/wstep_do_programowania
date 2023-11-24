import random
list = []
def funkcja(n):
    
    for i in range (n):
        if (i==0):
            x = 1
        else:
            x = random.randint(x+1,10+x)
       
        list.append(x)
        
    
    return(list)

print(funkcja(8))
