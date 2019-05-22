"""
Author:         Tim Smith
Description:    Sample Web API - NYT Best Seller List. This program will return the current #1 best selling EBook Fiction
"""
import json
with open("nyt.json", "r") as fin:
    data = json.load(fin)

print("{:<14}{}".format("TITLE:", data['results'][0]['book_details'][0]['title']))
print("{:<14}{}".format("DESCRIPTION:", data['results'][0]['book_details'][0]['description']))
print("{:<14}{}".format("AUTHOR:",data['results'][0]['book_details'][0]['author']))
print("{:<14}{}".format("ISBN:", data['results'][0]['book_details'][0]['primary_isbn13']))




