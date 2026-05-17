name = 'Shubham Ojha'
age = 20
#types of ways in which we can do print the formatted strings

#normal way
#print('hi ' + name + 'you are ' + age + 'years old') #this is wrong, because age is integer and we want it in string hence.
print('hi ' + name + ' you are ' + str(age) + ' years old') 

#better way
print(f'hi {name} you are {age} years old')

#best way
#print("hi {} you are {} years old").format(name,age) #this wrong because print() func is not string and it is used only for string
print("hi {} you are {} years old".format(name,age))

print("hi {1} you are {0} years old".format(name,age)) #here in CS everything starts with zero and name is here is zero and age is one and we tried giving the values which will eventually make it up side down

print("hi {} you are {} years old".format('tnOjha','57')) #you can directly pass the value inside the function

#print("hi {} you are {} years old".format(new_name= 'Hello world',age)) #this is wrong as you cannot pass ew values initialized variables inside the format () 
 
