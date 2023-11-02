word1 = input("Podaj 1 slowo: ")
word2 = input("Podaj 2 slowo: ")

if (len(word1) > len(word2)):
    print("Slowo 1 jest dluzsze")
elif (len(word1) < len(word2)):
    print("Slowo 2 jest dluzsze")
elif (len(word1) == len(word2)):
    print("Slowa sa rowne")
