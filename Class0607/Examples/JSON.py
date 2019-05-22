import json

# Translate a python data structure to a JSON encoded string
somedata = [{'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4), 'b': 3.0}]
data_string = json.dumps(somedata,sort_keys=True,indent=4) # sort_keys and indent are optional. Good for display to screen
print('JSON:', data_string)

with open('data01.json','w') as outfile:
    outfile.write(data_string)

with open('data01.json','r') as infile:
  data = json.loads(infile.read())

print("The type of the loaded data is ", type(data))