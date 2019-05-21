[TOC levels=1,2,3 numbered]: # "Class05"

# Class05
- [Class05](#class05)
- [Objectives](#objectives)
- [c05ex01](#c05ex01)
- [Data Structures](#data-structures)
  - [Tuples](#tuples)
  - [Lists](#lists)
  - [Manipulating lists](#manipulating-lists)
    - [append](#append)
    - [pop](#pop)
    - [del](#del)
    - [remove](#remove)
    - [insert](#insert)
  - [Dictionaries](#dictionaries)
- [c05ex02](#c05ex02)
  - [Casting a tuple to a list](#casting-a-tuple-to-a-list)
  - [Collections](#collections)
  - [The 'in' Python Operator](#the-in-python-operator)
- [c05ex03a](#c05ex03a)
- [c05ex03b](#c05ex03b)
  - [using zip to create a dictionary](#using-zip-to-create-a-dictionary)
    - [Example: Word Scramble](#example-word-scramble)
- [c05ex04](#c05ex04)
  - [List comprehensions](#list-comprehensions)
- [c05ex05](#c05ex05)
  - [Command line Input via program startup arguments in Python](#command-line-input-via-program-startup-arguments-in-python)
- [c05ex06](#c05ex06)
  - [Test1](#test1)


# Objectives

* Review and reinforce material from last class (structured programming (sequence, select, repetition), and functions)
* Introduce data structures (tuple, list, dictionary)
* Learn how to create functions that return multiple values, and can accept an arbitrary number of values. 

# c05ex01

Write a function that calculates the future value of a given present value (PV), invested for n terms, at an expected rate of return of r.

Test your function to ensure it works.


# Data Structures

We've covered variables such as int, bool, float and str. These, in a sense, are data structures, but we refer to them as `primitives`. You can also think of these are `atomic`, in that they are relatively indivisible and consist of `one thing`.

Often in programming we want to store more than `one thing`, we often want to group things into data structures. We call these `composite` data structures. This is where Python really shines, as Python has a number of built in composite data structures that are quite useful. We'll be covering a subset of these data structures: Tuples, Lists, and Dictionaries.

## Tuples

Tuples are a convenient way to store and access information in Python. They are a series of objects, where not all the objects need to be the same type.

Here is an example of a tuple of objects of the same type and how we reference the values found within a tuple.

```python
>>> atuple = (1000,1001,1002,1003)
>>> atuple[0]
1000
>>> atuple[1]
1001
>>> len(atuple)
4
>>> atuple[4] # Error! Indexes start at 0, so a tuple of 4 will have highest index of 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> atuple[3]
1003
>>> atuple[-1] # negatives "wrap around", so -1 gives us the last element in any size tuple
1003
```
NOTE: In the above examples, notice that if length of the tuple is four, then the possible index values are 0,1,2,3 ... and index 4 would be out of range. This is due to the zero based indexing. Indexes start at zero, not 1.


Tuples don't require you to store objects os a single type. Here is an example of a tuple of dissimilar objects (3 strings and an integer)

```python
>>> btuple = ("Dr.", "Tim", "Smith", 2039)
>>> len(btuple)
4
>>> btuple[0]
'Prof.'
>>> btuple[1]
'Tim'
>>> btuple[2]
'Smith'
>>> btuple[3]
2039
>>>
```

There's no reason why one of the objects in a tuple couldn't be a tuple - therefore tuples can also contain other tuples.

```python
>>> ctuple = (("Tim","Smith"),(123,"xyx street"),(23,32,45,54))
>>> ctuple[0]
('Tim', 'Smith')
>>> ctuple[0][0]
'Tim'
>>> ctuple[0][1]
'Smith'
>>> ctuple[2][1]
32
>>> ctuple[2][3]
54
```

## Lists

`Lists` are `tuples` that are mutable (that can be changed) (`tuples` are immutable - that is, they cannot change once they have been established).

For illustration, let's look what happens when we attempt to change one of the values of a `tuple`.

```python
>>> atuple=(1000,1001,1002,1003)
>>> atuple
(1000, 1001, 1002, 1003)
>>> atuple[0]
1000
>>> atuple[0]=999
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Now, let's create a `list` containing the same sequence of numbers. Look what happens when we attempt to change the number.

```python
>>> alist=[1000,1001,1002,1003]
>>> alist[0]
1000
>>> alist[0]=999
>>> alist
[999, 1001, 1002, 1003]
```

In the case of a tuple, we received an error when attempting to change one of the values. In the case of the list, we did not.

>Sidebar: You may ask, "why use tuples?". I offer three key reasons: 1) You want to protect the data within the data structure from being updated, 2) Accessing data using tuples is much faster than accessing data in lists (uses less processing) 3) taking advantage of the handling of immutable objects in modules and classes (more later)

A common feature of about tuples and lists is that in order to access any of the members of either, you use an index value. If there are two members of the tuple called atuple, then atuple[0] accesses the first member and atuple[1] accesses the second member. Tuples and lists are `ordered` data structures, and thus we use indexing to access each of the elements.

## Manipulating lists

There are a number of methods that we can use to alter lists.

### append
Append allows us to add something to the end of a sequence

```python
>>> alist = [2,1,4,16,11,234]
>>> alist.append(33)
>>> alist
[2, 1, 4, 16, 11, 234, 33]
```

### pop

Pop is list method the "pops" the last element of a sequence, that is, removes it from the sequence and returns its value.

```python
>>> alist = [2,1,4,16,11,234]
>>> alist.pop()
234
>>> alist
[2, 1, 4, 16, 11]
```
NOTE: This command pops (removes) that value at index 5 found in l. Pop actually returns the value that is deleted -- thus, "popping" it from the list.

### del

Del isn't a method, but a python command that deletes a object. We can use it as follows to delete an element of an array.

```python
>>> alist = [2,1,4,16,11,234]
>>> del alist[-1]
>>> alist
[2, 1, 4, 16, 11]
```

### remove

Unlike the previous mention methods, remove doesn't take as input an index, but rather a value. Hence, we can use it to the remove the first occurrence of the number 11 from the following list.

```python
>>> alist = [2,1,4,16,11,234]
>>> alist.remove(11)
>>> alist
[2, 1, 4, 16, 234]
```

Also, note that remove only removes the first occurrence found.

```python
>>> alist = [1,2,234,5,4,234]
>>> alist.remove(234)
>>> alist
[1, 2, 5, 4, 234]
```

### insert

Insert allows us to insert an object at a given index.

```python
>>> alist = [2,1,4,16,11,234]
>>> alist.insert(2,333)
>>> alist
[2, 1, 333, 4, 16, 11, 234]
```


## Dictionaries

In order to access an element contained within a tuple of a list, we can only use indices (whole number integers) to access elements. Dictionaries allow you access elements of a tuple or list by a name.

Let's look at an example.
```python
>>> adict = {'name':("Tim","Smith"),'address':(123,"xyx street"), 'data':(23,32,45,54)}
>>> adict['name']
('Tim', 'Smith')
>>> adict['name'][0]
'Tim'
>>> adict['address'][1]
'xyx street'
>>> len(adict['data'])
4
>>> adict['data'][len(adict['data'])-1]
54
```

Two ways in which we can create a dictionary:

Using `braces`:

```
>>> pets = {'dog':'Fluffy', 'cat':'Whiskers', 'rabbit':'Fang'}
>>> pets
{'rabbit': 'Fang', 'dog': 'Fluffy', 'cat': 'Whiskers'}
```

Using a constructor (looks like a function):

```
>>> pets = dict(dog='Fluffy', cat='Whiskers', rabbit='Fang')
>>> pets
{'rabbit': 'Fang', 'dog': 'Fluffy', 'cat': 'Whiskers'}
```

Dictionaries are particularly good at finding data:

```

>>> if 'rabbit' in pets:
...  print(pets['rabbit'])
...
Fang
```


Each lookup value/name in a dictionary must be unique. If you reuse a name, you will not get a runtime error but the original value that was stored at that name will be overwritten.

```
>>> pets = {'dog':'Fluffy', 'cat':'Whiskers', 'rabbit':'Fang', 'dog':'Killer'}
>>> pets
{'cat': 'Whiskers', 'rabbit': 'Fang', 'dog': 'Killer'}
```

To get just a list of keys:

```
pets.keys()
dict_keys(['dog', 'cat', 'rabbit'])
```

To get just the list of values:

```
pets.values()
dict_values(['Killer', 'Whiskers', 'Fang'])
```

# c05ex02

Write a program that uses a dictionary to translate a given digit (between 1 and 9) to it's word in French. Write a program that generates a random number between 1 and 9 (inclusive) and asks the user to enter the french word for that number. Display if they were correct or not, and then display and ask them for another number, etc. The user can end the program by entering a negative number. 



## Casting a tuple to a list

As we have seen previously, lists are less restrictive than tuples. Lists allow the programmer to change values after the list is initially created. Allowing such change not always desirable, but we may find situations when we've defined our data as a tuple, but later find that we need to change the data in the tuple. To do this, we can `convert` (programmer lingo for this is `cast`) the tuple to a list type. Once this is done, then the data can be changed. The programming, if needed, can then `convert` the list back to a tuple.

```python
>>> ctuple = (1000,1001,1002,1003)
>>> ctuple[0]=999 # because tuples data is protected, we will generate an error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> clist=list(ctuple) # cast to a list
>>> clist[0]
1000
>>> clist
[1000, 1001, 1002, 1003]
>>> clist[0]=999
>>> clist
[999, 1001, 1002, 1003]
>>> ctuple=tuple(clist) # cast back to a tuple
>>> ctuple
(999, 1001, 1002, 1003)
>>>
```

Now, remember that tuples and lists are `ordered` (we mentioned this previously), so you may assume that dictionaries are also ordered -- but they are not! Dictionaries will use whatever order is most efficient for lookup (it uses a hash table).  If you need an ordered dictionary, you can use OrderdDict from the collection library (see below), but it's rare that you need an order dict.

## Collections

Collections are a rather new data type (introduced in later 2 version of Python). These "advanced" data types include Chainmap, Counter, deque (Double ended Queue), defaultdict, namedtuple, OrderedDict, UserDict, UserList, Userstring. These can be thought of as more specific extensions of the Tuple, List, and Dictionary types covered above. For certain things we might do with a one of these other data types, Collections will be much quicker to code and will run much faster (for instance, see Counter objects)

We will not cover collection objects in this course. If you wish to continue on with your python development I'd encourage you to familiarize yourself with these: so that you can think, "hmm, what I'm doing with this tuple might be more efficiently handled using a Counter object" or other similar thoughts)

See: https://docs.python.org/3/library/collections.html

## The 'in' Python Operator

The in operator returns true if a given value is in a list, tuple, or string - and false otherwise. 


Let's look at checking to see if a value exists in a given tuple:

```python
>>> btuple  # we defined this in the above tuple examples
('Prof.', 'Tim', 'Smith', 2039)
>>> 'Tim' in btuple
True
>>> 'tim' in btuple
False
>>> 2039 in btuple
True
>>>
```

And, as you'd expect, you can also do this with lists (only the code will run slower)

```python
>>> blist  # we defined this in the above tuple examples
('Prof.', 'Tim', 'Smith', 2039)
>>> 'Tim' in blist
True
>>> 'tim' in blist
False
>>> 2039 in blist
True
>>>
```

We can also use in to test if a letter in in a string:

```python
>>> s = "Hello World"
>>> 'H' in s
True
>>> 'h' in s
False
>>> 
```

...and even check if a word is in a string:

```python
>>> s = "Hello World"
>>> 'Hello' in s
True
```

You can also use the "not in" form as well:

```python
>>> btuple  # we defined this in the above tuple examples
('Prof.', 'Tim', 'Smith', 2039)
>>> 'Tim' not in btuple
False
>>> 'tim' not in btuple
True
>>> 2039 not in btuple
False
>>>
```

The use of the `in` operator is especially useful when we wish to set up a loop to `traverse` all the elements of a list.
```
>>> alist = [2,1,4,16,11,234]
>>> for i in alist:
...     if i > 100:
...             print(str(i) + " is a big number")
...     else:
...             print(str(i) + " is a small number")
...
2 is a small number
1 is a small number
4 is a small number
16 is a small number
11 is a small number
234 is a big number
```

Now, with dictionaries, we can iterate over either all keys, or all values:

```

>>> pets = {'dog':'Fluffy', 'cat':'Whiskers', 'rabbit':'Fang', 'dog':'Killer'}
>>> for i in pets.keys():
...   print(i)
...
dog
cat
rabbit
>>> for i in pets.values():
...   print(i)
...
Killer
Whiskers
Fang

```

Notice, that if we don't specify it we want keys or values, it is assumed keys:

```
>>> for i in pets:
...   print(i)
...
dog
cat
rabbit
```

# c05ex03a

Create a tuple containing the names of all the courses you've completed at UT (for instance, ITM695, etc.)

Then write a program that allows a user to ask if you've taken a course. If what they enter is found in your list of courses, you respond with yes, otherwise no.

# c05ex03b

Copy and update your program from Ec05ex4a. Cast your tuple to a list, then add ITM695 to the list. Cast this list back to a tuple, and then print all values in the tuple using a for loop.

## using zip to create a dictionary

zip is one of the many built in functions found as part of the standard Python library (https://docs.python.org/3/library/functions.html). It's often used to create a dictionary from two lists -- where the first list is used as the keys, and the second list is used as the values. (NOTE: If the length of the lists differ, no error is generated, but only the matching pairs are used... the remaining portion of the longer list is simply ignored)

```
>>> alist=[1,2,3,4]
>>> blist=[22,23,24,25]
>>> d=dict(zip(alist,blist))
>>> d
{1: 22, 2: 23, 3: 24, 4: 25}
```
### Example: Word Scramble

Dictionaries can serve a an excellent way to translate one value to another. This can be useful for simple encryption (such as a caesar cipher) or anything we wish to "scramble".

```python
'''
Author:         Tim Smith
Description:    Word scramble game
'''

import string
import random

# create a list structure containing all the letters
letters = list(string.ascii_letters)
# sample without replacement (use random sample from the random library to shuffle letters)
codes = random.sample(letters, k=len(letters))

# create an encrypt and decrypt dictionary
encrypt_key = dict(zip(letters,codes))
decrypt_key = dict(zip(codes,letters))

# insert todays phrase (this could be changed to query a website, select from a supplied file with list
# of phrases. Note here that we randomly select a phrase from the plain_text_list. 
plain_text_list=["The secret of getting ahead is getting started", "For whom the bell tolls", "I can't get no satisfaction, but I try"]
plain_text = plain_text_list[random.randint(0,len(plain_text_list))-1]

# Here we scramble our phrase and create a new string called scrambled
cipher_text = ''
for i in plain_text:
    if i in string.ascii_letters:
        cipher_text += encrypt_key[i]
    else:
        cipher_text += i

# # Note, for those looking to understand more advanced techniques, we can accomplish the same things as the for loop
# # above using a single line "list comprehension"
# scrambled = ''.join([encrypt[x] if x in string.ascii_letters else x for x in phrase])


# Here we start our user interface, and let the player play the game
print("\nWelcome to word scramble!\n\n")

while True:
    print("Todays word is:")
    print(cipher_text)

    user_input = input("\nPlease enter your guess (or type exit to exit): \n")

    if user_input.lower() == "exit":
        break
    elif user_input == plain_text:
        print("\nThat is correct! Great work")
        break
    else:
        print("\nSorry, that is incorrect. Please try again.\n")

print("\n\nThanks for playing word scramble.\n\n")
```
# c05ex04

Using a dictionary structure, create a program that encrypts a phrase given by the user. (start with the word scramble example and alter it to provide this solution)

## List comprehensions

From math, you're probably familiar with set notation (where a given variable is drawn some a set, and the set is defined as subset of the integers, or reals, or other). A list comprehension creates a set of values that are stored in a list. 

List comprehensions are a powerful means of taking this idea and bringing it to your programming. It is an example of what is found in "functional" programming languages.

```python
s1 = [x for x in range(10)]
s2 = [x**2 for x in range(10)]
s3 = [x for x in range(10) if x % 2 == 0]
print(s1)
print(s2)
print(s3)
```

The output of which will be...

```
$ python fun03.py
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 2, 4, 6, 8]
```
A list comprehension creates a list. (Keep in mind that this list is stored in Primary Storage -- and therefore, lists such as "all integers" would be infinite, and you don't have infinite memory in your computer.)

List comprehensions are often used to process a list of values:

```
>>> data = [1,2,3,4,5,6,7,8,9]
>>> [x/2 for x in data]
[0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
>>> [x**2 for x in data]
[1, 4, 9, 16, 25, 36, 49, 64, 81]

```

You can even include if structures within a list comprehension:

```python
[x for x in range(1000) if x % 2 == 0]
```

We can even embed list comprehensions inside list comprehensions. For example, the following generates a set of prime numbers:

```python
[x for x in range(2, 1000) if all(x % y != 0 for y in range(2, x))]
```

>all() is part of the Python builtin library - https://docs.python.org/3/library/functions.html#all

> NOTE: List comprehensions are part of `functional` programming. If you are interested in exploring more on functional programming concepts in python, see here https://www.datacamp.com/community/tutorials/python-list-comprehension.

# c05ex05

Use a list comprehension to create a list of the cubes of the first 100 integers.

Using a for loop, display this list of numbers to the screen with dash as a separator character.

ex.
```
1-8-27...-10000
```
NOTE: The dash is only between numbers, as a separator. 

## Command line Input via program startup arguments in Python

NOTE: Windows users will need to have python.exe in their "path". You can add the path to python using .bashrc and install it in your user directory. Whenever bash starts, it will read this file and set the path you have set within the .bashrc file. See and example .bashrc file posted in the ClassNotes/Resources folder).

Command line input is a way to get user input, or provide a programmatic interface for other programs to interact with yours.

Create a program with the following code
```Python
import sys
print(sys.argv)
```

And then run it from the command line as follows:
```python
$ python myprog.py first second third
['myprog.py', 'first', 'second', 'third']
```

Now, I can access these arguments as follows
```python
import sys
print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
```

And, now when I run the program again

```python
$ python myprog.py first second third
['myprog.py', 'first', 'second', 'third']
myprog.py
first
second
third
```

But what happens when to attempt to read more arguments that were given by the user?

```python
import sys
print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])
```

And, now when we run the program, we get an error:

```python
$ python myprog.py first second third
['myprog.py', 'first', 'second', 'third']
myprog.py
first
second
third
Traceback (most recent call last):
  File "myprog.py", line 7, in <module>
    print(sys.argv[4])
IndexError: list index out of range
```

You should always protect your programs from users not using your system correctly. In this case, we need to add better logic surrounding how many arguments we will read.

```python
import sys
for i in range(0, len(sys.argv)):
    print(sys.argv[i])
```

# c05ex06

Write a program that simply prints out any command line arguments given to the program that start with the dash character.

>NOTE: Given a string called S, you can get the first character of the string using using index 0, S[0].


## Test1

Test1 will go live after class. You will find it in the Test Repo within the Classes gitHub site. You must submit your answers to your personal private repo (ST0??) by **2:00pm** before the start of Monday's class. Late submissions will not be accepted, so be sure to start this early. If you leave this to the last minute you will risk failing the test. NOTE: This test also tests your ability to work with git/github. You'll need to be able to push this to your github repo in order to submit your test. 



