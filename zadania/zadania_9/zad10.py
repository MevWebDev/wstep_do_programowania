def head(lista):
    return lista[0]

def tail(lista):
    newlist = lista
    toRemove = head(lista)
    newlist.remove(toRemove)
    return newlist


revlist = []
def rewers(lista):
    if len(lista) > 0:
        revlist.insert(0,head(lista))
        return rewers(tail(lista))
    return revlist
print(rewers([1,2,3,4,5]))
