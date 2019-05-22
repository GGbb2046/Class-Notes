import requests
import json
api_key = "34074bd64c6a43eb8ed19a04dbf0d216" # this is the professors appid, please use your own
base_url = 'http://api.openweathermap.org/data/2.5/weather?'
full_url = base_url +  "&q=Tampa" + '&APPID=' + api_key 
print(full_url)
f = requests.get(full_url)
json_string = f.text
if len(json_string) < 1:
    print("The API is currently unavailable. Please try again in a few minutes. ")
else: 
    try:
        fout = open("weather.json", 'w')
        fout.write(json_string)
        fout.close()
    except IOError:
        print("ERROR: Error opening weather.json for writing. Please correct the problem and try again")
