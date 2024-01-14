lista1 = [1,2,3,4,6]
lista2 = [3,1,2,5,4]
lista3 = ["a","b","c","d","f"]
lista4 = ["c","e","a","b","d"]



def isPermutation(list1,list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    if list1 == list2:
        return True
    else:
        return False

print(isPermutation(lista1,lista2))