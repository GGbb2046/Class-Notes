import json

somedata = [{'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4),
            'b': 3.0, 'c': {'x': 12, 'y': 100}}]

data_string = json.dumps(somedata) # translate this data structure into a json string
print('ENCODED:', data_string) # json encoded (serialized) string representation

decoded = json.loads(data_string) # reverse the process by de-serializing the data.
print('DECODED:', decoded)

# now, let's compare the results of the pre-encoded data, and the end result of the unencoded (deserialized data)
print('ORIGINAL:', somedata)
print('ORIGINAL:', type(somedata))
print('DECODED :', decoded)
print('DECODED :', type(decoded))
print('ORIGINAL:', somedata[0]['fname'])
print('ORIGINAL:', type(somedata[0]['fname']))
print('DECODED :', decoded[0]['fname'])
print('DECODED :', type(decoded[0]['fname']))
print('ORIGINAL:', somedata[0]['occupation'])
print('ORIGINAL:', type(somedata[0]['occupation']))
print('DECODED :', decoded[0]['occupation'])
print('DECODED :', type(decoded[0]['occupation']))
print('ORIGINAL:', somedata[0]['a'])
print('ORIGINAL:', type(somedata[0]['a']))
print('DECODED :', decoded[0]['a']) # notice how tuple became a list!
print('DECODED :', type(decoded[0]['a'])) # notice how tuple became a list!
print('ORIGINAL:', somedata[0]['b'])
print('ORIGINAL:', type(somedata[0]['b']))
print('DECODED :', decoded[0]['b'])
print('DECODED :', type(decoded[0]['b']))
print('ORIGINAL:', somedata[0]['c'])
print('ORIGINAL:', type(somedata[0]['c']))
print('DECODED :', decoded[0]['c'])
print('DECODED :', type(decoded[0]['c']))