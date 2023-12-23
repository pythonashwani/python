# str = "They said, "Hello what's going on?"
# SyntaxError: invalid syntax
# print(str)
# using triple quotes
print('''''They said, "What's there?"''')
# escaping single quotes
print('They said, "What\'s going on?"')
# escaping double quotes
print("They said, \"What's going on?\"")


# Using Curly braces
print("{} and {} both are the best friend".format("python", "Devops"))
# Positional Argument
print("{1} and {0} best players ".format("Virat", "Rohit"))
# Keyword Argument
print("{a},{b},{c}".format(a="James",  c="Ricky",b="Peter"))

Integer = 10
Float = 1.290
String = "Python"
print("""Hi I am Integer ... My value is %d\n
Hi I am float ... My value is %f\n
Hi I am string ... My value is %s""" %(Integer, Float, String))

name="sars_cov_2"
disease="covid19"
print("The name of virus is {} and it causes {}".format(name,disease))
print(f"The name of virus is {name} and it causes {disease}")
# Concatenation
print("The name of virus is" + " " + name)