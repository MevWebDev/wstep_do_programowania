slowo = input("Podaj slowo: ")
ile_a = 0
ile_e = 0
ile_i = 0
ile_o = 0
ile_u = 0
ile_y = 0
samogloski = 0
for i in range(len(slowo)):
    if (slowo[i] == 'a' or slowo[i] == 'A'):
        ile_a = ile_a +1
        samogloski = samogloski + 1
    if (slowo[i] == 'e' or slowo[i] == 'E'):
        ile_e = ile_e +1
        samogloski = samogloski + 1
    if (slowo[i] == 'i' or slowo[i] == 'I'):
        ile_i = ile_i +1
        samogloski = samogloski + 1
    if (slowo[i] == 'o' or slowo[i] == 'O'):
        ile_o = ile_o +1
        samogloski = samogloski + 1
    if (slowo[i] == 'u' or slowo[i] == 'U'):
        ile_u = ile_u +1
        samogloski = samogloski + 1
    if (slowo[i] == 'y' or slowo[i] == 'Y'):
        ile_y = ile_y +1
        samogloski = samogloski + 1

print("Liczba samoglosek to: " + str(samogloski))
print("A: " + str(ile_a))
print("E: " + str(ile_e))
print("I: " + str(ile_i))
print("O: " + str(ile_o))
print("U: " + str(ile_u))
print("Y: " + str(ile_y))