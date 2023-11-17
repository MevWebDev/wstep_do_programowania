alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","v","w","x","y","z"]
def panagram(slowo):
    
    test = slowo.lower()
    for i in range(len(test)):
        noSpace = []
        if (test[i] != " "):
            noSpace.append(test[i])
    noSpace.sort()
    
    for i in range(len(slowo)):
        if noSpace[i] != alfabet[i]:
            return False
        return True
slowo = "The quick brown fox jumps over the lazy frog"
print(panagram(slowo))           
