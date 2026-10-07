s = "Hello World"
print(s.split())
print(s.replace("World", "Py"))

print(s.startswith("  He") )
print(s.find("World") )
print(s.index("World") )
print(s.encode("utf-8"))
#boolean
print(bool('shubham'))

name = 'shubham'
age = 21
relationshipStatus = 'single'
relationshipStatus = "it\'s complicated"
print(relationshipStatus)
birth=input("which year you were born into ? ")
print('\n')
age = 2026-int(birth)     #---->Type converting string to int
print('your age is : ',age)