#f(0) robi nic / suma = 0
#f(1) robi nic/ suma = 0
#f(2) dodaje 2 / suma = 2
#f(3) = f(2) i robi nic / suma = 2
#f(4) = f(3) i dodaje 4/ suma = 4
#f(5) = f(4) i dodaje nic / suma = 4
#f(6) = f(5) i dodaje 6 / suma = 10

def sumaParzyste(n):
    if(n==0) or (n==1):
        return 0
    if (n == 2):
        return 2
    elif (n%2==1):
        return sumaParzyste(n-1)
    else:
        return (sumaParzyste(n-1)) + n
    
print(sumaParzyste(10))

#write some code to test my function
assert sumaParzyste(0) == 0
assert sumaParzyste(1) == 0
assert sumaParzyste(2) == 2
assert sumaParzyste(3) == 2
assert sumaParzyste(4) == 6





