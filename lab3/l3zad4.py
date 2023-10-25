życia = 3
odp = 1
pyt1 = "8 + 2"
pyt2 = "16 - 12"
pyt3 = "3 * 5"
#zmieniłem koncepcje i stworzyłem
#grę gdzie trzeba odpowiedzieć na 3 pytania i ma się 3 życia
while (odp != pyt1):
    if(życia == 0):
        print("Zginales")
        quit()

    odp = int(input("Podaj wynik działania: " + pyt1 + " "))
    if (odp == 10):
        break
    życia -= 1
    print("Zła odpowiedź. Pozostało ci " + str(życia) + " żyć")

while (odp != 4):
    if (życia == 0):
        print("Zginales")
        quit()
    odp = int(input("Podaj wynik działania: " + pyt2 + " "))
    if (odp == 4):
        break
    życia -= 1
    print("Zła odpowiedź. Pozostało ci " + str(życia) + " żyć")
while (odp != 15):
    if (życia == 0):
        print("Zginales")
        quit()
    odp = int(input("Podaj wynik działania: " + pyt3 + " "))
    if (odp == 15):
        break
    życia -= 1
    print("Zła odpowiedź. Pozostało ci " + str(życia) + " żyć" )
print("Gratulacje zdałeś :D")



