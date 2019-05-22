import json

data = [ (1, 2, 3), {1:"un", 2:"deux"}]

with open("output.json", "w") as fout:
    json.dump(data, fout)
