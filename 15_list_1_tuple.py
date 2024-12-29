# Python program to show how to create a tuple    
tuple = (1, 2, 3, 4, 5, 6)
print(tuple[0])
print(tuple[1])
print(tuple)
print(type(tuple))

# updating tuple values  : not possible
#tuple[1] = 100 # TypeError: 'tuple' object does not support item assignment
print(tuple)

# Creating an empty tuple    
empty_tuple = ()    
print("Empty tuple: ", empty_tuple)    
# Creating tuple having integers    
int_tuple = (4, 6, 8, 10, 12, 14)    
print("Tuple with integers: ", int_tuple)    
    
# Creating a tuple having objects of different data types    
mixed_tuple = (4, "Python", 9.3)    
print("Tuple with different data types: ", mixed_tuple)    
    
# Creating a nested tuple    
nested_tuple = ("Python", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6))    
print("A nested tuple: ", nested_tuple)    

# Python program to show how to create a tuple having a single element    
single_tuple = ("Tuple")    
print( type(single_tuple) )     
# Creating a tuple that has only one element    
single_tuple = ("Tuple",)    
print( type(single_tuple) )     
# Creating tuple without parentheses    
single_tuple = "Tuple",    
print( type(single_tuple) )    
