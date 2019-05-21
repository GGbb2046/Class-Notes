astring = "Hello World"

print("0:  " + str(len(astring)))
print("1:  " + astring[1:11]) # from from index 0 up-to but not including index 11
print("2:  " + astring[1:])  # If you're copying to the end of a string, you can leave out the last index
print("3:  " + astring[:3]) # from start of string
print("4:  " + astring[:]) # copy of the entire string
print("5:  " + astring[::2]) # every second character of the string
print("6:  " + astring[1:8:2]) # every second character from index 1 up to but not including index 8
print("7:  " + astring[::-1]) # reversed string
print("8:  " + astring[-1]) # the last character of the string
print("9:  " + astring[-2]) # the second last character of the string
print("10: " + astring[1:-1]) # the string with the first and last character dropped. 
print("11: " + astring[-2:0:-1]) # the reverse of the string with the first and last character dropped.

alist = ["hello", "world"]
print(alist[0][0]) # select the first element of the list (the string) and then select the first character of that string
print(alist[1][0]) # select the second element of the list (the string) and then select the first character of that string
# print(alist[2][0]) # index out of bounds error, as there is not element in the list at index 2.
print(alist[1][::-1]) # the second element of the list, reversed

adict = {"first":"Hello", "second":"World"}
print(adict["first"][0]) # select the value at the key "first" (a string) and then select the first character of that string
print(adict["second"][0]) # select the value at the key "second"  and then select the first character of that string
# print(adict["third"][0]) # key error, there is no key called "third"
print(adict["second"][::-1]) # the second element of the list, reversed