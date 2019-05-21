x = 1/3 # this will produce a float with a long series of decimal places
print(x) # this will display a long series of decimals
print("{:.2f}".format(x)) # this will display only the first two decimals
x *= 2 # this will produce a float with a long string of 6's in the decimal
print(x)
print("{:.2f}".format(x)) # this will display only the first two -- note that it rounds
print("{:.2f}".format(int(x*100)/100)) # python does not have a truncate function, but you can do a little math to accomplish truncation

