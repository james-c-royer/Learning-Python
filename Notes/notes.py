# example of a module implementation:
import math

# import a module and use an alias for it
import math as m # import modName as modAlias

# import a specific function from a modue
from math import e # math library w/the "e" variable

# print(help("modules")) # gives a list of modules
# print(help("modules name")) # gives a list of vars/functions in a module

# if a specific var/func is implemented it can be called without a prefix

print(e) # can be used since it is specifically implented

print(math.pi) # needs "math" prefix because it is from the math module

import moduleExample as moduleExample # another file that was created and saved to be reused
# moduleExample is in the same folder as notes so that this import functions

cubed_number = moduleExample.cube(4)
print(cubed_number)