sorted_list = [1,2,3,4,5,6]
x = 7
def recursive_search(i,x):
    if (i >= len(sorted_list)):
        return False
    elif (sorted_list[i] == x):
        return True
    else:
        return recursive_search(i+1,x)
print(recursive_search(0,x))