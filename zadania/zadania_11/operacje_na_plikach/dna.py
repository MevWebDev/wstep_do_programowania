file_dna = open('file-dna.txt', 'r')
content = file_dna.read()
def dna_validator(content):
    content = content.upper()
    #3b)
    content = content.replace('N', "")
    content= content.replace('-', "")

    gaga_counter = content.count("GAGA")
    ctgaa_counter = content.count("CTGAA")
    content = content.replace("GAGA", "AGAG")
    G_index = content.rindex("GGGGGGG")
    print("3c) GAGA wystąpiło: " + str(gaga_counter) + " razy")
    print("3f) CTGAA wystąpiło: " + str(ctgaa_counter) + " razy")
    print("3d) Indeks wystąpienia 7 guanin z rzędu to: " + str(G_index))
    #3h)
    RNA = content.replace("T", "U")
    for letter in content:
        if letter not in ['A', 'G', 'C', 'T','\n']:
            return "Kod DNA jest niepoprawny"
    return "3a) Kod jest poprawny"
    
print(dna_validator(content))

