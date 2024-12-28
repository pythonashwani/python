def greet(name):
    return f"Hello, {name}!"


message = greet("Guest")
print(message)


# add function
def add(a, b):
    print(f"a= {a} b={b}")
    return a + b


result = add(2, 3)
print('result: ', result)


# Square function
def square(num):
    """  
    This function computes the square of the number.  
    """
    return num ** 2


result = square(6)
print("The square of the given number is: ", result)
