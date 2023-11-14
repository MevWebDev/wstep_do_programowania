import random
matrix =[]
transportedList = []
transportedMatrix = []
list = []
for x in range(3):
    list = []
    for i in range(4):
        list.append(random.randint(1,10))
    matrix.append(list)
for list in matrix:
    print(list)
print("----------------")
for x in range(4):
    transportedList = []
    for i in range(3):
        transportedList.append(matrix[i][x])
    transportedMatrix.append(transportedList)
for list in transportedMatrix:
    print(list)
    



