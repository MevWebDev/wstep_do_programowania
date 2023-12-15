list = [1,3,5,7,9,2]
def wstaw(lista):
    x = lista[-1]
    for i in range(len(lista)):
        if lista[i] > x:
            lista.insert(i,x)
            lista.pop(-1)
            return lista
print(wstaw(list))
