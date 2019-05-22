astring = "Hello"
astring.upper()
print(astring) # note that astring is not all upper 
if astring.upper == "HELLO":
    print("The astring contains upper or lower letters in HELLO")
    print(astring)
astring = astring.upper()
print(astring)
print("world".upper()) # note that even literals have methods - "world" is a string, therefore, it has all the string methods
