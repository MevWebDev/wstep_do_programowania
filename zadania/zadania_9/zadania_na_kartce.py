# # Zad 1.
# def s(n): 
#     if n<1:
#         return n
#     return n + s(n-1)
# print (s(5))

# # Kroki:
# # 5 + s(4)
# # 5 + 4 + s(3)
# # 5 + 4 + 3 + s(2)
# # 5 + 4 + 3 + 2 + s(1)
# # 5 + 4 + 3 + 2 + 1 + s(0)
# # = 15

# # Zad 2.

# def f(n):
#     if n<1:
#         return 0
#     else:
#         print(n)
#         f(n-1)
#         print(n)
# # Kroki:
# # f(3)
# # 3,f(2),3
# # 3,2,f(1),2,3
# # 3,2,1,1,2,3

# Zad3.
# g(n):
#     if n > 0:
#         n-=1
#         g(n)
#         print(n)
#         n-=1
#         g(n)


# # g(3)
# #  g(2) 2, g(1)       

# #  g(1),1 g(0)
 
# #  g(0) = none
# #  g(1) = g(0) print (0) g(-1) / printuje 0
# #  g(2) = g(1) print(1) g(0) / printuje 0 i 1
# #  g(3) = g(2) print (2) g(1) / printuje 0 i 1 i 2 i 0
# #  g(4) = 0,1,2,0,3,0,1


# #  Zad4.

#  def fun(a,n)
#     if n == 1
#         return a[0]
#     else:
#         x = fun (a,n-1)
#     if x > a[n-1]
#         return x
#     else:   
#         return a[n-1]
# l = 12,10,30,50,40

# print fun(l,5)

# # fun(l,1) / return 12
# # fun(l,2) / x = 12 , if 12 > 10 -> returns 12
# # (l,3) / x = 12 , if x > 30 -> returns 30
# # l,4 / x = 30 if x>50 -> returns 50
# # l,5 / x = 50 if x>40 - > returns 50








