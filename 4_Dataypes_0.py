x = 0b10100 #Binary Literals  
y = 100 #Decimal Literal   
z = 0o215 #Octal Literal  
u = 0x12d #Hexadecimal Literal  

#Float Literal  
float_1 = 100.5   
float_2 = 1.5e2

#Complex Literal   
a = 5+3.14j

print(x, y, z, u)  
print(float_1, float_2)  
print(a, a.imag, a.real)  
print('---------')
# String's
str1 = "\u0061lpha"
str2 = 3* 'beta'
str3 = '''gamma string'''
str4 = """delta string"""
print(str1, str2, str3, str4)
# Numbers
num1 = 123
flt1 = 2.0

# List / Collection of multi datatype, enclosed in square brackets.
first_list = [str1, "DevOps", 47, num1, 1.5]

# Printing a List
print(first_list)

# Tuple/ Collection of multi datatype, enclosed in round bracket
first_tuple = (str1, "DevOps", 47, num1, 1.5)

# Printing a tuple
print(first_tuple)

# Dictionary/ Elements in the dictionary are always in pairs(Key:Value), curly brackets.
first_dictionary = {"Name":"Imran", "Weight":75, "Exercises":["Boxing", "Dancing", "Jogging"]}

# Printing a Dictionary
print(first_dictionary)

print("Variable first_list is a:", type(first_list))
print("Variable first_tuple is a:", type(first_tuple))
print("Variable first_dictionary is a:", type(first_dictionary))

# Boolean
x = True
y = False

# Printing Boolean
print(x)
print(y)

print("x is a ", type(x))
print("y is a ", type(y))