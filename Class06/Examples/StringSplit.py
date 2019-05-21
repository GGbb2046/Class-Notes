"""
Author:         Tim Smith
Description:    Class05 Example to demonstrate string split
"""

astring = "This is a string"
bstring = "This is another string"

words = astring.split(' ')
print(words)

words = words + bstring.split(' ')
print(words)

# There is a fourth composite type called a set. Set is like a list, only that each element of a set will be unique.
# If you add a new value that already exists in the set, this addition will be ignored. This comes in handle, for
# instance, if we want to find the unique values in a list.
print(set(words))