# Creating a set which have immutable elements  
set1 = {1,2,3, "python", 20.5, 14}  
print(type(set1))  
#Creating a set which have mutable element  
#set2 = {1,2,3,["python",4]}   # error TypeError: unhashable type: 'list'
#print(type(set2))  

# Empty curly braces will create dictionary
set3 = {}
print(type(set3)) # <class 'dict'>

# Empty set using set() function
set4 = set()
print(type(set4)) # <class 'set'>

set5 = {1,2,4,4,5,8,9,9,10}  
print("Return set with unique elements:",set5)
# Return set with unique elements: {1, 2, 4, 5, 8, 9, 10}