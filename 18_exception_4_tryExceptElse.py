# Python program to show how to use else clause with try and except clauses  

# Defining a function which returns reciprocal of a number  
def reciprocal( num1 ):  
    try:  
        reci = 1 / num1  
    except ZeroDivisionError:  
        print( "We cannot divide by zero" )  
    else:  
        print ( reci )  
# Calling the function and passing values  
reciprocal( 4 )  
reciprocal( 0 )  
print("end of the code")