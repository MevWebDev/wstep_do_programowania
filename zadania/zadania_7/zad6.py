x = 9
list = [1,2,3,4,5,5,5,5,5,6,7,8,9]
def binary_search(list, x):

    low=0
    high=len(list)-1
    mid=0
    lower = higher = even = 0
    while low<=high:

        mid=(low+high)//2
        if list[mid]==x:
            for i in range(1,len(list)):
                if list[mid] == list[mid-1]:
                    mid = mid-1 
                else:
                    break
            
            for i in range(0,mid):
                lower += 1
            
            for i in range(1,len(list)):
                if mid + i + 1 >= len(list) or list[mid + i] != list[mid + i + 1]:
                    mid = mid+1
                else:    
                    break
            for i in range (mid+1,len(list)):
                higher += 1
            
        
            even = len(list) - lower - higher
            return higher,lower,even
            
        elif list[mid]>x:

            high=mid-1

        else:

            low=mid+1

    return False
print(binary_search(list,x))