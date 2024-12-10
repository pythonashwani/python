str = "Hello"
str1 = " world"
print(str*3)  # HelloHelloHello
print(str+str1)  # Hello world
print(str[4])  # o
print(str[2:4])  # ll
print('w' in str)  # false as w is not present in str
print('wo' not in str1)  # false as wo is present in str1.
print("C:\\python37")  # C://python37 as it is written
print(r"C:\\python37")  # C://python37 as it is written
print("%s string str : %s" % (str,"welcome"))  # prints Hello string str : welcome