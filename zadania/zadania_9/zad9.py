liczba = 123
suma = 0
def sumaliczba(liczba):
    global suma
    if liczba>0:
        cyfra = liczba % 10
        suma += cyfra
        return sumaliczba(liczba // 10)
    return suma
print(sumaliczba(liczba))