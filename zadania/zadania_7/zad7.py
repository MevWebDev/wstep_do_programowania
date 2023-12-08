a = 0
b = 3
kroki = 0
epsilon = 1
def f(x):
    return (x**3 - 2*x**2+x-7)

def miejsce_zerowe(a,b,eps):
    kroki = 0
    while abs(a-b) > eps:
        x1 = (a+b)/2
        if abs(f(x1)) <= eps:
            break
        elif f(x1) * f(a) <= 0:
            b = x1
        else:
            a = x1
        kroki += 1
    print(kroki)
    return ((a + b) / 2)
    
   
print(miejsce_zerowe(a,b,epsilon))



            
        

        
    
    