def odTylu(slowo):
    rewers = ""
    for i in range(len(slowo)):
        rewers += slowo[-1 - i]
    print(rewers)

slowo = "Franek"
odTylu(slowo)