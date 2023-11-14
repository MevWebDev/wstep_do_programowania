matrix = [[1,2,4,6],[2,3,4,5],[12,3,4,5]]
print(type(matrix))
matrix_multiplied = []
matrix_final =[]
skalar = 3
for x in matrix:
    matrix_multiplied =[]
    for i in range(len(x)):
        multi = x[i] * skalar
        matrix_multiplied.append(multi)
    matrix_final.append(matrix_multiplied)
print(matrix_final)

