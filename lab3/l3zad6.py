n = int(input("Podaj n: "))
for x in range (1, n+1):
    for x in range (1, n+1):
        if(x%2 == 1):
            print("1", end="")
        else:
            print("0", end="")
    print()