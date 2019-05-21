[TOC levels=1,2,3 numbered]: # "Class06"

# Class06
- [Class06](#class06)
- [Objectives](#objectives)
- [Review](#review)
  - [I’m really, really stuck and I need help.](#im-really-really-stuck-and-i-need-help)
  - [More on GitHub](#more-on-github)
  - [c06ex0a - proposing a change to a repo you do not have write access to (using only github)](#c06ex0a---proposing-a-change-to-a-repo-you-do-not-have-write-access-to-using-only-github)
  - [c06ex0b - updating forked repo with upstream changes](#c06ex0b---updating-forked-repo-with-upstream-changes)
  - [c06ex0c - proposing a change to a repo you do not have write access to (from a local copy usinfg git, vscode, and github)](#c06ex0c---proposing-a-change-to-a-repo-you-do-not-have-write-access-to-from-a-local-copy-usinfg-git-vscode-and-github)
- [c06ex0d - handle merge conflicts between local and remote repo (easy - when no changes have been made to the same file)](#c06ex0d---handle-merge-conflicts-between-local-and-remote-repo-easy---when-no-changes-have-been-made-to-the-same-file)
- [c06ex0e - handle merge conflicts between local and remote repo (more difficult - when changes have been made to the same file)](#c06ex0e---handle-merge-conflicts-between-local-and-remote-repo-more-difficult---when-changes-have-been-made-to-the-same-file)
- [c06ex0f - creating branches, switching between them, and merging content between branches](#c06ex0f---creating-branches-switching-between-them-and-merging-content-between-branches)
- [c06ex0g - restoring to a previous commit](#c06ex0g---restoring-to-a-previous-commit)
- [The enumerate function](#the-enumerate-function)
- [Strings and string formatting](#strings-and-string-formatting)
  - [Split](#split)
  - [String slicing](#string-slicing)
  - [String find](#string-find)
    - [Other methods](#other-methods)
- [c06ex01:](#c06ex01)
  - [String formatting](#string-formatting)
    - [Format specification](#format-specification)
- [Working with data from files](#working-with-data-from-files)
  - [Reading and writing files](#reading-and-writing-files)
    - [Plaintext ("Text") files](#plaintext-%22text%22-files)
    - [Binary files](#binary-files)
  - [Writing Text Files](#writing-text-files)
    - [Using With statement](#using-with-statement)
  - [Reading Text Files](#reading-text-files)
- [c06ex02](#c06ex02)
  - [Binary files](#binary-files-1)
  - [Structured plaintext files](#structured-plaintext-files)
    - [CSV](#csv)
- [c06ex03](#c06ex03)
    - [JSON data](#json-data)
- [c06ex04](#c06ex04)
      - [Shelf files](#shelf-files)
- [c06ex05](#c06ex05)
- [Working with OS calls](#working-with-os-calls)
  - [Getting a list of all files within a directory](#getting-a-list-of-all-files-within-a-directory)
  - [Example patterns](#example-patterns)
    - [Search the system for files with a certain extension](#search-the-system-for-files-with-a-certain-extension)
- [Search the contents of Files](#search-the-contents-of-files)
  - [Regular Expressions Intro](#regular-expressions-intro)
    - [Finding words in a file](#finding-words-in-a-file)
    - [Finding integers in a file](#finding-integers-in-a-file)
    - [Finding floating point numbers in a file](#finding-floating-point-numbers-in-a-file)
    - [Finding email addresses in a file](#finding-email-addresses-in-a-file)

# Objectives

* Review Test
* More on github -- setting default editor, and handling merge conflicts
* More on Python
   * String formatting
   * Modules (and more on DocStrings) & Python Packages
   * Namespaces and Scoping
   * Reading and writing data in files
   * Searching data in files
   * The os package -- how to navigate and query the filesystem.

# Review

##  I’m really, really stuck and I need help.

First, try getting away from the computer for a few minutes. Computers emit waves that affect the brain, causing these effects:

* Frustration and/or rage.
* Superstitious beliefs (the computer hates me) and magical thinking (the program only works when I wear my hat backward).
* Random-walk programming (the attempt to program by writing every possible program and choosing the one that does the right thing).

Moreover, in a classroom environment, you also see effects such as:
* blame the professor
* call the professor names
* send the professor an email expressing your frustration
  
If you find yourself suffering from any of these symptoms, get up and go for a walk. When you are calm, think about the program. What is it doing? What are some possible causes of that behavior? When was the last time you had a working program, and what did you do next?

Creative problem solving begins with understamding the problem. Make sure you are at least first clear on what it is that you're trying to solve. Mr. Google (and stack overflow) can also help you in further refining your knowledge about the problem you are attempting to overcome.

(edited excerpt above from "How to think like a Computer Scientist")


## More on GitHub

It's time to revisit Git/GitHub. In the following exercises, you will learn...
1) How to propose a change to a repo you have read access, but do not have write access (for instance, a public repo)
2) How to update your local forked repo with the latest chamges in the upstream repo. 
3) How to clone a forked repo to your local machine, make changes, add, commit, push, and open a pull request to the origin "upstream" repo. 
4) How to manage and resolve "merge" conflicts between your local repo and your github repo. 
   1) When different files have been edits (easy)
   2) When the same file has been edited on both sides with different edits (a little more difficult)
5) How to create additional branches, switch between branches, and merge changes from one branch to another. 
6) Undoing things
   
For each of the following exercises, follow along with the professor as he walks you through this. 

## c06ex0a - proposing a change to a repo you do not have write access to (using only github)

Using the github interface, propose a change to a public repo https://github.com/tcsmith-tampa/c06ex0 by adding a hello message (Hello from <your name>, <URL to your GitHub profile>. (NOTE: This is the same as Test1 part1 -- so this is a refresher)

See video example [here](https://use.vg/bzwtBd).

## c06ex0b - updating forked repo with upstream changes

Note that your local fork of the c06ex0a repo is behind the upstream repo (this is what the original repo from which the fork came is called). 

Refresh your copy of the c06ex0a repo with all changes made to the upstream repo (see the video posted by the professor on refreshing local fork with any changes from the upstream repo)

See video example [here](https://use.vg/hDmpAi).

## c06ex0c - proposing a change to a repo you do not have write access to (from a local copy usinfg git, vscode, and github)

Clone your c06ex0 fork to your computer. 

Use VSCode make changes to the README.md file (add anything you wish)

Add, commit and push this change to README.md to your c06ex0 repo. 

Log into your github account and create a pull request to apply this new commit to the upstream repo. 

NOTE: See video walk-through example [here](https://use.vg/yQMOqi).

# c06ex0d - handle merge conflicts between local and remote repo (easy - when no changes have been made to the same file)

You may get into a situation where you have changes on your local repo that haven't been pushed to the remote (guithub) repo, but have also made changes on the remote (github) repo. In such situations, you'll find that you can push your work from the local repo to the server -- as you will see an error displayed. 

In this case, we'll simulate this by adding a file to my local repo, and adding another file to my remote repo before a push from the local repo has been made. In such situations both repos have a merge conflict -- where there are changes on both that been made since the last time the repo was synced. 

* Using github, create a new public repo called c06ex0d. Using the github interface, add a README.md file to this repo (write in the file something/anything you want).

* Clone this repo to your local computer. 

* Using VSCode, add a new file called Hello.md. Add the text Hello World to this file.

* Add, commit (BUT DO NOT PUSH!) this change.

* Now, log back into GitHub, and using the GitHub interface also make a change to your c06exd repo -- this time, add a new file called Hello2.md (put in the text "hello again" (or anything else you'd like) in this file)

* On your local computer, add and commit the local changes (that you made to the README.md file)

* NOW -- As a test, try to push this to github. You will receive an error about issues with merging. To resolve this, you'll need to do a pull request to merge the latest changes from your github repo (`git pull origin master`) into the changes made to your local repo.

* Once you do this (unless you've changed the default git editor) you will see you're in some strange editor call vim (you'll see how to change this in the next exercise). To exit this hit the ESC key, followed by :wq. This will write the text and quit the editor. 

* After doing this, your local repo has merged the changes on github to the changes made to your local repo. The final step now is to push everything up to the server (to ensure that both the local and server repos are now in sync).

NOTE: See video walk-through example [here](https://use.vg/AfhyBB).

# c06ex0e - handle merge conflicts between local and remote repo (more difficult - when changes have been made to the same file)

Set VSCode as your merge editor:

`git config --global core.editor "code --wait"`

Now, when you have a merge conflict (or when you need to comment a commit because you forgot to include the commit message in the command line argument), you will see VSCode instead of vim (or other).

Now, we're following the basic steps as in c06ex0d, but this time make changes to the same file (last time we added two different files). 

* Within your local c06ex0d repo, using VSCode, edit the READMD.md. Add any new text that you'd like.
* Add, commit (BUT DO NOT PUSH!) this change.
* Now, log back into GitHub, and using the GitHub interface also make a change to your README.md file in your c06exd repo.
* NOW -- As a test, from your local repo, try to pull the changes down from github. You will receive an error about issues with merging. 
```
 From https://github.com/timcsmith/c06ex0d
 * branch            master     -> FETCH_HEAD
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

* To resolve this, you'll need to edit your README.md file. 
* open README.md in vscode, and you'll see something like the following

```
# c06Ex0d

Test repo
<<<<<<< HEAD
Another line added
=======

Added another line via the github interface
>>>>>>> 919d85486a38d6c29b763281c7f9f8441b0dd8d5

```

* You must edit this file to be what you want. Here is what my REAMDE.md looks like after these edits(note that VSCode has a few options displayed in the text -- that you can select to resolve the issue -- OR you can simply edit it by hand)

```
# c06Ex0d

Test repo
Another line added

```

* Once you do this, you can now add, commit this change to your local repo, and then push thsi new commit up to your remote repo (GitHub).
  


# c06ex0f - creating branches, switching between them, and merging content between branches


As discussed in class, a typical development repo will have multiple branches. A common structure is to have master, testing, and dev (possibly multiple dev branches, named by feature of the person working on the branch).

Every repo has at least one branch called master. In this exercise, we will create a new branch called dev, checkout this branch and make a few changes, and once we're happy with these changes, merge these changes into the master repos. 

Branches allow us to better organize our code in large projects. Master is usually kept as a "clean" branch; that is, all code in the b ranch is complete (and tested). Development is typically done in a separate branch, and then once the branch is ready, merged into the master branch. This keeps the work in progress separate from the released work. 

Let's work with your PublicRepo in your UT.edu github account. 

1. If you haven't already done so, clone this repo to your local machine. If you already have a clone, make sure it's in sync with the remote (git status will tell you if it is -- if it's not, then make sure they are before you proceed). (NOTE: If your local repo is ahead of the remote, then you will push the latest changes to the remote. If the remote is ahead of the local repo, you will pull the latest changes from the remote)
2. Within your local repo, list all the branches (`git branch`) and note that there is only one branch called master. 
3. Now create a dev branch called "dev" (`git branch dev`). 
4. Again, list the local branches (`git branch`), but see that there are now two local branches. 
5. Switch to you new dev branch (`git checkout dev`). 
6. Make a change to your README.md file. Add this change (`git add REAMDE.md`), commit this change (`git commit -m "minor change to README.md for testing of branches`). 
7. Now do a git status to get a view of the status of your repo. 

So far you've only made a change to the files in the dev branch (which is your current branch). Let's merge this change into your master branch. 

8. First your will need to switch to the master branch (`git checkout master`)
9. then you will `merge` the dev branch into master (`git merge dev`). 


NOTE: If you wish to have a deeper understanding on how branching works in git, read sections [3.1](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell), [3.2](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging), [3.3](https://git-scm.com/book/en/v2/Git-Branching-Branch-Management), [3.4](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows), [3.5](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches),[3.6](https://git-scm.com/book/en/v2/Git-Branching-Rebasing), and [3.7](https://git-scm.com/book/en/v2/Git-Branching-Summary) for the official guide of git branching (and related merging and rebasing)


# c06ex0g - restoring to a previous commit

This isn't an exercise you need to complete -- but, I'd suggest that you experiment with....

Often you'll only find a mistake until after a commit is made. First, it's best to identify mistakes before attempting to stage a file. If you happen to stage an incorrect file, but have not yet committed it, you can run the following command to empty your staging area and restore the files to their previous state ('git reset HEAD`). But, if you've messed things up and have committed these errors to the repo, you may wish to revert back to a previous commit. To reset to a previous commit (and erase all changes since), use the command 'git reset HEAD --hard`.

In in your local PublicRepo, using VSCode make a change to your README.md file. Save this change, and add this to staging. Now, you've decided that you don't want to commit that change -- and just want to forget about it - type the command `git reset HEAD` (or to remove only a specific file `git reset HEAD filename`). Now when you do a `git status` you will notice that any changes are now unstaged.

Note that you can also remove individual files from teh repo itself (see `git rm`,. and `git rm --cached`). For more indepth view of "undoing things", see section [2.4](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) of the official git documentation. 



# The enumerate function

We've been using for loops now for a few class. As you should now know, we often use for loops to traverse all the elements of data structure -- such as a list.

For example, let's look at a program the prints all the elements of a list of the cubes of the first 10 integers starting at 0 with a dash separator between the numbers.

```python
numbers = [x**3 for x in range(10)]

count = 0
for i in numbers:
    print(i, end='')
    if count < len(numbers)-1:
        print('-', end='')
    count += 1
```

But, it's extra work to manage the count variable, and with extra work, it increases the chance that a programmer will make an error.

Creating and using a counter in for loops is so common, the developers of Python have added the enumerate() function. Using it can eliminate simply the use of a counter.

```python
numbers = [x**3 for x in range(10)]

for count, i in enumerate(numbers):
    print(i, end='')
    if count < len(numbers) - 1:
        print('-', end='')

```

# Strings and string formatting

We've been using strings and string concatenation. Let's look at more examples of of manipulating strings:

## Split

Strings, like turtle objects and list objects, have methods. Split is one of those methods.

We use split to split a string into a number of substrings. Split requires a delimiter string that identifies where the split(s) are to be made.

For instance, the following code will split a string based on spaces.

```python

astring = "This is a string"
bstring = "This is another string"

words = astring.split(' ')
print(words)

words = words + bstring.split(' ')
print(words)

# There is a fourth composite type called a set (remember: the other three are Tuple (too-ple), List and Dictionary). Set is like a list, only that each element of a set will be unique.
# If you add a new value that already exists in the set, this addition will be ignored. This comes in handy, for
# instance, if we want to find the unique values in a list.
print(set(words))
```

## String slicing

We often wish to take "slices" of strings -- that is, look at some substring or segment of a string.

```
astring = "Hello World"

print("0:  " + str(len(astring)))
print("1:  " + astring[1:11]) # from from index 0 up-to but not including index 11
print("2:  " + astring[1:])  # If you're copying to the end of a string, you can leave out the last index
print("3:  " + astring[:3]) # from start of string
print("4:  " + astring[:]) # copy of the entire string
print("5:  " + astring[::2]) # every second character of the string
print("6:  " + astring[1:8:2]) # every second character from index 1 up to but not including index 8
print("7:  " + astring[::-1]) # reversed string
print("8:  " + astring[-1]) # the last character of the string
print("9:  " + astring[-2]) # the second last character of the string
print("10: " + astring[1:-1]) # the string with the first and last character dropped. 
print("11: " + astring[-2:0:-1]) # the reverse of the string with the first and last character dropped.

```

Let's say we have a list of strings. How can we both select a string from the list, and a character in that string?

```
alist = ["hello", "world"]
print(alist[0][0]) # select the first element of the list (the string) and then select the first character of that string
print(alist[1][0]) # select the second element of the list (the string) and then select the first character of that string
print(alist[2][0]) # index out of bounds error, as there is not element in the list at index 2.
print(alist[1][::-1]) # the second element of the list, reversed
```

We can also have a dictionary of strings;

```
adict = {"first":"Hello", "second":"World"}
print(adict["first"][0]) # select the value at the key "first" (a string) and then select the first character of that string
print(adict["second"][0]) # select the value at the key "second"  and then select the first character of that string
print(adict["third"][0]) # key error, there is no key called "third"
print(adict["second"][::-1]) # the second element of the list, reversed
```

We can also have a list of lists, that have strings (or any other types we'd like)...

```python
alist = [["hello", "world"], ["another", "list"], ["yet", "another", "list"]]
print(alist[0][0]) # hello
print(alist[1][0]) # another
print(alist[2][0]) # yet
print(alist[2][0][0]) # y
print(alist[0][0][0]) # h
print(alist[0][1][0:2]) # wo
```

## String find

String find allows you to search a string. It returns an index to the start of the string found, or -1 if the string was not found.

You can provide string find with a begin and end index -- which is useful if you want a way to find the next occurrence of a string.

```python
astring = "This sentence has repetition, repetition, and more repetition."

print(astring.find("sentence"))    # this returns the index to the start of the word found

print(astring.find("repetition"))     # find the first occurrence (index 18)

print(astring.find("repetition", 19))  # to find any other occurrences, I need to start the search after the first one found

print(astring.find("xray")) # returns -1 if the string was not found
```

### Other methods

* s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
* s.strip() -- returns a string with whitespace removed from the start and end
* s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
* s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
* s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
* s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc

NOTE1: See [here](https://www.w3schools.com/python/python_ref_string.asp) and in the official [Python Documentation](https://docs.python.org/) for more detail on the available string methods.

NOTE2: Most string methods do not affect the data inside the object. They return the altered data but keep the objects data unchanged.

```python
astring = "Hello"
astring.upper()
print(astring) # note that astring is not all upper 
if astring.upper == "HELLO":
    print("The astring contains upper or lower letters in HELLO")
    print(astring)
astring = astring.upper()
print(astring)
print("world".upper()) # note that even literals have methods - "world" is a string, therefore, it has all the string methods
```

Now, let's revisit a problem we did last class -- that is, produce the cubes of the first 100 integers (from 0 to 99 inclusive), with a dash character separating each number. 

Here is the step by step version using the join method...

```python
# here is a step by step version
cubes = [x**3 for x in range(100)] # create a list of the cubes of each of the numbers from o to 99
cubes_as_strs = [str(x) for x in cubes] # cast each element in the cubes list to a string type
seperator = "-" # create a string with the separator characters
outstr = seperator.join(cubes_as_strs) # join the strings found in cubes_as_strs using the seperator 
print(outstr)
```

...here are all the steps above written in one line (this is how an experienced program would write the above steps)

```python
print("-".join([str(x**3) for x in range(100)]))
```

# c06ex01:

Write a program that accepts user input of a string, and prints that string with only the first and last characters as upper, amd the other characters as lower.

PS: see if you can do c06ex01 with at most two lines of code.

## String formatting

Often, we require more control over the output of our strings. Python 3 includes the format method to help us with this (note: there is the older style that useses the percentage operator -- we will only cover the modern approach, using the more powerful format method)

```python
s1 = "My name is {0}!".format("Dr. Smith")
print(s1)

name = "Bob"
age = 14
s2 = "I am {1} and I am {0} years old.".format(age, name)
print(s2)

n1 = 4
n2 = 5
s3 = "2**10 = {0} and {1} * {2} = {3:f}".format(2**10, n1, n2, n1 * n2)
print(s3)
```

The output of which will look as follows:

```
My name is Dr. Smith!
I am Bob and I am 14 years old.
2**10 = 1024 and 4 * 5 = 20.000000
```

### Format specification

Each of the replacement fields can also include a format specification. Format specifications allow you to have even more control over how a string is formatted.
* The format specify must preceed a colon characxter
* Can set the width allocation to a field
* Can align the field left (<), right (>) or center (^)
* Can specify something about how a specific type is displayed - i.e. Specify the number of decimal places to display for a float.

```python
x = 1/3 # this will produce a float with a long series of decimal places
print(x) # this will display a long series of decimals
print("{:.2f}".format(x)) # this will display only the first two decimals
x *= 2 # this will produce a float with a long string of 6's in the decimal
print(x)
print("{:.2f}".format(x)) # this will display only the first two -- note that it rounds
print("{:.2f}".format(int(x*100)/100)) # python does not have a truncate function, but you can do a little math to accomplish truncation
```

If you need to truncate the float (google truncate if you are not familiar with the term) instead of rounding, you can do this using the following pattern...

```python
x = 2/3
print("{:.2f}".format(int(x*100)/100)) # python does not have a truncate function, but you can do a little math to accomplish truncation
```

Let's look at creating extra space in our strings, and centering, left justifying, and right justifying values....

```python
c1 = "United States"
c2 = "China"
c3 = "Germany"
c4 = "United Kingdom"

print("Pi to three decimal places is {0:.3f}".format(3.1415926))
print("|{0:<18}|{1:^18}|{2:>18}|{3}|".format(c1,c2,c3,c4))
```
The output of which is:

```
Pi to three decimal places is 3.142
|United States     |      China       |           Germany|United Kingdom|
```

You can find out more about string formatting in python [here](https://realpython.com/python-string-formatting/) and in the official [Python Documentation](https://docs.python.org/).


# Working with data from files

Up until now, all our data used within out programs has either been written into the program (as literal values) or entered by a used (either from the command line, or from a text interface that you've developed).

What we will look at today is how to access, and store, data in files.


## Reading and writing files

Files are typically text, or binary, and structured or unstructured.

### Plaintext ("Text") files

Plaintext files only contain basic text characters and do not include information on font, size, or color. We typically see text files having the .txt extension, but Python script files ending with the .py extension are also examples of plaintext files. These text files can be opened with Windows’s Notepad or OS X’s TextEdit application. Using Python you can read the contents of plaintext files and treat them as an ordinary string values.

### Binary files
Binary files are files that are not intended to be read directly on the screen. These files contain raw data that has been stored in the file.

Our work in this course will focus on plaintext files. This is the more common method used to store and retrieve information from files.

## Writing Text Files


```python
file = open("test.txt", "w") # open file - create if new or overwrite if exists
file.write("Hello world!")
file.write("...and yadda yadda yadda.")
file.close()
```

Using the command prompt we can run this script and view the contents of the file test.txt.

```
$ cat test.txt
Hello world!...and yadda yadda yadda.
```

To append to the file

```python
file = open("test.txt", "a") # open the file for writing, be keep the original text
file.write("Hello World again")
file.close()
```

To see the results we can review the output file:

```
cat test.txt
Hello world!...and yadda yadda yadda.Hello World again
```

Let's add more lines:

```python
file = open("test.txt", "a")
file.write("\n\nHello World again, and again\n")
file.close()
```

...And observe the output:

```
$ cat test.txt
Hello world!...and yadda yadda yadda.Hello World again

Hello World again, and again
```

Often we will use loops to write data to our file:

```python
file = open("test.txt", "a")
file.write("\n\nHello World again, and again\n")
file.close()
```

### Using With statement

It's good to develop the habit of using the with statement. Using the with statement we don't have to remember to close the file, it will be automatically closed for us.

```python
with open("test.txt", "a") as file:
  for x in range(0, 10):
    file.write(str(x) + "\n")
```

...and the output of which is:

```
$ cat test.txt
Hello world!...and yadda yadda yadda.Hello World again

Hello World again, and again
0
1
2
3
4
5
6
7
8
9
```

## Reading Text Files

Reading text files is similar to the write. We'll use the with statement for our examples here.

If you want to read the entire file contents into a string, use the read function
```python
with open("test.txt", "r") as file:
  content = file.read() # reads the entire file into memory as a string
print(content)
```

The output of which would be our entire text file:

```
$ python text_file5.py
Hello world!...and yadda yadda yadda.Hello World again

Hello World again, and again
0
1
2
3
4
5
6
7
8
9
```

__NOTE1__: Files and filepaths. When referencing a file that is in the current directory of the script, we only need to provide the filename. There are times, however, when we will need to reference a file that is located in another directory. In such cases we will need to provide the path along with the filename. There are differences between Windows and MacOS in how file paths are expressed. We will be using the Windows version in this course, which uses the drive letter and backslash format (i.e. "C:\folder\subfolder\filename.txt"). MacOS and Linux use forward slash, and may not use drive letter references - for instance, in MacOS "/Volumes" folder, and in Linus, "/mnt". If you are using one of these other platforms, you will need to translate these path references to your particular platform. Python does have built in library support to handle many of these issues - see os.path found here https://docs.python.org/3/library/os.path.html.

__NOTE2__: Since the backslash character (used in windows filepaths) is an escape character used in string formatting, we need to double the backslash as in the following example: "c:\\users\\bob\\file.txt"



# c06ex02

Using VSCode, create a sample text file. Write a few sentences in the file and save it as input_e2.txt.

Write a program called remove_vowels.py that accepts two filenames via command line arguments. The first filename will be used as the input file, and the second filename sill be used as the output file. The program will read input file, remove any vowels, and output the results to the output file. 

Ex:
```
$python remove_vowels.py input_e2.txt output_e2.txt
```

## Binary files

Unlike plaintext files, binary files contain information that is not constrained to just text. Binary files store information as binary data, and the interpretation of this data is generally very proprietary, or context specific. We will not be dealing much with binary files in this course, but you should be aware of them and how to deal with them when needed. Also, some file formats, such as Pythons "shelve" format and pickle formats (used to store Python objects) also use a binary format.

(if you find that you need to work with binary files, for further information look [here](https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch05s04.html and section 7.2.1) or  [here](https://docs.python.org/3.6/tutorial/inputoutput.html) )

## Structured plaintext files

Structured text files require some extra information in order for them to be interpreted. The information required is what structure is being used to arrange the data inside the text file. We'll cover two of the more popular formats, CSV and JSON.

### CSV

CSV file functions in Python:
* [official Python documentation](https://docs.python.org/3/library/csv.html)

Each line in a CSV file is a "row" (or record, observation, etc.), and the commas within the file indicate a new field (or cell, attribute, etc.).

CSV files are simple text files, making them convenient and well supported across many different applications. The downside to these files is that there don't contain any extra information such as Type of the values seen, don't indicate any formatting information (color, highlighting, ect.), don't have multiple worksheets, no specified width of the fields, etc.


```python
import csv
with open('sample.csv', 'r') as csv_file:
    sample_reader = csv.reader(csv_file)
    sample_data = list(sample_reader)
    print(sample_data)
```


Now, if you csv file has a header (which our example does), we can view it as follow:

```python
import csv
with open('sample.csv', 'r') as csv_file:
    sample_reader = csv.reader(csv_file)
    sample_data = list(sample_reader)
    print(sample_data[0][0:])
```


We can also load this data into a tuple structure:

```python
import csv
with open('sample.csv','w"') as csv_file:
    sample_reader = csv.reader(csv_file)
    sample_data = tuple(sample_reader)
print(sample_data[0][0], ": ", sample_data[1][0], sep='')
print(sample_data[0][1], ": ", sample_data[1][1], sep='')
```


Reading data using for Loop

```python
import csv
csv_file = open('sample.csv', 'r')
sample_reader = csv.reader(csv_file)
for row in sample_reader:
    print('Row #' + str(sample_reader.line_num) + ": " + str(row[0]))
```

Now, let's look at writing to a CSV file:

```python
import csv
csv_file = open('sample2.csv', 'w')
sample_writer = csv.writer(csv_file)
sample_writer.writerow(['Bob', 'Jones', '1234 Elm Street'])
sample_writer.writerow(['Jill', 'Green', '4321 Pine Avenue'])
csv_file.close()
```


__NOTE__: In the above code csv5.py, I switched from using the "with open..." form of opening files. I could have written this code as follows:

```python
import csv
with open ('sample2.csv', 'w') as csv_file:
    sample_writer = csv.writer(csv_file)
    sample_writer.writerow(['Bob', 'Jones', '1234 Elm Street'])
    sample_writer.writerow(['Jill', 'Green', '4321 Pine Avenue'])
    csv_file.close()
```

The output from either would be...

```
$ cat sample2.csv
Bob,Jones,1234 Elm Street
Jill,Green,4321 Pine Avenue
```

If we wanted to edit a values. Let's change Bob to Robert.

```python
import csv
with open('sample2.csv', 'r') as csv_file:
    sample_reader = csv.reader(csv_file)
    sample_data = list(sample_reader)

print(sample_data)
sample_data[0][0] = "Robert"

with open ('sample2.csv', 'w') as csv_file:
    sample_writer = csv.writer(csv_file)
    sample_writer.writerows(sample_data)

```

# c06ex03

Using vscode, create a csv file with four columns, and three rows, of random numbers (any numbers you'd like). 

Write a python program that reads this csv file, and creates a new csv file that has one column, and four rows, that contains the sum of each row of the input file. Name the output file whatever you'd like. Also, write the program so that it can accept an input file with any number of rows.

### JSON data

> JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language, Standard ECMA-262 3rd Edition - December 1999. JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language. (taken from www.json.org)

For more detail on the format of a JSON file, see www.json.org.

In Python, we can use a module "json" to serialize and store our Python objects in a json format file. We can also deserialize and bring these objects back into memory. Json thus serves as a convenient method of storing and sharing persistent data.

For example, let's create a json string (this could simply be a string stored in memory, which is a serialized version of the data structures we are interested in).

```python
import json

# Translate a python data structure to a JSON encoded string
somedata = [{'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4), 'b': 3.0}]
# sort_keys and indent are optional. Added to display nicely to screen
data_string = json.dumps(somedata,sort_keys=True,indent=4) 
print('JSON:', data_string)

```

We can also store this Json encoded string to a file, and later read this file.

import json

```python
# Translate a python data structure to a JSON encoded string
somedata = [{'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4), 'b': 3.0}]
data_string = json.dumps(somedata,sort_keys=True,indent=4) # sort_keys and indent are optional. Good for display to screen
print('JSON:', data_string)

with open('data01.json','w') as outfile:
    outfile.write(data_string)

with open('data01.json','r') as infile:
  data = json.loads(infile.read())

print("The type of the loaded data is ", type(data))
```

Here is an example that demonstrates how we can access elements of the data that has been loaded using JSON (keep in mind, that the data loaded is a list containing a dictionary structure, and the values in the dictionary are a list, a tuple, a float, and a dictionary)


```python
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

```

As we see from the above code, though this shouldn't be much of an issue, remember that tuples become lists when encoded and then decoded.

Here is an example of updating what is stored in a JSON file:  we load, edit, and the store the stored objects - thus simply rewriting the old file.

```python
import json
somedata = {'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4),
            'b': 3.0, 'c': {'x': 12, 'y': 100}}
print('ORIGINAL DATA: ', somedata)

with open('data.json', 'w') as fout:
  json.dump(somedata, fout)

with open('data.json', 'r') is fin:
  somedata = json.load(fin)

print('READ FROM JSON FILE: ', somedata)

somedata['fname'] = 'Al'
print('ORIGINAL BUT EDITED IN MEMORY: ', somedata)

with open('data.json', 'w') as fout:
  json.dump(somedata, f)

with open('data.json', 'r') as fin:
  somedata = json.load(f)

print('RE-READ FROM JSON: ', somedata)

```


__NOTE__: Notice that dictionary data types are unordered. If you print them, the order may not display in the same order in which the items were created, also, the order could change each time it is printed.


# c06ex04

Write a python program that creates and saves (to a JSON file) a data structure that consists of a list, within which there is one dictionary, and one tuple. Put in any data within these that you wish. Call the file output.JSON.


#### Shelf files

With the "shelf" modules, we can save python objects from memory into binary shelf files.

```python
import shelve
pets = ['Fluffy', 'Pookems', 'Killa']
e2f = {1:"un", 2:"deux", 3:"trois"}

with shelve.open('mydata.dat', "r") as shelfie:
  shelfie['pets'] = pets
  shelfie['english to french'] = e2f


with shelve.open('mydata.dat', "w") as shelfie:
  print("keys --->",list(shelfie.keys()))
  print("values ->", list(shelfie.values()))
```


...and the output of which looks like:

```
keys ---> ['english to french', 'pets']
values -> [{1: 'un', 2: 'deux', 3: 'trois'}, ['Fluffy', 'Pookems', 'Killa']]
```

__NOTE__: For information on Python object persistence and shelve, read more [here](https://docs.python.org/3.4/library/shelve.html). Using shelve will not be a requirement for any test or individual assignment in this course... but, it's good to know that it exists, just in case you could use something like this for your final project.

# c06ex05

Write a python program that creates and saves (to a Shelf file) a data structure that consists of a list, within which there is one dictionary, and one list. Put in any data within these that you wish (use the same one you created in c06ex03). Call the file out.shelf.

Write a second python program that reads the out.shelf file, and prints the contents of the file to the screen.


<strike>
# Working with OS calls

Often, we need to "talk" to the operating system and utilize some of the interfaces offered by your OS. One particular area that we find this used heavily, is navigating the file system. So far, we've just been creating and reading files that exist in the same directory that your program is run within. What about accessing other directories? What about getting listing of what is contained in a directory? To do these things, we need to use the OS libary.

## Getting a list of all files within a directory

```python
import os
for file in os.listdir("./"): 
    if file.endswith("*.*"):
        print(os.path.join("/mydir", file))
```

## Example patterns

### Search the system for files with a certain extension

The following snippet of code will search your entire drive and find all python files that you have write access to. Each time it finds a file, it will print it to the screen and append the full path to the file to the list variable all_writable_py_files:

```python
path = "C:\\" # for windows, default C drive
# path = "/" # for MacOS
all_writable_py_files = []
count = 0
for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        if filename.endswith(".py"):
            file_path = os.path.join(dirpath,filename)
            if os.access(file_path, os.W_OK):
                count += 1
                all_writable_py_files.append(file_path)
                print(str(count) + "  " + file_path + " is writable")
```

# Search the contents of Files

Though we can use standard python operators such as equals, and in, to explore the contents of a file - Python includes a powerful pattern matching system called "Regular Expressions."

For this course, you'll only need to know how to find and use an existing regular expression (you will not need to build any new ones).

__SIDEBAR__ One very useful facility/function in Python is regular the expressions package, re. We'll not have time to elaborate much more thatn the following section, but if you're interested work thorough this intro [here](https://developers.google.com/edu/python/regular-expressions), and the interactive exercise [here](https://regexone.com/lesson/introduction_abcs)
## Regular Expressions Intro

### Finding words in a file

```python

import re

# for more on regex, see https://developers.google.com/edu/python/regular-expressions
# or https://regexone.com/references/python
# or https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285

data = input("Enter text: \n")

reg = re.compile(r'([A-Z][^\.!?]*[\.!?])') # note r here signals that it's a raw string
m = reg.findall(data)

print(m)

# try entering the following data
# THis is a sentence. This is another sentence. asdfasdf asdfasdf : . This is one last sentence.
# this program will identify the sentences, and output the following
# ['THis is a sentence.', 'This is another sentence.', 'This is one last sentence.']

```

### Finding integers in a file

Use the regular expression:

```
reg = re.compile(r'\d+')
```


### Finding floating point numbers in a file

Use the regular expression:

```
reg = re.compile(r'\d+\.\d+')
```


### Finding email addresses in a file

Use the regular expression:

```python
reg = re.compile(r'[\w\.,]+@[\w\.,]+\.\w+')
```
</strike>


