[TOC levels=1,2,3 numbered]: # "Class09"

# Class09
- [Class09](#class09)
- [Objectives](#objectives)
- [Secure Code & Debugging](#secure-code--debugging)
  - [Style guides and best practices](#style-guides-and-best-practices)
  - [Exception Handling](#exception-handling)
  - [Static Analysis](#static-analysis)
    - [Static Analysis with Bandit](#static-analysis-with-bandit)



# Objectives


# Secure Code & Debugging

Two general forms of errors. Compile time errors (these are errors in syntax and structure), and runtime errors (these can be the most incidious and difficult to track).

Syntax errors are caught during the compile phase of developing software. Since Python is (generally) an interpreted language, only the code that is run is "compiled", and thus with Python, live testing (with well thought out test cases) of code is especially important. With a compiled language, if there is an error in a branch of code that only gets executed under the right conditions, syntax will still be found during the compile process --  even if the code never runs. With Python, you need to have the branch of code run in order to identify if there are any 'compile time' errors. (NOTE: This is a side effect of the dynamic nature of Python that makes it easy to work with -- as the saying goes "There is not such thing as a free lunch")

## Style guides and best practices

When working on a large project, you'll often encounter a "style guide" (developed and/or managed by some project lead(s)). Though such guides might seem to "impose" unnecessary structure, it's important to follow any such guides as they as essential to help teams coordinate efforts to increase readability of code, and decrease incidents of introducing errors in the code.

Some best practices:
* We all write buggy code. You're not above this. Accept this, and deal with it.
    * Double, and triple, check your code before release to production.
    * Write your code with testing in mind. Take a "test" driven development mindset.
* Follow any style guide(s), within reason:
    * Special cases aren't special enough to break the rules.
    * Although practicality beats purity.
* Readability counts:
    * Beautiful is better than ugly.
    * Explicit is better than implicit.
* KISS (Keep it simple stupid) - what is the simplest approach that could possibly work and meet requirements?
   * Simple is better than complex. Complex is better than complicated.
   * Flat is better than nested
   * Sparse is better than dense
   * If the implementation is hard to explain, it's a bad idea.
   * If the implementation is easy to explain, it may be a good idea.
* Code with the purpose and objective in mind
    * In the face of ambiguity, refuse the temptation to guess.

If you write ```import this``` within a python interactive session, you'll see displayed "The Zen of Python".

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## Exception Handling

By now, we should all be familiar with writing code like the following:

```python
my_num = int(input("Please enter a whole number between 1 and 100: "))
print(my_num)
```

This code will work find, as long as the user "plays nicely". For instance, let's say the user (taking things very literally), enters the number 1.2


Something like this will cause your code to do what is called "throw an exception". Unhandled exceptions will result in the program terminating with the a "Traceback" message.

```
Please enter a number between 1 and 100: 1.2
Traceback (most recent call last):
  File "C:/Users/Tim/Dropbox/__UT/ITM695/PyCharm695M18/ClassNotes/Class09/Examples/test.py", line 3, in <module>
    my_num = int(input("Please enter a number between 1 and 100: "))
ValueError: invalid literal for int() with base 10: '1.2'
```

Notice the exception that has been thrown is "ValueError".

Exception handling is a means of "catching" such exceptions, and handling any associated issues with a bit more grace.

To handle this input, for instance, we can use exception handling to catch the exception and ask the user to enter the value again.

```python
while True:
    try:
        my_num = int(input("Please enter a whole number between 1 and 100: "))
        break
    except ValueError:
        print("Input error. You have entered a non-integer value. Please read the instructions and try again.")```
```

The above code will catch any exceptions related to attempting to cast the user input to an integer (such the user entering a string of characters)

We commonly look to catch exceptions when dealing with files. For instance, if you attempt to open a file for reading that doesn't exist, this will cause your program to crash with a "FileNotFound" exception. To stop this:

```python
try:
    with open('execution.log') as file:
        read_data = file.read()
except FileNotFoundError:
    print("ERROR: The execution.log file was not found")

```

You can explore all of Python's builtin exceptions here https://docs.python.org/3/library/exceptions.html

## Static Analysis

Static analysis is an analysis of code at "compile time" - it's analyzing code without executing it. Static analysis involves scanning code to identify potential issues. Static analysis is accomplished both manually (code review) and through tools like pyflakes, bandit, etc.

Why use this? You can automate security and issue testing in your "devOps" (developer operations) processes.

> DevOps is the combination of cultural philosophies, practices, and tools that increases an organization's ability to deliver applications and services at high velocity: evolving and improving products at a faster pace than organizations using traditional software development and infrastructure management processes.


### Static Analysis with Bandit

Bandit is a tool designed to find common security issues in Python code. To do this Bandit processes each file, builds an AST from it, and runs appropriate plugins against the AST nodes. Once Bandit has finished scanning all the files it generates a report.

(for more on bandit, see here https://pypi.org/project/bandit/)

Let's install bandit...


```
pip install bandit
```

NOTE: You may get a warning to install msgpack (or other). Simple use pip to install any missing packages.

```
$ pip install bandit
Collecting bandit
  Downloading https://files.pythonhosted.org/packages/77/41/d57366098a30a86af1821e231949221d2b6b896cc4bdd060cc1be27fdd47/bandit-1.4.0-py2.py3-none-any.whl (116kB)
    100% |████████████████████████████████| 122kB 928kB/s
Requirement already satisfied: six>=1.9.0 in c:\users\tim\anaconda3\lib\site-packages (from bandit) (1.11.0)
Requirement already satisfied: PyYAML>=3.10.0 in c:\users\tim\anaconda3\lib\site-packages (from bandit) (3.12)
Collecting GitPython>=1.0.1 (from bandit)
  Downloading https://files.pythonhosted.org/packages/88/9c/b462dddb492204417f88d538b0931e87631f2a98afe89842929f4ed9ca5b/GitPython-2.1.9-py2.py3-none-any.whl (447kB)
    100% |████████████████████████████████| 450kB 1.6MB/s
Collecting stevedore>=1.17.1 (from bandit)
  Downloading https://files.pythonhosted.org/packages/17/6b/3b7d6d08b2ab3e5ef09e01c9f7b3b590ee135f289bb94553419e40922c25/stevedore-1.28.0-py2.py3-none-any.whl
Collecting gitdb2>=2.0.0 (from GitPython>=1.0.1->bandit)
  Downloading https://files.pythonhosted.org/packages/e0/95/c772c13b7c5740ec1a0924250e6defbf5dfdaee76a50d1c47f9c51f1cabb/gitdb2-2.0.3-py2.py3-none-any.whl (63kB)
    100% |████████████████████████████████| 71kB 1.3MB/s
Collecting pbr!=2.1.0,>=2.0.0 (from stevedore>=1.17.1->bandit)
  Downloading https://files.pythonhosted.org/packages/2d/9d/7bfab757977067556c7ca5fe437f28e8b8843c95564fca504de79df63b25/pbr-4.0.3-py2.py3-none-any.whl (98kB)
    100% |████████████████████████████████| 102kB 1.6MB/s
Collecting smmap2>=2.0.0 (from gitdb2>=2.0.0->GitPython>=1.0.1->bandit)
  Downloading https://files.pythonhosted.org/packages/e3/59/4e22f692e65f5f9271252a8e63f04ce4ad561d4e06192478ee48dfac9611/smmap2-2.0.3-py2.py3-none-any.whl
distributed 1.21.8 requires msgpack, which is not installed.
Installing collected packages: smmap2, gitdb2, GitPython, pbr, stevedore, bandit
Successfully installed GitPython-2.1.9 bandit-1.4.0 gitdb2-2.0.3 pbr-4.0.3 smmap2-2.0.3 stevedore-1.28.0
```

Watch for any message that may something about a package that is required but not installed (you may, or may not have to - you only have to if there is a message saying so.


Having bandit scan a code tree (your project and project subfolders)

Inside PyCharm, right click on the root folder of your project and select "Open Terminal Here". Once the terminal is open, run the following command.

```
bandit -r ./
```

> NOTE: There are a number of command line arguments that can be passed to bandit. `-r` means recursive - that is, run in the supplied directory and all sub directories within this directory.

Or, you can be more selective

```
bandit ./subdirectory/*.py
```

Now, let's find any security issues in the code you've written for class.

Move to a directory with some of your code, and type:

```
bandit -r ./ -f html -o outresults.html
```

* -o output file
* -f type of output file format (in this case, html)


After this is finished, you will find an outresults.html in this folder. This file contains all the security issues detected by bandit. You can view this output in a web-browser (by opening the file using a web-browser) or vscode. 

You'll notice there are two measures of issues: Severity, and Confidence about the finding.

For more information see https://github.com/PyCQA/bandit


