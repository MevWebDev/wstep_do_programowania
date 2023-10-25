slowo = input("Podaj słowo: ")
znak = input("Podaj znak: ")
i = 0
licznik = 0
while i < len(slowo):
    if(slowo[i] == znak):
        licznik += 1
    i+=1
print(licznik)
