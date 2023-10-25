x = None
suma = 0
while x!=0:
    x = int(input("Podaj liczbe: "))
    suma += x
    if x==0:
        print("Suma liczb to: "+ str(suma))
        break