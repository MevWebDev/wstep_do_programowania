zdanie = input("Podaj slowo do sprawdzenia czy jest palindromem: ")
czyPalindrom = True
for i in range(len(zdanie)):
    if zdanie[i] != zdanie[len(zdanie) -1 -i]:
        czyPalindrom = False
        break         
    
          
if czyPalindrom:
       print("Zdanie jest palindromem")
else:
       print("Zdanie nie jest palindromem")
