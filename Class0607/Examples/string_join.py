# here is a step by step version
cubes = [x**3 for x in range(100)] # create a list of the cubes of each of the numbers from o to 99
cubes_as_strs = [str(x) for x in cubes] # cast each element in the cubes list to a string type
seperator = "-" # create a string with the separator characters
outstr = seperator.join(cubes_as_strs) # join the strings found in cubes_as_strs using the seperator 
print(outstr)

# here is the above but written in one line
print("-".join([str(x**3) for x in range(100)]))