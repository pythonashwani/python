# access module
import my_module_math

print(my_module_math.square(2))
print(my_module_math.pi)

# access module using alias
import my_module_math as mt

print(mt.square(2))
print(mt.pi)

# access module only specific function and directly access it
from my_module_math import pi, square

print(pi)

# access module and all function and directly access it
from my_module_math import *

print(square(2))
print(pi)

print(dir(my_module_math))

print("my_module_math.__file__ attribute:", my_module_math.__file__)
print("my_module_math.__doc__ attribute:", my_module_math.__doc__)
print("my_module_math.__name__ attribute:", my_module_math.__name__)
print("__file__ attribute:", __file__)
print("__doc__ attribute:", __doc__)
print("__name__ attribute:", __name__)
