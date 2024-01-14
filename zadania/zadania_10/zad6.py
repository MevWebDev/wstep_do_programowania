#szyfr cezara
dic={'a':'c',
     'ą':'ć',
     'b':'d',
     'c':'e',
     'ć':'ę',
     'd':'f',
     'e':'g',
     'ę':'h',
     'f':'i',
     'g':'j',
     'h':'k',
     'i':'l',
     'j':'ł',
     'k':'m',
     'l':'n',
     'ł':'ń',
     'm':'o',
     'n':'ó',
     'ń':'p',
     'o':'r',
     'ó':'s',
     'p':'ś',
     'r':'t',
     's':'u',
     'ś':'w',
     't':'y',
     'u':'z',
     'w':'ź',
     'y':'ż',
     'z':'a',
     'ź':'ą',
     'ż':'b'}

slowo = "FRANEK STOBIERSKI TO GOAT"
slowo = slowo.lower()
zakodowane =''
for letter in slowo:

    if (letter in dic):
            toChange = dic.get(letter)
            zakodowane += toChange
    elif (letter == " "):
        zakodowane += " "
    else:
         zakodowane += letter

print(slowo.upper())
print(zakodowane)
