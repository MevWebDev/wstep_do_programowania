x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
z = int(input("Podaj z: "))
if(x>y and x>z):
    print("X jest najwieksze")
elif(y>z and y>x):
    print("Y jest najwieksze")
elif(z>y and z > x ):
    print("Z jest najwieksze")
else:
    print("Nie ma najwiekszej liczby")