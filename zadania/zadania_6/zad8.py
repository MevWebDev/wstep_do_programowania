def czyPierwsza(liczba):
    
    for i in range(2,liczba):
        if (liczba % i == 0):
            return False
    return True
print(czyPierwsza(4))
    
    