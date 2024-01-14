def f(n):
    print(n)
    if n>99:
        return n-10
    return f(f(n+11))
print(f(98))

# printuje 98
# zwraca f(f(109)) czyli printuje 109 i zwraca 99
# printuje 99
# zwraca (f(f110)) czyli printuje 110 i zwraca 100
# printuje i zwraca i konczy dzialanie
