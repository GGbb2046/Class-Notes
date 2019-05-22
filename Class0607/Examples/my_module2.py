"""This is the docstring associated with mymodule.


If I call help(mymodule) the docstring found at the beginning of the file is
displayed. Convention is to include a brief description of the module in the
docstring.

This module contains two variables (var1 and var2), one function (fun1), and
one line of code (a print statement) that will be run as soon as the module
is first imported.
"""

var1 = 10
var2 = "Some string"


def fun1():
    """This is a docstring that describes fun1()."""
    return("Hello from fun1")

if __name__ == "__main__":
    print("You called me directly. Therefore, my __name__ variable is set to __main__")
else:
    print("You imported me. My name, therefore, is " + __name__)
