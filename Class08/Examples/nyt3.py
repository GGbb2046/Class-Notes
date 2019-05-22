"""
Author:         Tim Smith
Description:    Sample Web API - NYT Best Seller List. This program will return the current #1 best selling EBook Fiction
"""
import requests
import json
f = requests.get("https://api.nytimes.com/svc/books/v3/lists.json?list=e-book-fiction&api-key=u72bmRKWaAo0Q7pdI3P0kBOictfmJGxI")
json_string = f.text
data = json.loads(json_string)

print("{:<14}{}".format("TITLE:", data['results'][0]['book_details'][0]['title']))
print("{:<14}{}".format("DESCRIPTION:", data['results'][0]['book_details'][0]['description']))
print("{:<14}{}".format("AUTHOR:",data['results'][0]['book_details'][0]['author']))
print("{:<14}{}".format("ISBN:", data['results'][0]['book_details'][0]['primary_isbn13']))




