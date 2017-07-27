Programming For Biology 2017
===========================


Instructors
============
Simon Prochnik  
Sofia Robb  
    
***

Table of Contents
 * [Big Picture](#big-picture)
 * [Unix](#unix)
     * [Unix Overview](#unix-overview)
     * [Getting Around](#getting-around)  
     * [Getting things done](#getting-things-done)
     * [Text Editors](#text-editors)
     * [Git for Beginners](#git-for-beginners)
  * [AWS](#aws)
     * [AWS Overview](#aws-overview)
  * [Python](#python)
     * [Python Overview](#python-overview)
     * [Running Python](#running-python)
     * [Syntax](#syntax)
     * [Variables, Types, etc](#variables-types-etc)
     * [Operators](operators)
     * [Logic: Control Statements](#logic-control-statements)
     * [Numbers](#numbers)
     * [Strings](#strings) 
     * [Tuples and Lists](#tuples-and-lists)
     * [Loops](#loops)
     * [Files: I/O](#files-io)
     * [Dictionaries and Sets](#dictionaries-and-sets)
     * [Functions](#functions)
     * [Modules](#modules)
     * [Exceptions](#exceptions)
     * [Classes](#classes) 
     * [Datastructures](#datastructures)
 * [BioPython](#biopython)
    * [BioPython Overview](#biopython-overview)
    * [BioPython Subtopic 1](#biopython-subtopic-1)
    * [BioPython Subtopic 2](#biopython-subtopic-2)
 * [My Questions](#my-questions)
 * [Bioinformatic Analysis and Tools](#bioinformatic-analysis-and-tools)
   * [Bioinformatic Analysis and Tools Overview](#bioinformatics-analysis-and-tools-overview)
   * [Sequence Search and Alignments](#sequence-search-and-alignments)
   * [Assembly](#assembly)
   * [NGS](#ngs)
   * [Variant Calling](#variant-calling)
   * [Ontology](#ontology)

  
  
***  


Big Picture
=======================
Why is it important for Biologists to learn to program?

***
# Unix
***

Unix Overview
=============
Note: I think it could work nicely if we  get prepaid visa credit cards for each student, $50 maybe. Then we can have each of them 

- create an account
- log in
- create and launch an instance
- ssh into instance


Getting Around  
==============
 - ls  
 - cd  
 - cp  
 - rm  
 - cat  
 - less/more  
 - grep  
 - wc
 - ssh
 - scp 


Getting things done
==================
 - sort
 - uniq
 - awk
 - sed
 - perl
 - for

Text Editors
============


Git for Beginners
=================


***
# AWS
***  



AWS Overview
============

Note: I think it would work nicely if we can get prepaid visa credit cards for each student, $50 maybe. Then we can have each of them 

- create an account
- log in
- create and launch an instance
- ssh into instance

  
  

***
# Python
***
  
  


Python Overview
===============
 * We are teaching the simplest form of the language, no 'clever' stuff.
 * We can expand on this in subsequent years

Functions and statements we are NOT covering
`assert`

Language basics: 3.x, interpreted, slow, python notebook eg jupyter


Running Python
==============  


Interactive Interpreter
-----------------------
Python can be run one line at a time in an interactive interpreter.  
To lauch the interpreter type the following into your terminal window:
`$ python`  
Note: '$' indicates the command line prompt  

First Python Script:
```bash
$ python
```  


```python
>>> print ("Hello, PFB2017!")
Hello, PFB2017!
```  



Script Programming
-----------------------
Calling the python commnad with a script name as an argument will cause the execution of the script.  

__Python Script__
* The same code from above is typed into a text file. 
* This file will have the extension .py. 

File Contents:  
```
#!/usr/bin/python3
print ("Hello, PFB2017!")
```  

Execute the Python script:
```bash
$ python test.py 
```

This produces the following result:
```bash
Hello, PFB2017!
```






Syntax
=======

@sep example code, statements, functions(), tab spacing, interactive interpreter, debugger

__Python Identifiers__: 
A Python identifier is a name used to identify a variable, function, class, module or other object. An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).

Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case sensitive programming language. Thus, seq_id and seq_ID are two different identifiers in Python.

__Naming conventions for Python Identifiers__: 
 * 1st character is lowercase, unless it is a name of a Class. Classes should begin with an uppercase characters. (ex. seq)
 * Private identifiers begin with an underscore. (ex. \_private)
 * Strong private identifiers begin with two underscores. (ex. \_\_private)
 * Language-defined special names begin and end with two underscores. (ex.\_\_special\_\_)

__Reserved Words__: 
The following is a list of Python keywords. These are special words that already have a purpose in python and therefore cannot be used in indentifier names.

```
and         exec        not
as          finally     or
assert      for         pass
break       from        print
class       global      raise
continue    if          return
def         import      try
del         in          while
elif        is          with
else        lambda      yield
except
```

__Lines and Indentation__: 
Python does not use braces({}) to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line indentation. Incorrect line spacing and indention will cause an error to be reported.

The number of spaces in the indentation need to be consistent but a specific number is not required. All lines of code, or statements, within a single block must be indented in the same way. For example:


__Comments__: 
Comments are a good programming practice. Making a note of what a line or block of code is doing will help the writer and readers of the code.

__#__ : 
The pound or hash symbol is used to prepend a comment. All characters after the # and to the end of the line are apart of the comment and it will not be interpreted. 
```python
#!/usr/bin/python3

# this is my first script
print ("Hello, PFB2017!") # this line prints
```


__Blank Lines__: 
Blank lines are also important for increasing the readability of the code. Blank lines are ignored by the interpreptor


__Python Options__: 
```bash
$ python -h
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser (also PYTHONDEBUG=x)
-E     : ignore environment variables (such as PYTHONPATH)
-h     : print this help message and exit
```






Variables, Types, etc
=====================
overview of all types: start with constants: numbers, strings '' "" ''' ''' r'' = raw strings, + for concat, * for repeat
iterable, string, int, float, tuple, list, dictionary, set


Operators
==========
These depend on the type of variable, so revisit the most relevant ones in subsequent sections
include // floor division and % modulus


Logic: Control Statements
=========================
while, if, elif, else, break, continue, 
ugh: else in while loop


Numbers
========


Strings
========
.format()
strip()


__Quotation Marks__
Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.

The triple quotes are used to span the string across multiple lines. For example, all the following are allowed:

word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""


Tuples and Lists
===============
append(x), .extend(iter) pop() insert() sort() reverse()
list comprehension 
`squares = [x**2 for x in range(10)]`
zip() -- loop over two lists at the same time
iterators: next(), generators


Loops
=====
for i in list: 
(ugh: else in for loop)
iterators, range()


Files: I/O
==========
with open() as f:
open()
read() readline()
write()
close()


Dictionaries and Sets
======================
for k, v in knights.items():
keys()


Functions
=========
`def, return, positional arguments, keyword arguments, *arguments **keywords`
lambda e.g.
`squares = list(map(lambda x: x**2, range(10)))`


Modules
=======
dir()
import
from bla import boo


The standard library:
os, sys, glob, shutil, math, random, statistics (scipy), zlib, sqlite3 (DB access)? urllib.request 


Regular Expressions
====================



Exceptions
==========
try/except/finally (see with/as)



Classes 
=======
`class`
scope & namespace, 
`global, nonlocal`



Datastructures
==============
import json


***
# BioPython
***


BioPython Overview
==================


BioPython Subtopic 1
--------------------


BioPython Subtopic 2
--------------------


My Questions
============


***
# Bioinformatic Analysis and Tools
***


Bioinformatic Analysis and Tools Overview
========================================
  * What you want to do:
      * tools to do it



Sequence Search and Alignments
==============================



Assembly
========

DNA
----

RNA
----



NGS
===




Variant Calling
===============




Ontology
========

