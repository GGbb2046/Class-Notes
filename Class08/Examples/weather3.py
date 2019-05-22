import requests
import json
api_key = "34074bd64c6a43eb8ed19a04dbf0d216" # this is the professors appid, please use your own
base_url = 'http://api.openweathermap.org/data/2.5/weather?'
full_url = base_url +  "&q=Tampa" + '&APPID=' + api_key 
print("Here is the full URL being used for the WebAPI call", full_url)
f = requests.get(full_url)
json_string = f.text
if len(json_string) < 1:
    print("The API is currently unavailable. Please try again in a few minutes. ")
else: 
    parsed_json = json.loads(json_string)
    temp_k = parsed_json['main']['temp'] 
    temp_f = (9/5) * (temp_k - 273.15) + 32 
    print("Current temperature in fahrenheit is {:.2f}".format(temp_f))