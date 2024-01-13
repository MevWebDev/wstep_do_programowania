
def binsearch(list, element):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == element:
            return True
        elif list[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
    return False

x = [1, 2, 3, 4, 5, 6]
print(binsearch(x, 4))


