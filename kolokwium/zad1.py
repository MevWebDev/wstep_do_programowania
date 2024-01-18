n = 6
def pyramid(n):
    for i in range(1,n+1):
            for space1 in range(n-i):
                 print(" ", end="")
            for j in range(1,i+1):
                print(j,end="") 
            for l in reversed(range(1,i)):
                print(l,end="") 
            print()
(pyramid(n))