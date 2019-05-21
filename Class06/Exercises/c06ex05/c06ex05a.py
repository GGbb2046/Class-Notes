import shelve

data = [ (1, 2, 3), {1:"un", 2:"deux"}]

with shelve.open("output.shelf", "c") as shelf_out:
    shelf_out["data"] = data