list = [5,6,7,8,9,1,2,0,3,5,6,5]
x = 5
def szukajX(x,lista):
    for i in reversed(range(len(lista))):
        if (lista[i]==x):
            return i
        
print(szukajX(x,list))

