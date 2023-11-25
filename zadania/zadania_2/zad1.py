i = 1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")
    i = 0
while i < 10:
    i += 1
    if i == 5:
        break
    print("Aktualny numer to", i)
print("Jestem poza pętlą")