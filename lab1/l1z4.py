import math
x = float(input("Podaj liczbe zmiennoprzecinkowa: "))
y = float(input("Podaj druga liczbe zmiennoprzecinkowa: "))
wynik = (x+y) + (x-y) + (x*y) + (x/y)
print(math.floor(wynik))