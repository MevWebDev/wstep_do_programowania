d ={"1":1,
    "2":3,
    "3":3,
    "4":4,
    "5":5,
    }
v = 3
e = 5
def replace(d,v,e):
    for key,value in d.items():
        if value == v:
            d.update({key:e})
    return d.values()

print(replace(d,v,e))
