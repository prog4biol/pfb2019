# PFB2017

## Why we had to switch to an inferior language


 * [Bioinformatics Overview](#bioinformatics-overview)
 * Unix
     * [Unix Overview](#unix-overview)
     * [Getting Around](#getting-around)  
     * [Getting things done](#getting-things-done)
     * [Text Editors](#text-editors)
     * [Git for Beginners](#git-for-beginners)
  * AWS
     * [AWS Overview](#aws-overview)
  * Python
     * [Python Overview](#python-overview)
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
 * BioPython
    * [BioPython Overview](#biopython-overview)
    * [BioPython Subtopic 1](#biopython-subtopic-1)
    * [BioPython Subtopic 2](#biopython-subtopic-2)
 * [My Questions](#my-questions)
 * [Bioinformatics Analysis and Tools](#bioinformatic-analysis-and-tools)
 * [Sequence Search and Alignments](#sequence-search-and-alignments)
 * [Assembly](#assembly)
 * [NGS](#ngs)
 * [Variant Calling](#variant-calling)
 * [Ontology](#ontology)




Bioinformatics Overview
=======================

Unix
=====
Unix Overview
-------------

Getting Around  
--------------

Getting things done
-------------------

Text Editors
------------

Git for Beginners
-----------------


AWS Overview
============


Python Overview
===============
 * We are teaching the simplest form of the language, no 'clever' stuff.
 * We can expand on this in subsequent years

Functions and statements we are NOT covering
`assert`

Language basics: 3.x, interpreted, slow, python notebook eg jupyter


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



BioPython Overview
==================

BioPython Subtopic 1
--------------------


BioPython Subtopic 2
--------------------


My Questions
============


Bioinformatics Analysis and Tools
================================
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

