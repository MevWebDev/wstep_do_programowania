
podzbiory = []
def wyznaczanie_podzbiorow(n):
    obecny_podzbior = []
    zbior = []
    for i in range (1,n+1):
        zbior.append(i)
    if podzbiory == []:
        podzbiory.append('pusty')
    while obecny_podzbior != zbior:  
        for  i in range((len(zbior)-1),-1,-1):
            if zbior[i] not in obecny_podzbior:
                if i != len(zbior)-1:
                    index = obecny_podzbior.index(zbior[i+1])
                else:
                    index = i
                del obecny_podzbior[index:]
                obecny_podzbior.append(zbior[i])
                
                break
        podzbiory.append(obecny_podzbior[:])
        print(obecny_podzbior)
        
    return podzbiory
print(wyznaczanie_podzbiorow(6))
#1,2,3,6 sprawdza ze 5 nie jest w podzbiorze wiec usuwa 6 i wstawia 5
#1,2,3,5 sprawdza ze 6 nie jest w podzbiorze wiec dodaje 6 i usuwa 
#1,2,3,5,6 sprawdza ze 4 nie jest w podzbiorze wiec dodaje 4 i usuwa 