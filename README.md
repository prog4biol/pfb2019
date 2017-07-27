# PFB2017

## Why we had to switch to an inferior language


# Bioinformatics
### [Bioinformatics Overview](bioinfo_0.md)

# Unix
### [Unix Overview](unix_0.md)
### [Getting Around](unix_1.md)
### [Getting things done](unix_2.md)
### [Text Editors](texteditors_0.md)
### [Git for Beginners](git_0.md)

# AWS
### [AWS Overview](aws_0.md)

# Python

# We are teaching the simplest form of the language, no 'clever' stuff.
# We can expand on this in subsequent years

## Functions and statements we are NOT covering
`assert`

### [Python Overview](python_overview.md)
Language basics: 3.x, interpreted, slow, python notebook eg jupyter

### [Syntax](python_syntax.md)
example code, statements, functions(), tab spacing, interactive interpreter, debugger

### [Variables, Types etc](python_variables.md)
overview of all types: start with constants: numbers, strings '' "" ''' ''' r'' = raw strings, + for concat, * for repeat
iterable, string, int, float, tuple, list, dictionary, set
### [Operators](python_operators.md)
These depend on the type of variable, so revisit the most relevant ones in subsequent sections
include // floor division and % modulus

### [Logic: Control Statements](python_logic.md)
while, if, elif, else, break, continue, 
ugh: else in while loop
### [Numbers](python_numbers.md)
### [Strings](python_strings.md)
.format()
strip()

### [Tuples and Lists](python_tuples.md)
append(x), .extend(iter) pop() insert() sort() reverse()
list comprehension 
`squares = [x**2 for x in range(10)]`
zip() -- loop over two lists at the same time
iterators: next(), generators

### [Loops](python_loops.md)
for i in list: 
(ugh: else in for loop)
iterators, range()

### [Files: I/O](python_files.md)
with open() as f:
open()
read() readline()
write()
close()

### [Dictionaries and Sets](python_dict.md)
for k, v in knights.items():
keys()

### [Functions](python_functions.md)
`def, return, positional arguments, keyword arguments, *arguments **keywords`
lambda e.g.
`squares = list(map(lambda x: x**2, range(10)))`


### [Modules](python_modules.md)
dir()
import
from bla import boo


### The standard library
os, sys, glob, shutil, math, random, statistics (scipy), zlib, sqlite3 (DB access)? urllib.request 
### [Regular Expressions](python_regex.md)

### [Exceptions](python_exceptions.md)
try/except/finally (see with/as)

### Classes 
`class`
scope & namespace, 
`global, nonlocal`
### [Datastructures](python_datastructures.md)
import json
### [BioPython](python_biopyton.md)
### [My Questions](python_questions.md)

# Bioinformatic Topics
### Sequence Search and Alignments
### Assembly (DNA/RNA)
### NGS
### Variant Calling
### Ontology
### Bioinformatics Projects (GMOD)



