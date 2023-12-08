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