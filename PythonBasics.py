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


#---------------------------------------- #NEXT DAY

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