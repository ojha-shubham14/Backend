name = input("what is youor name ? ")
print("heyyyyy " + name + " how is life going on ?")
print(type(7*7))



print(bin(5))
print(int("0b101",2)) #this is used to convert the binary form to the Int form and the 2 in the parameter pf the int is the form of the type which we have written i.e, we have written in binary form and hence that is the reason why we have put 2 not 10 (because 10 is used for decimals not for the binary)

a = 10 #no need to declare the variable for storing the TYPE i.e, int  a = 10 is wrong syntax
b = 21
print(a,b)

c,d,e = 4,5,6 #we can do assign like this
print(a,b,c,d,e)

#all about the string data type
print(type("Heyy shubham how you doing today ")) #note we can also type the sting in ' ' single strings
long_string = ''' 
wwwww 
*   *
-----
''' #now i can write the long string in multiple line unlike the single and the double strings
print(long_string)


#we can add the two different strings just like how we do for the Integers addition
firstName = 'shubham'
lastName =  'ojha'
full_name = firstName + ' ' + lastName 
print(full_name)
#string concatenations
print("hello " + "shubham ") #but we can only type the stings for concatenations i.e, this is wrong print("hello " + "14 ")

#Type casting
''' we can convert the integer type data to the string type by just doing the following operations'''
print(type(str(1408))) #-------> it is converted to string form
#now converting it to the integer form
print(type(int(str(1408)))) #-----> this will be in  the integer form as the string form is converted to the integer form
'''the other form of writing this and which is more easy to understand is :-'''
a=100
b=str(a) #------> makes 100 integer to string 
e= int(b) #------> makes the converted 100 in string to integer again 
c=type(b)
print(c)
d=type(e)
print(d)


