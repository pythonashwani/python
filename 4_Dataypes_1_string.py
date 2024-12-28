str = "HELLO"  # immutable (can't be changebale)
# H E L L O
# 0 1 2 3 4
print(str) # HELLO
print(str[2])  # L
print(str[2:5])  # LLO
print(str[0:4])  # HELL
#str[0] = "h"  # TypeError: 'str' object does not support item assignment
print(str)
str1 = "Python"
print(str1)
del str1
print(str1) # NameError: name 'str1' is not defined. Did you mean: 'str'?
print(a) # NameError: name 'a' is not defined