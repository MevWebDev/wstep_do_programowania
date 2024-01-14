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
message = "itcógm uyrdlgtuml yr jrcy"
def uncode(dic,message):
    odkodowane = ""
    for letter in message:
        if (letter in dic.values()):
            for key,value in dic.items():
                if (value==letter):
                    toChange = key
                    odkodowane += toChange
        else:
            odkodowane += letter
    return odkodowane
print(uncode(dic,message))