def checkBigger(liczba1,liczba2):
    if liczba1 > liczba2:
        print("Liczba 1 jest wieksza")
    elif liczba1 < liczba2:
        print("Liczba 2 jest wieksza")
    else :
        print("Liczby sa rowne")

liczba1 = int(input("Podaj liczbe 1: "))
liczba2 = int(input("Podaj liczbe 2: "))
checkBigger(liczba1, liczba2)
