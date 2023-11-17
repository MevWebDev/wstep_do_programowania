list = [1, 2, 3, 2, 2, 4, 5, 3, 1]

def bezPowtorzen(list):
    sorted_list = sorted(list)
    nowaLista = []
    for i in range(len(sorted_list)-1):
        if sorted_list[i] != sorted_list[i+1]:
            nowaLista.append(sorted_list[i])
    nowaLista.append(sorted_list[-1])
    print(nowaLista)

bezPowtorzen(list)