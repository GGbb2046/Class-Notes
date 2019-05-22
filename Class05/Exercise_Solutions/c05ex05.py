"""
Author:         Tim Smith
Description:    Solution to Class04 Ex3
"""

cubes = [x**3 for x in range(100)]  # see class notes. This is a simple list comprehension

# here is the simple way
counter = 0
for i in cubes:  # i will take on the value of each of the items found in cubes
    print(i, end='')  # print this i
    if counter < len(cubes)-1:
        print("-", end='')  # as long as I'm not on the last cube value, then print the dash
    counter += 1  # count is being used to keep track of the number of cubes we've processed



print() # this just prints a blank line - used to separate the two outputs.

# here is a more advanced "pythonic" approach (we didn't cover enumerate, so this is just for those who are looking to
# know more advanced techniques in python
for counter, i in enumerate(cubes):
    print(i, end='')  # print this i
    if counter < len(cubes)-1:
        print("-", end='')  # as long as I'm not on the last cube value, then print the dash
