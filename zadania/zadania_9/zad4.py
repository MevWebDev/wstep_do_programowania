def kwadrat(n):
    if (n==1):
        return 1
    else:
        return (kwadrat(n-1) + n-1 + n)
print(kwadrat(5))

#f(1)^2 = 1
#f(2) = f(1) + 1 + 2
#f(3) = f(2) + 2 + 3
#f(4) = f(3) + 3 + 4
#f(5) = f(4) + 4 + 5