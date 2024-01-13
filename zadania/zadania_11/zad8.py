dic = {'I':1,
       'V':5,
       'X':10,
       'L':50,
       'C':100,
       'D':500,
       'M':1000
    }
liczba = 3999
def dec_to_rome(dic,liczba):
    i = 0
    rome = ''
    keys = list(dic.keys())
    while liczba != 0:
        key = keys[-1-i]
        if liczba >= dic.get(key):
            rome += key
            liczba -= dic.get(key)
        else:
            liczbastr = str(liczba)
            if len(liczbastr) >= 3 and key == "M" and liczbastr[-3] == "9":
                rome += "CM"
                liczba -= 900
            elif len(liczbastr) >= 3 and key == "D" and liczbastr[-3] == "4":
                rome += "CD"
                liczba -= 400
            elif len(liczbastr) >= 2 and key == "C" and liczbastr[-2] == "9":
                rome += "XC"
                liczba -= 90
            elif len(liczbastr) >= 2 and key == "L" and liczbastr[-2] == "4":
                rome += "XL"
                liczba -= 40
            elif len(liczbastr) >= 1 and key == "X" and liczbastr[-1] == "9":
                rome += "IX"
                liczba -= 9
            elif len(liczbastr) >= 1 and key == "V" and liczbastr[-1] == "4":
                rome += "IV"
                liczba -= 4
            i += 1
            
    return rome 
print(dec_to_rome(dic,liczba))

#SCHEMAT DZIALANIA
#sprawdza czy 628 > M / nie
#sprawdza czy liczba = x900
#Tak: Wypisuje CM
#sprawdza czy 628 > D / tak
#wypisuje D i odejmuje od 628
#sprawdza czy 628 > D / nie
#sprawdza czy liczba = x400
#Tak: Wypisuje CD
#sprawdcza czy 128 > C / tak
#wypisuje C i odejmuje od 128
#sprawdcza czy 128 > C / nie
#sprawdza czy liczba = x90
#Tak: Wypisuje XC
#sprawdza czy 28 > L / nie
#sprawdza czy liczba = x40
#Tak: Wypisuje XL
#sprawdza czy 28 > X / tak
#wypisuje X i odejmuje od 28
#sprawdza czy 18 > X / tak
#wypisuje X i odejmuje od 18
#sprawdza czy 8 > X / nie
#sprawdza czy liczba == 9
#Tak: Wypisuje IX
#Nie: Idzie dalej
#sprawdza czy 8 > V / tak
#wypisuje V i odejmuje od 8
#sprawdza czy 3 > V / nie
#sprawdza czy liczba = 4
#Tak: Wypisuje IV
#sprawdza czy 3 > I / nie