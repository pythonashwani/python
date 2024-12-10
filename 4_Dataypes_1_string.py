str = "HELLO"  # immutable (can't be changebale)
print(str[2])  # L
print(str[2:5])  # LLO
#str[0] = "h"  # TypeError: 'str' object does not support item assignment
print(str)
str1 = "Python"
print(str1)
del str1
print(str1) # NameError: name 'str1' is not defined. Did you mean: 'str'?