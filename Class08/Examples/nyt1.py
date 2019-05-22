
import requests
import json
f = requests.get("https://api.nytimes.com/svc/books/v3/lists.json?list=e-book-fiction&api-key=u72bmRKWaAo0Q7pdI3P0kBOictfmJGxI")
json_string = f.text
with open("nyt.json", "w") as fout:
    fout.write(json_string)




