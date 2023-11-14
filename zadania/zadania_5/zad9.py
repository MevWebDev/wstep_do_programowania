list = [1,3,5,7,9,10]
list.pop(-1)
list2 = [2,4,6,8]
for i in range(len(list2)):
    list.append(list2[i])

print(list)