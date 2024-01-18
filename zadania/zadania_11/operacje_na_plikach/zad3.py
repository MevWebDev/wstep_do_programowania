file = open("file.txt", "r+")
content = file.read()
dic = {'a': 'c', 'ą': 'ć', 'b': 'd', 'c': 'e', 'ć': 'ę', 'd': 'f', 'e': 'g', 'ę': 'h',
       'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'ł', 'k': 'm', 'l': 'n', 'ł': 'ń',
       'm': 'o', 'n': 'ó', 'ń': 'p', 'o': 'r', 'ó': 's', 'p': 'ś', 'r': 't', 's': 'u',
       'ś': 'w', 't': 'y', 'u': 'z', 'w': 'ź', 'y': 'ż', 'z': 'a', 'ź': 'ą', 'ż': 'b'}

content = content.lower()
zakodowane = ''
for letter in content:
    if letter in dic:
        to_change = dic.get(letter)
        zakodowane += to_change
    elif letter == " ":
        zakodowane += " "
    else:
        zakodowane += letter

zakodowane = zakodowane.upper()
file_cesar = open("file-cesar.txt", "w")
file_cesar.write(zakodowane + "\n")

file.close()
file_cesar.close()

