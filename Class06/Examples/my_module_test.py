# Import our module
import my_module # A module is "compiled" (run) when it is first loaded, therefore we will see the results from the print

# verify that the module is loaded, and works as expected
print(my_module.var1, my_module.var2, my_module.fun1(), sep="\n")


# note that in my_module we have a docstring for the module (found at the top of the file), and a docstring for the
# function (found at the start of the function code)
print(help(my_module)) # displays information found in the docstring of the module, along with other summary information
print(help(my_module.fun1))

# now, we can also change a value found in a module
my_module.var1 = 20
my_module.var2 = "another string"

# and to verify that change has been made, we can do the following
print(my_module.var1, my_module.var2, my_module.fun1(), sep="\n")

# we can import a module more than once, but the module is only processed the first time it is loaded. After
# the first import, any other imports will be ignore.

import my_module # the second time a module is imported, Python will not run it again, as it's already in memory

# so, we can see that the second import didn't "reset" any of the values for var1 and var2
print(my_module.var1, my_module.var2, my_module.fun1(), sep="\n")



print(help(my_module.fun1))
