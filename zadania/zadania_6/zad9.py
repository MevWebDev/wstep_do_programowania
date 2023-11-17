lista = [1,2,3,4,5,6,7,8,9,10]
def parzystaLista(list):
    plista = []
    for i in list:
        if(i%2==0):
            plista.append(i)
    return plista
print(parzystaLista(lista))
