#silnia(0) = 1
#silnia(1) = silnia(0)
#silnia (2) = silnia(1) * 2
#silnia(3) = silnia(2) * 3
#silnia(4) = silnia(3) * 4
#silnia(5) = silnia(4) * 5

def silnia (n):
    if n > 0:
        return silnia(n-1) * n
        
    else:
        return 1
print (silnia(5))

    
    