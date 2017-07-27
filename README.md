Programming For Biology 2017
===========================


Instructors
============
 * Simon Prochnik
 * Sofia Robb  
    



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




Big Picture
=======================
Why is it important for Biologists to learn to program?

***
# Unix
***

Unix Overview
=============


Getting Around  
==============


Getting things done
==================


Text Editors
============


Git for Beginners
=================


***
# AWS
***


AWS Overview
============


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
To lauch the interpreter type the followin into your terminal window:

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



example code, statements, functions(), tab spacing, interactive interpreter, debugger


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

