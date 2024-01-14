def recursive_powering(a,b):
    if b != 0:
        return (a*recursive_powering(a,b-1))
    else:
        return 1
print(recursive_powering(2,3))

#2 * r(2,2)
# 2*2*r(2,1)
#2*2*2*r(2,0)
#koniec