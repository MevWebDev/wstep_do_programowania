
def suma(n):
       
    if n == 1:
        return 1/n
    else:
        return suma(n-1) + 1/n





print(suma(5))


#sum(1) == 1/1
#sum(2) == sum(1) + 1/2
#sum(3) == sum(2) + 1/3
#sum(4) == sum(3) + 1/4
#sum(5) == sum(4) + 1/5

