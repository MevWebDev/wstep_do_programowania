grocery={}
grocery={"mleko":1, "chleb":2}
print(grocery)
grocery["woda"]=5
print(grocery)
for val in grocery.values():
    print (val)
for key in grocery.keys():
    print (key)
programmingLangauges = {1:"Python",2:"CSharp",3:"PHP"}
#if value exists, it returns the value
print(programmingLangauges.get(1))
#if value doesn't exist, it returns None
print(programmingLangauges.get(4))
print(programmingLangauges.values())
print(programmingLangauges.pop(3))
print(programmingLangauges)
if 3 in programmingLangauges:
    del programmingLangauges[3]
print(programmingLangauges)
letters = ['a','b','c','d']
numbers = [1,2,3,4]
myDict = dict(zip(letters,numbers))
print(myDict)
programmingLangauges = {1:"Python",5:"Java",3:"PHP"}
for key in sorted(programmingLangauges):
    print(key,programmingLangauges[key])