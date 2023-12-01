przedzial = [0,3]
x = przedzial[0]
funkcja = x**3 - x + 1
print(funkcja)
x = przedzial[len(przedzial)-1]
funkcja = x**3 - x + 1
print(funkcja)
przedzial = [przedzial[0] + (przedzial[len(przedzial) - 1] - przedzial[0]) / 2]
print(przedzial)


