list1 = [1,2,4,7,8]
list2 = [1,2,7,8,9]
def funkcja1 (lista1,lista2):
    if len(lista1) <= len(lista2):
        x = len(lista2)-1
    else:
        x = len(lista1) -1
    for i in range (0,x):
        if lista1[i] != lista2[i]:
            return i
        else:
            continue
print(funkcja1(list1,list2))

def funkcja2(lista1,lista2):
    wspolne = []
    for i in range (0, funkcja1(lista1,lista2)):
        wspolne.append(list1[i])
    return wspolne

print(funkcja2(list1,list2))
