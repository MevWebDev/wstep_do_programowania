punkty = int(input("Podaj swoje punkty: "))
#nie wiem jakie dokladne sa punktacje wiec dalem losowo
if (punkty<51):
    print("Nie zdales")
elif(punkty > 51 and punkty < 60):
    print("3")
elif(punkty > 61 and punkty < 70):
    print("3.5")
elif(punkty > 71 and punkty < 80):
    print("4")
elif(punkty > 81 and punkty < 90):
    print("4.5")
elif(punkty > 51 and punkty < 60):
    print("5")
else:
    print("Zakres punktow to 0-100")