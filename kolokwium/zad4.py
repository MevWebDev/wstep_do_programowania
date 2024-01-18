lista = [6,0,3,5]
def bubblesort(lista):
    for x in range(len(lista) - 1):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                swap = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = swap
    return lista
def mediana(lista):
    lista = bubblesort(lista)
    if len(lista) % 2 == 1:
        median_index = len(lista) // 2
        return lista[median_index]
    else:
        median_index1 = len(lista) // 2 - 1
        median_index2 = len(lista) // 2
        median = (lista[median_index1] + lista[median_index2]) / 2
        return median
matrix = [[2,3,1,5],[3,3,2,5],[2,3,1,7],[5,2,3,4]]

def matrixmediana(matrix):
    lista = []
    for row in matrix:
        print(row)
    for i in range(len(matrix)):
        lista.append(matrix[i][i])
    print("--------------")
    print(lista)
    result = mediana(lista)
    return result
print(matrixmediana(matrix))

