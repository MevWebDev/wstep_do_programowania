sublist_1= []
sublist_2 = []
for i in range(20):
    sublist_1.append(i+1)

for i in reversed(range(len(sublist_1))):
    sublist_2.append(i+1)


list = [sublist_1,sublist_2]
print(list)