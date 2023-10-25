
opcja = input("""Witaj w kalkulatorze :)"
      "Wybierz opcje:"
      "1. Dodawanie"
      "2. Odejmowanie"
      "3. Mnożenie:
      """)
x = int(input("Podaj 1 liczbe: "))
y = int(input("Podaj 2 liczbe: "))
if opcja == "1":
    print(x+y)
elif opcja == "2":
    print(x-y)
elif opcja == "3":
    print(x*y)
else:
    print("Nieprawidłowa opcja!")
