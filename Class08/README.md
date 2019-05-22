[TOC levels=1,2,3 numbered]: # "Class08"

# Class08
- [Class08](#class08)
- [Objectives](#objectives)
- [Practice exercises](#practice-exercises)
  - [c08ex01 - Write text to a file](#c08ex01---write-text-to-a-file)
  - [c08ex02 - Read text from a file](#c08ex02---read-text-from-a-file)
  - [c08ex03 - Save a data structure as a JSON file to be read later](#c08ex03---save-a-data-structure-as-a-json-file-to-be-read-later)
  - [c08ex04 - Recreate a data structure saved as a JSON file](#c08ex04---recreate-a-data-structure-saved-as-a-json-file)
- [Online (Web) API's (examples: weather, NYT best sellers list)](#online-web-apis-examples-weather-nyt-best-sellers-list)
  - [Case1: Open Weather Map](#case1-open-weather-map)
  - [Case2: NYT Best Seller List](#case2-nyt-best-seller-list)

# Objectives

* Exercises to reinforce material from last class
  * Write text to a file
  * Read text from a file
  * Save a data structure as a JSON file to be read later.
  * Recreate a data structure saved as a JSON file. 
  * Review Assignment05
* How to call / use Web API's (and revisit of JSON)

# Practice exercises

## c08ex01 - Write text to a file

Write a command line program that accepts a filename argument (only one argument, no more no less) and writes the phrase "Hello World" to the given filename. 


## c08ex02 - Read text from a file

Write a command line program that accepts a filename argument (only one argument, no more no less) and reads and displays the contents of this file to the screen.

## c08ex03 - Save a data structure as a JSON file to be read later

Write a command line program that accepts a filename argument (only one argument, no more no less). Inside this program, you'll create a data structure that is a list containing two elements; a list of numbers from 1 to 5, and a dictionary within which there are two elements; the first has a key of "fname" and a value that is your first name, the second has a key of "lname", and has a value that is your last name. The program should write this data structure as json data (serialize the data structure) into the filename given by the command line argument. 

## c08ex04 - Recreate a data structure saved as a JSON file

Write a command line program that accepts a filename argument (only one argument, no more no less). This program will read the given file as a json file, and attempt to create an in memory data structure from this data (de-serialize the data).


# Online (Web) API's (examples: weather, NYT best sellers list)

There are many Web API's (application programming interface) available on the internet (see github page here https://github.com/toddmotto/public-apis_). These API's are services that programs you write can access. 

Many of these Web API's respond with JSON data. JSON data is essentially textual data, but with internal structure (like CSV, but more expansive in it's application). As we have previously, JSON can be used for persistent storage of a programs data structures -- as they can be saved to disk using JSON, and later recreated from the saved file. JSON is also used to communicate information between programs. In the case of Web API's, there are "always on" programs that are available to respond to your programs request for information.

NOTE: There are two general forms of access to a web site -- the first is called a "get" request, and second is called a "post" request. We will be covering the "get" request approach.

## Case1: Open Weather Map
Open Weather Map (https://openweathermap.org/price) provides a weather API (they provide a few of these API's, we're interested in https://openweathermap.org/current). You need to sign up to get a token, and then use this token to access their API.

NOTE: Make sure that VSCode has the proper Python interpreter selected. CMD-SHIFT-P will bring up a command dialog, start typing 'python select interpreter' (without the quotes), then select the command Python: Select Interpreter from this list. Then you may need to select the repo to which to apply this (this may be specific to MacOS, and you may not see this). Finally, select the anaconda 64 bit interpreter in the list (you may only have one to select from, but on a mac you will have a few options)

ALERT: To run the following program you will first need to install the "requests" module. All the modules we've used thus far (i.e. math, turtle, json, and shelf) are included in the python standard distribution. Other modules need to be installed. Anaconda has a built-in package manager called "conda". To install the requests package, at your command prompt type in "conda install requests" - and follow the instructions to install.  The requests package provides "HTTP" request functions to assist development of programs that connect to remove servers using the HTTP protocol. We will user the requests package to connect to Web APIs (for more information on the requests package, see [here](https://realpython.com/python-requests/))



```python
import requests
import json
api_key = "34074bd64c6a43eb8ed19a04dbf0d216" # this is the professors appid, please use/create your own
base_url = 'http://api.openweathermap.org/data/2.5/weather?'
full_url = base_url +  "&q=Tampa" + '&APPID=' + api_key 
print(full_url)
f = requests.get(full_url)
json_string = f.text
if len(json_string) < 1:
    print("The API is currently unavailable. Please try again in a few minutes. ")
else: 
    fout = open("weather.json", 'w')
    fout.write(json_string)
    fout.close()
```
[The above python file can be found here](./Examples/weather1.py)

Like many web api's, the Open Weather Map API returns a JSON file, the above program saves this file and you can open this using VSCode 

NOTE: If you look at the output from weather1.py, it may show all on one line. If so, this makes it rather difficult to "see" the structure of the file. I'd recommend installing the  "prettier" plugin, and then CTL-SHIFT-P and search for format document. This will "beatify" the JSON file and make it easier to read. 

You can view the contents of this JSON file using vscode. If you open the file, you'll see the the following:
```json
{"coord":{"lon":-82.46,"lat":27.95},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"base":"stations","main":{"temp":304.91,"pressure":1018,"humidity":55,"temp_min":302.04,"temp_max":307.59},"visibility":16093,"wind":{"speed":2.1,"deg":220},"clouds":{"all":40},"dt":1558547081,"sys":{"type":1,"id":6046,"message":0.011,"country":"US","sunrise":1558521425,"sunset":1558570572},"timezone":-14400,"id":4174757,"name":"Tampa","cod":200}
```

To make it easier to interpret this output, you can use VSCode's "format" command (CMD-OPTION-F on MacOS, or SHIFT-ALT-F on windows). Once you do this inside vscode (in the editor window with the json data), the json data will now look like the following:

```json
{
  "coord": { "lon": -82.46, "lat": 27.95 },
  "weather": [
    {
      "id": 502,
      "main": "Rain",
      "description": "heavy intensity rain",
      "icon": "10n"
    },
    {
      "id": 211,
      "main": "Thunderstorm",
      "description": "thunderstorm",
      "icon": "11n"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 297.77,
    "pressure": 1013,
    "humidity": 94,
    "temp_min": 294.15,
    "temp_max": 300.37
  },
  "visibility": 6437,
  "wind": { "speed": 2.1, "deg": 300 },
  "rain": { "1h": 7.87 },
  "clouds": { "all": 90 },
  "dt": 1555289046,
  "sys": {
    "type": 1,
    "id": 3654,
    "message": 0.0079,
    "country": "US",
    "sunrise": 1555239958,
    "sunset": 1555286033
  },
  "id": 4174757,
  "name": "Tampa",
  "cod": 200
}
```

Now, we can load this JSON file into memory using the json.loads method. The result will be an in memory data structure created based on this json data. Once this is done, you can access any of the data found within the response. 

```python
import json

with open("weather.json", "r") as fin:
    data = json.load(fin)

temp_k = data['main']['temp']
temp_f = (9/5)*(temp_k - 273) + 32

print("The current temperature is {:.2f}.".format(temp_f))
```
[The above python file can be found here](./Examples/weather2.py)


Now, let's simply read and display the temperature directly from the Web API (rather than saving it to a file)

```python
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
```
[The above python file can be found here](./Examples/weather3.py)



## Case2: NYT Best Seller List

http://developer.nytimes.com/


This snippet of code will display the #1 best selling EBook NonFiction. It will display the book title, description, author and ISBN (13) number.

```python
import requests
import json
f = requests.get("https://api.nytimes.com/svc/books/v3/lists.json?list=e-book-fiction&api-key=u72bmRKWaAo0Q7pdI3P0kBOictfmJGxI")
json_string = f.text
with open("nyt.json", "w") as fout:
    fout.write(json_string)
```
[The above python file can be found here](./Examples/nyt1.py)


The above code simply saves the returns json data to a local file. You can open this file in JSON, and to make the formatting "prettier", select CMD-ALT-K (on windows) or CMD-OPT-K on MacOS. 

Here is an example JSON output from the NYTimes Best Seller API:

```json
{
  "status": "OK",
  "copyright": "Copyright (c) 2019 The New York Times Company.  All Rights Reserved.",
  "num_results": 15,
  "last_modified": "2017-03-21T13:38:01-04:00",
  "results": [
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 1,
      "rank_last_week": 0,
      "weeks_on_list": 1,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "https://www.amazon.com/Full-Package-Lauren-Blakely-ebook/dp/B01MT5HMRV?tag=NYTBS-20",
      "isbns": [],
      "book_details": [
        {
          "title": "FULL PACKAGE",
          "description": "A man shares a cramped apartment with his friend's fetching sister.",
          "contributor": "by Lauren Blakely",
          "author": "Lauren Blakely",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Lauren Blakely",
          "primary_isbn13": "A00B01MT5HMRV",
          "primary_isbn10": "None"
        }
      ],
      "reviews": [
        {
          "book_review_link": "",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    },
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 2,
      "rank_last_week": 0,
      "weeks_on_list": 2,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "http://www.amazon.com/Guernsey-Literary-Potato-Peel-Society/dp/0385340990?tag=NYTBS-20",
      "isbns": [
        { "isbn10": "0385341008", "isbn13": "9780385341004" },
        { "isbn10": "0440337976", "isbn13": "9780440337973" },
        { "isbn10": "1984801813", "isbn13": "9781984801814" }
      ],
      "book_details": [
        {
          "title": "THE GUERNSEY LITERARY AND POTATO PEEL PIE SOCIETY",
          "description": "After World War II, a journalist travels to the island of Guernsey to meet residents who resisted the Nazi occupation. Originally published in 2008.",
          "contributor": "by Mary Ann Shaffer and Annie Barrows",
          "author": "Mary Ann Shaffer and Annie Barrows",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Dial",
          "primary_isbn13": "9780440337973",
          "primary_isbn10": "0440337976"
        }
      ],
      "reviews": [
        {
          "book_review_link": "",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    },
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 3,
      "rank_last_week": 4,
      "weeks_on_list": 12,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "https://www.amazon.com/Whistler-John-Grisham-ebook/dp/B01C1LUFFK?tag=NYTBS-20",
      "isbns": [
        { "isbn10": "0385541198", "isbn13": "9780385541190" },
        { "isbn10": "0385541201", "isbn13": "9780385541206" },
        { "isbn10": "0385541570", "isbn13": "9780385541572" },
        { "isbn10": "1101967676", "isbn13": "9781101967676" },
        { "isbn10": "1101967684", "isbn13": "9781101967683" }
      ],
      "book_details": [
        {
          "title": "THE WHISTLER",
          "description": "A whistleblower alerts a Florida investigator to judicial corruption involving the Mob and Indian casinos.",
          "contributor": "by John Grisham",
          "author": "John Grisham",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Doubleday",
          "primary_isbn13": "9780385541206",
          "primary_isbn10": "0385541201"
        }
      ],
      "reviews": [
        {
          "book_review_link": "https://www.nytimes.com/2016/11/06/books/review/john-grisham-whistler.html",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    },
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 4,
      "rank_last_week": 0,
      "weeks_on_list": 1,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "https://www.amazon.com/Ring-Fire-Pike-Logan-Thriller/dp/1101984767?tag=NYTBS-20",
      "isbns": [{ "isbn10": "1101984767", "isbn13": "9781101984765" }],
      "book_details": [
        {
          "title": "RING OF FIRE",
          "description": "Pike Logan, a member of a secret counterterrorist unit called the Taskforce, investigates a Saudi-backed Moroccan terrorist cell.",
          "contributor": "by Brad Taylor",
          "author": "Brad Taylor",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Dutton",
          "primary_isbn13": "9781101984772",
          "primary_isbn10": "None"
        }
      ],
      "reviews": [
        {
          "book_review_link": "",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    },
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 5,
      "rank_last_week": 7,
      "weeks_on_list": 9,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "http://www.amazon.com/Small-Great-Things-Jodi-Picoult-ebook/dp/B01AQNYZ3I?tag=NYTBS-20",
      "isbns": [
        { "isbn10": "0345544951", "isbn13": "9780345544957" },
        { "isbn10": "034554496X", "isbn13": "9780345544964" },
        { "isbn10": "1410463745", "isbn13": "9781410463746" },
        { "isbn10": "0425286010", "isbn13": "9780425286012" },
        { "isbn10": "0345544978", "isbn13": "9780345544971" }
      ],
      "book_details": [
        {
          "title": "SMALL GREAT THINGS",
          "description": "A medical crisis entangles a black nurse, a white supremacist father and a white lawyer.",
          "contributor": "by Jodi Picoult",
          "author": "Jodi Picoult",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Ballantine",
          "primary_isbn13": "9780345544964",
          "primary_isbn10": "034554496X"
        }
      ],
      "reviews": [
        {
          "book_review_link": "https://www.nytimes.com/2016/10/16/books/review/jodi-picoult-small-great-things-roxane-gay.html",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    },
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 6,
      "rank_last_week": 0,
      "weeks_on_list": 1,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "https://www.amazon.com/Shelter-Adeline-Badge-Honor-Heroes-ebook/dp/B01MF62CN8?tag=NYTBS-20",
      "isbns": [],
      "book_details": [
        {
          "title": "SHELTER FOR ADELINE",
          "description": "A fireman must keep his overprotective nature in check while pursuing an epileptic prey to her suspiciously obsessive boss.",
          "contributor": "by Susan Stoker",
          "author": "Susan Stoker",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Stoker Aces Production",
          "primary_isbn13": "A00B01MF62CN8",
          "primary_isbn10": "None"
        }
      ],
      "reviews": [
        {
          "book_review_link": "",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    },
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 7,
      "rank_last_week": 9,
      "weeks_on_list": 3,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "http://www.amazon.com/Man-Called-Ove-Novel/dp/1476738025?tag=NYTBS-20",
      "isbns": [
        { "isbn10": "1476738025", "isbn13": "9781476738024" },
        { "isbn10": "1476738017", "isbn13": "9781476738017" },
        { "isbn10": "1594139830", "isbn13": "9781594139833" },
        { "isbn10": "1410472922", "isbn13": "9781410472922" }
      ],
      "book_details": [
        {
          "title": "A MAN CALLED OVE",
          "description": "An angry old curmudgeon gets new neighbors, and things are about to change for all of them.",
          "contributor": "by Fredrik Backman",
          "author": "Fredrik Backman",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Atria",
          "primary_isbn13": "9781476738031",
          "primary_isbn10": "None"
        }
      ],
      "reviews": [
        {
          "book_review_link": "",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    },
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 8,
      "rank_last_week": 2,
      "weeks_on_list": 2,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "https://www.amazon.com/Mistress-Novel-Danielle-Steel-ebook/dp/B01E2GZ5FC?tag=NYTBS-20",
      "isbns": [
        { "isbn10": "0345531116", "isbn13": "9780345531117" },
        { "isbn10": "0425285359", "isbn13": "9780425285350" },
        { "isbn10": "0735210039", "isbn13": "9780735210035" }
      ],
      "book_details": [
        {
          "title": "THE MISTRESS",
          "description": "The beautiful mistress of a Russian oligarch falls in love with an artist and yearns for freedom.",
          "contributor": "by Danielle Steel",
          "author": "Danielle Steel",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Delacorte",
          "primary_isbn13": "9780425285350",
          "primary_isbn10": "0425285359"
        }
      ],
      "reviews": [
        {
          "book_review_link": "",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    },
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 9,
      "rank_last_week": 0,
      "weeks_on_list": 1,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "https://www.amazon.com/Guests-South-Battery-Tradd-Street/dp/0451475232?tag=NYTBS-20",
      "isbns": [{ "isbn10": "0451475232", "isbn13": "9780451475237" }],
      "book_details": [
        {
          "title": "THE GUESTS ON SOUTH BATTERY",
          "description": "Spirits invade the life of a Charleston realtor.",
          "contributor": "by Karen White",
          "author": "Karen White",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Berkley",
          "primary_isbn13": "9780698193000",
          "primary_isbn10": ""
        }
      ],
      "reviews": [
        {
          "book_review_link": "",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    },
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 10,
      "rank_last_week": 0,
      "weeks_on_list": 8,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "https://www.amazon.com/No-Mans-Land-John-Puller/dp/145558651X?tag=NYTBS-20",
      "isbns": [
        { "isbn10": "145558651X", "isbn13": "9781455586516" },
        { "isbn10": "1455541664", "isbn13": "9781455541669" },
        { "isbn10": "1455586498", "isbn13": "9781455586493" },
        { "isbn10": "1455586501", "isbn13": "9781455586509" }
      ],
      "book_details": [
        {
          "title": "NO MAN'S LAND",
          "description": "John Puller, a special agent with the Army, searches for the truth about his mother, who disappeared 30 years ago.",
          "contributor": "by David Baldacci",
          "author": "David Baldacci",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Grand Central",
          "primary_isbn13": "9781455586493",
          "primary_isbn10": "1455586498"
        }
      ],
      "reviews": [
        {
          "book_review_link": "",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    },
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 11,
      "rank_last_week": 0,
      "weeks_on_list": 0,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "https://www.amazon.com/Below-Belt-Stone-Barrington-Novel/dp/0399573976?tag=NYTBS-20",
      "isbns": [{ "isbn10": "0399573976", "isbn13": "9780399573972" }],
      "book_details": [
        {
          "title": "BELOW THE BELT",
          "description": "The New York lawyer Stone Barrington faces danger when he finds himself in possession of a retired C.I.A. agent\u2019s explosive memoir.",
          "contributor": "by Stuart Woods",
          "author": "Stuart Woods",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Putnam",
          "primary_isbn13": "9780399574184",
          "primary_isbn10": "None"
        }
      ],
      "reviews": [
        {
          "book_review_link": "",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    },
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 12,
      "rank_last_week": 0,
      "weeks_on_list": 0,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "https://www.amazon.com/Cross-Line-James-Patterson-ebook/dp/B01C37XEUU?tag=NYTBS-20",
      "isbns": [
        { "isbn10": "0316407097", "isbn13": "9780316407090" },
        { "isbn10": "031640716X", "isbn13": "9780316407168" },
        { "isbn10": "0316407151", "isbn13": "9780316407151" }
      ],
      "book_details": [
        {
          "title": "CROSS THE LINE",
          "description": "Detective Alex Cross and his wife, Bree, team up to catch a killer causing chaos in Washington, D.C.",
          "contributor": "by James Patterson",
          "author": "James Patterson",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Little, Brown",
          "primary_isbn13": "9780316407168",
          "primary_isbn10": "031640716X"
        }
      ],
      "reviews": [
        {
          "book_review_link": "",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    },
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 13,
      "rank_last_week": 0,
      "weeks_on_list": 0,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "https://www.amazon.com/Dry-Novel-Jane-Harper-ebook/dp/B01BSN15F6?tag=NYTBS-20",
      "isbns": [
        { "isbn10": "1250105609", "isbn13": "9781250105608" },
        { "isbn10": "1250105617", "isbn13": "9781250105615" }
      ],
      "book_details": [
        {
          "title": "THE DRY",
          "description": "",
          "contributor": "by Jane Harper",
          "author": "Jane Harper",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Flatiron",
          "primary_isbn13": "9781250105615",
          "primary_isbn10": "1250105617"
        }
      ],
      "reviews": [
        {
          "book_review_link": "",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    },
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 14,
      "rank_last_week": 0,
      "weeks_on_list": 0,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "https://www.amazon.com/Dogs-Purpose-Novel-Humans/dp/0765330342?tag=NYTBS-20",
      "isbns": [
        { "isbn10": "0765326264", "isbn13": "9780765326263" },
        { "isbn10": "0765330342", "isbn13": "9780765330345" },
        { "isbn10": "0765388111", "isbn13": "9780765388117" },
        { "isbn10": "0765388103", "isbn13": "9780765388100" },
        { "isbn10": "1429960272", "isbn13": "9781429960274" }
      ],
      "book_details": [
        {
          "title": "A DOG'S PURPOSE",
          "description": "A canine narrator undergoes a series of reincarnations.",
          "contributor": "by W. Bruce Cameron",
          "author": "W Bruce Cameron",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Forge",
          "primary_isbn13": "9781429960274",
          "primary_isbn10": "1429960272"
        }
      ],
      "reviews": [
        {
          "book_review_link": "",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    },
    {
      "list_name": "E-Book Fiction",
      "display_name": "E-Book Fiction",
      "bestsellers_date": "2017-01-14",
      "published_date": "2017-01-29",
      "rank": 15,
      "rank_last_week": 0,
      "weeks_on_list": 0,
      "asterisk": 0,
      "dagger": 0,
      "amazon_product_url": "https://www.amazon.com/Sleepwalker-Novel-Chris-Bohjalian-ebook/dp/B01FPGY5TK?tag=NYTBS-20",
      "isbns": [
        { "isbn10": "038553891X", "isbn13": "9780385538916" },
        { "isbn10": "0385538928", "isbn13": "9780385538923" }
      ],
      "book_details": [
        {
          "title": "THE SLEEPWALKER",
          "description": "The daughters of a Vermont woman who disappeared from her home in the middle of the night try to understand what happened.",
          "contributor": "by Chris Bohjalian",
          "author": "Chris Bohjalian",
          "contributor_note": "",
          "price": 0,
          "age_group": "",
          "publisher": "Doubleday",
          "primary_isbn13": "9780385538923",
          "primary_isbn10": "0385538928"
        }
      ],
      "reviews": [
        {
          "book_review_link": "",
          "first_chapter_link": "",
          "sunday_review_link": "",
          "article_chapter_link": ""
        }
      ]
    }
  ]
}
```


Now, let's extract the top book's title, description, author, and ISBN information. To do this, you'll need to figure out how to index into this data structure in order to get the correct data you're attempting to retrieve. 

```python
import json
with open("nyt.json", "r") as fin:
    data = json.load(fin)

print("{:<14}{}".format("TITLE:", data['results'][0]['book_details'][0]['title']))
print("{:<14}{}".format("DESCRIPTION:", data['results'][0]['book_details'][0]['description']))
print("{:<14}{}".format("AUTHOR:",data['results'][0]['book_details'][0]['author']))
print("{:<14}{}".format("ISBN:", data['results'][0]['book_details'][0]['primary_isbn13']))
```
[The above python file can be found here](./Examples/nyt2.py)


Finally, let's write a program that does this all once (get's the data from the server and displays the results)

```python
import requests
import json
f = requests.get("https://api.nytimes.com/svc/books/v3/lists.json?list=e-book-fiction&api-key=u72bmRKWaAo0Q7pdI3P0kBOictfmJGxI")
json_string = f.text
data = json.loads(json_string)

print("{:<14}{}".format("TITLE:", data['results'][0]['book_details'][0]['title']))
print("{:<14}{}".format("DESCRIPTION:", data['results'][0]['book_details'][0]['description']))
print("{:<14}{}".format("AUTHOR:",data['results'][0]['book_details'][0]['author']))
print("{:<14}{}".format("ISBN:", data['results'][0]['book_details'][0]['primary_isbn13']))
```
[The above python file can be found here](./Examples/nyt3.py)
