list = [1,2,3,4,5]
list_2 = []
for i in range (len(list)):
     if i == 0:
        list_2.append(list[-1])
     elif i == len(list) -1:
        list_2.append(list[0])
     else:
        list_2.append(list[i])
   
print(list_2)
    

