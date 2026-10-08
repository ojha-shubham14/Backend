#list declaration
list = ['a','shubham',2.25,True]
print(list)

#modifying list v/s assigning list

#Copying & Modifying list:
shopping_cart=['carrot','maggie',"banana"]

new_shopping_cart=shopping_cart[:] #this means the copy of the shopping cart
#new_shopping_cart=shopping_cart[0:1]
print(new_shopping_cart)

new_shopping_cart[0] ="watermellon"     #mdoifying the data of the list, we can also modify the original list.
print(new_shopping_cart,"\nnew shopping cart")
print(shopping_cart,"\nold shopping cart")

#assigning list:
new_shopping_cart = shopping_cart       #assigned old shopping cart to the new one and it's address is also assigned to new_shopping_cart
new_shopping_cart[1]="hanuman ji"
print(shopping_cart,"->this is original shopping cart") #here actually both new and old shopping_cart will be updated because in assigning, it gives the memory address as well so the changes made to the new_shopping_cart directly changes the memory address hence the shopping_cart will also be updated with the same as both uses the same memory address
print(new_shopping_cart,"-->This the new shopping cart")



#matrix --> nested list (used in ML and Image processing for computers to understand)

matrix = [
    [1,2,3],
    [0,1,0],
    [1,0,1]
]

print(matrix[0][2],"i.e, --> 2nd index of the first list") #--> that means matrix k andar ka 0th list k andar 2nd index , which is 3 so 3 will be printed


#list methods

basket = [1,2,3,6,9]
print(len(basket),"--> we can use in built functions as well")
print("\nList Methods")
#adding values
basket.append(18) #--> adds 18 to the last of the list
print(basket,"\nadded 18 in the end of the list")
basket.insert(3,"hello world") #--> adds to a specefic position i.e, insert(index,value)
print(basket,"\nadded hello world at 3rd index")
basket.extend([1000,"shubham ojha"]) #--> helps to add a list to the existing list
print(basket,"\nafter adding the elements using external list additon")

#removing values
basket.pop() #--> removes the last element from the list and this is not implace
print(basket,"\nremoved last element")
basket.pop(3) #removes the specefic index from the list
print(basket,"\nremoved 3rd element")
basket.remove(1000) #--> removes the specefic value from the list
print(basket, "\nremoved 1000 from the list")
basket.clear() #--> clears the entire list , i.e, no elements in the list 
print(basket,"\ncleared the list")

a,b,c, *remainingelements ,d = [1,2,3,4,5,6]
print(a)
print(remainingelements)
print(d)
