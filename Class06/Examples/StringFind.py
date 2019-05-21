"""
Author:         Tim Smith
Description:    Example for Class05 - demonstrates string find method
"""

astring = "This sentence has repetition, repetition, and more repetition."

print(astring.find("sentence"))    # this returns the index to the start of the word found

print(astring.find("repetition"))     # find the first occurrence (index 18)

print(astring.find("repetition", 19))  # to find any other occurrences, I need to start the search after the first one found

print(astring.find("xray")) # returns -1 if the string was not found