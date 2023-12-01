x = 5
list = [3,5,7,3,9,7,4,5,2]
def algorytm(x,lista):
    mniejsze = wieksze = rowne = 0
    print(lista)
    print(x)
    for l in lista:
        if l>x:
            wieksze += 1
        elif l < x:
            mniejsze += 1
        else:
            rowne +=1
    return wieksze,mniejsze,rowne
print(algorytm(x,list))

