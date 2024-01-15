file =  open('franek.txt', 'r')
content = file.read()
file_copy = open("franek-copy.txt", "w")
file_copy.write(content)


file.close()
file_copy.close()