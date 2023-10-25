a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))
r = None
x = 1
while x == 1:
  if (a%b!=0):
      r = a % b
      a = b
      b = r
  else:
      print(b)
      break


