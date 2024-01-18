grocery_list = [
    {"ID":"0","Nazwa":"Masło","cena":"5.99","ilość":100},
    {"ID":"4","Nazwa":"Ryż","cena":"3.59","ilość":70},
    {"ID":"8","Nazwa":"Masło","cena":"5.99","ilość":100},
    {"ID":"10","Nazwa":"Ryż","cena":"3.59","ilość":70},
]
print("-----------")
# product = {"ID":"1","Nazwa":"Sok","cena":"3.99","ilość":50}
def addProduct(name,price,amount,grocery_list):
    newproduct = {}
    for i in range(len(grocery_list)):
        if grocery_list[i]["ID"] != i:
            newproduct.update({"ID":i+1, "Nazwa":name,"cena":price,"ilość":amount})
            grocery_list.insert(i+1,newproduct)
            return grocery_list    

# print(addProduct("Sok",3.99,50,grocery_list))
grocery_list = [
    {"ID":"0","Nazwa":"Masło","cena":"5.99","ilość":100},
    {"ID":"2","Nazwa":"Ryż","cena":"3.59","ilość":70},
    {"ID":"1","Nazwa":"Ryż","cena":"4.59","ilość":20},
]
print("-----------")
def READ(name,grocery_list):
    krotka = ()
    lista = []
    for item in grocery_list:
        for key,value in item.items():
            if key == "Nazwa":
                if value == name:
                    lista = list(krotka)
                    lista.append(item)
                    krotka = tuple(lista)
    return krotka
# print(READ("Ryż",grocery_list))

def UPDATE(id,discount,grocery_list):
    for item in grocery_list:
        if item["ID"] == str(id):
            item["cena"] = str(float(item["cena"]) * (1 - discount / 100))
    return grocery_list
# print (UPDATE(2,50,grocery_list))

def DELETE(min,max,grocery_list):
    copy = grocery_list.copy()
    for item in copy:
        if min < float(item["cena"]) < max:
            grocery_list.remove(item)
    return grocery_list

# print(DELETE(3,4,grocery_list))
def bubblesort(grocery_list):
    for j in range(len(grocery_list)):
        for i in range(len(grocery_list)-1-j):
            if grocery_list[i]["ilość"] > grocery_list[i+1]["ilość"]:
                grocery_list[i], grocery_list[i+1] = grocery_list[i+1], grocery_list[i]
    return grocery_list


def SEARCH(val,grocery_list):
    grocery_list = bubblesort(grocery_list)
    list = []
    l = 0
    p = len(grocery_list)
    if p == 0:
        return -1
    while True:
        s = (l+p)//2
        if grocery_list[s]["ilość"]<val:
            list.append(grocery_list[s]["ID"])
            grocery_list.pop(s)
            l = 0
            p = len(grocery_list)
        elif p-l == 1:
            break
        elif grocery_list[s]["ilość"] >= val:
            p=s
    if list == []:
        return -1
    return list


print(SEARCH(71,grocery_list))



            