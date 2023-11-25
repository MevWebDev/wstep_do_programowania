n = 11110101
n = str(n)
liczba = 0
i = 0
for x in reversed(n):
    liczba += int(x)*(2**i)
    i+=1
print(liczba)