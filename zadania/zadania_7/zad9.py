list = [9,1,6,8,4,3,2,0]

def sort_by_max(lista):
    
    
    for i in range(len(lista)-1):
        max = 0
        for j in range (1,len(lista)-i):
            if lista[max] < lista[j]:
                max = j
        print(list[max])
        
        swap = lista[-1-i]
        lista[-1-i] = list[max]
        lista[max] = swap
        
    return lista
print(sort_by_max(list))

