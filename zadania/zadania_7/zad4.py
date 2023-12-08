
import math
from itertools import count
list = [1,2,3,5,5,5,5,5,5,5,7,8,9,10,11]
dlugosc = int(math.log(len(list),2))
x = 11
def szukajX(x,lista):
    low=0

    high=len(lista)-1

    mid=0

    while low<=high:

        mid=(low+high)//2
        i = 0
        if list[mid]==x:
            for i in range(0, len(lista) - 1):
                if mid + i + 1 >= len(lista) or lista[mid + i] != lista[mid + i + 1]:
                     return mid + i
                
                    

        elif list[mid]>x:

            high=mid-1

        else:

            low=mid+1

    return False
        
    
print(szukajX(x,list))
                

