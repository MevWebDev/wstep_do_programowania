lista = ["kajak", "kacper", "franeczekff"]
def funkcja(lista):
    licznik = 0
    for slowo in lista:
        if len(slowo) % 2 == 1:
            if slowo[0] == slowo[-1]:
                licznik += 1
    return licznik
print(funkcja(lista))

def rekurencyjna(lista, i, licznik=0):
    if i < len(lista):
        if len(lista[i]) % 2 == 1:
            if lista[i][0] == lista[i][-1]:
                licznik += 1
        return rekurencyjna(lista, i + 1, licznik)
    return licznik


print(rekurencyjna(lista, 0))