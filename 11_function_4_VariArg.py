# Python code to demonstrate the use of variable-length arguments       
# Defining a function    
def function( *args_list ):    
    ans = []    
    for l in args_list:    
        ans.append( l.upper() )    
    return ans    
# Passing args arguments    
result = function('Python', 'Functions', 'tutorial')    
print( result )    

# defining a function    
def function( **kargs_list ):    
    ans = []
    print(kargs_list['Third']) #Arbitrary
    for key, value in kargs_list.items():    
        ans.append([key, value])    
    return ans    
# Paasing kwargs arguments    
result = function(First = "Python", Second = "Functions", Third = "Tutorial")    
print(result)    