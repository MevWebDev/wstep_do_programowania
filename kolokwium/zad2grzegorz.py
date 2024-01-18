def generatesubzbiory(n, podzbiory=[]):
    a = list(range(1, n + 1))
    for i in range(1, n + 1):
        podzbiory.append([i])

    for i in range(n):
        for j in range(i + 1, n):
            c = [a[i], a[j]]
            podzbiory.append(c)
    podzbiory.append(a)


    return podzbiory

print(generatesubzbiory(5))