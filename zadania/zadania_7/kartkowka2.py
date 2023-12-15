# Napisz funkcje, ktora odpowie na pytanie czy x znajduje sie w liscie uporzadkowanej. Nie mozna iterowac po liscie.
# Przyklad:
# czy_w_liscie([1, 2, 3, 4, 5], 3) -> True
# czy_w_liscie([1, 2, 3, 4, 5], 6) -> False

def czy_w_liscie(lista,x):
    low = 0
    high = len(lista)-1
    mid = 0
    while low <= high:
        mid = (low+high)//2
        if lista[mid] == x:
            return True
        elif lista[mid] > x:
            high = mid-1
        else:
            low = mid +1
    return False

print(czy_w_liscie([1, 2, 3, 4, 5], 3))
print(czy_w_liscie([1, 2, 3, 4, 5], 6))
print(czy_w_liscie([1, 2, 3, 4, 5, 5, 5, 5, 5], 3))
print(czy_w_liscie([1, 2, 3, 4, 5, 5, 5, 5, 5], 6))
print(czy_w_liscie([], 3))
print(czy_w_liscie([1], 3))

        
            
    

