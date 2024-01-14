def NWD(a,b):
    if a>b:
        a = a-b
        return NWD(a,b)
    elif b>a:
        b = b-a
        return (NWD(a,b))
    else:
        return a
    
    
print(NWD(105,45))