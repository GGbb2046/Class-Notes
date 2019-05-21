"""
Author:         Tim Smith
Description:    Example to illustrate enumerate
"""

numbers = [x**3 for x in range(10)]

count = 0
for i in numbers:
    print(i, end='')
    if count < len(numbers)-1:
        print('-', end='')
    count += 1

print() # print a blank line to separate lines
# here is the same thing done with enumerate
for count, i in enumerate(numbers):
    print(i, end='')
    if count < len(numbers) - 1:
        print('-', end='')
