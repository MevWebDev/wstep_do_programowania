def recursive_powering(a,b):
    if b != 0:
        return (a*recursive_powering(a,b-1))
    else:
        return 1
print(recursive_powering(2,3))

#2 * r(2,2)
# 2*2*r(2,1)
#2*2*2*r(2,0)
#koniec


def binary_search(list, x):

    low=0

    high=len(list)-1

    mid=0

    while low<=high:

        mid=(low+high)//2

        if list[mid]==x:

            return mid

        elif list[mid]>x:

            high=mid-1

        else:

            low=mid+1

    return False
binary_search([2,3,4,5],6)



def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return