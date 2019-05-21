print("\n==========Hello from mymod_2a==========")

mymod_1b_str = "This string is local to mymod_1b_str"

def mymod_2a_fun():
    test_str="string local to mymod_2a_fun"
    print("==========Hello from mymod_2a_fun==========")
    print(dir())

print(dir())

print("\n==========End import of mymod_2a==========\n\n")