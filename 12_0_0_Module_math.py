# access module
import math
print(math.pi)
print(math.sqrt(16))
print(math.pow(2, 3))
print(math.floor(3.9))
print('*' * 50)
# access module using alias
import math as mt
print(mt.pi)
print(mt.sqrt(16))
print('#' * 50)
# access module only specific function and directly access it
from math import pi, sqrt
print(pi)
print(sqrt(16))
print('@' * 50)
# access module and all function and directly access it
from math import *
print(pi)
print(sqrt(16))
print(pow(2, 3))
print(floor(3.9))
print('^' * 50)
print(dir(math))

print("math.__file__ attribute:", math.__file__)
print("math.__doc__ attribute:", math.__doc__)
print("math.__name__ attribute:", math.__name__)
print("__file__ attribute:", __file__)
print("__doc__ attribute:", __doc__)
print("__name__ attribute:", __name__)

