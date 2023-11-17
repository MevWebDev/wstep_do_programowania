def checkBigger(liczba1,liczba2):
    if liczba1 > liczba2:
        wieksza = liczba1
        return liczba1
    elif liczba1 <= liczba2:
        wieksza = liczba2
        return liczba2
a=10
b=15
c=20
print(checkBigger(checkBigger(a,b),c))