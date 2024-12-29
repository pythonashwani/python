# Python program to show how to use else clause with try and except clauses  

# Defining a function which returns divide of a number  
def divide( num ):  
    try:  
        res = 100 / num  
    except ZeroDivisionError:  
        print( "We cannot divide by zero" )  
    else:  
        print ( res )  
# Calling the function and passing values  
divide(4)  
divide(0)  
print("end of the code")