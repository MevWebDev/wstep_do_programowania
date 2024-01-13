def maxsort(list):
    sorted_list = []

    for i in range(len(list)-1, 0, -1):
        current_max_index = 0

        
        for j in range(1, i+1):
            if list[j] > list[current_max_index]:
                current_max_index = j

        
        list[i], list[current_max_index] = list[current_max_index], list[i]

    return list

unsorted_list = [4, 2, 3, 1]
sorted_list = maxsort(unsorted_list)
print(sorted_list)
