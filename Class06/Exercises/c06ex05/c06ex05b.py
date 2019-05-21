import shelve


with shelve.open("output.shelf", "c") as shelf_in:
    data = list(shelf_in.values())
    
print(data) # originally data = [ (1, 2, 3), {1:"un", 2:"deux"}]
