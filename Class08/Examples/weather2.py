import json

with open("weather.json", "r") as fin:
    data = json.load(fin)

temp_k = data['main']['temp']
temp_f = (9/5)*(temp_k - 273) + 32

print("The current temperator is {:.2f}.".format(temp_f))
