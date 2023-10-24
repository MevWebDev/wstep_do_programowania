import math
a = float(input("Podaj wspolczynnik a: "))
b = float(input("Podaj wspolczynnik b: "))
c = float(input("Podaj wspolczynnik c: "))
delta = pow(b,2) - 4 * a * c
print("Delta wynosi: " +str(delta))
if delta > 0:
    print("Trojmian ma rozwiazanie")
    x1 = (-b - (math.sqrt(delta)))/(2*a)
    x2 = (-b + (math.sqrt(delta)))/(2*a)
    print("Rozwiazanie 1 to: " + str(x1))
    print("Rozwiazanie 2 to: " + str(x2))
elif delta == 0:
    print("Trojmian ma jedno rozwiazanie")
    x = (-b/(2*a))
    print("Rozwiazanie to: " + str(rozwiazanie))
else:
    print("Trojmian nie ma rozwiazania")





