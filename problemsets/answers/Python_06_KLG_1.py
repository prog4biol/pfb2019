#!/usr/bin/env python3

# Python 6 - IO - Problem Set
# ===================

# 1. Write a script to do the following to [Python_06.txt](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_06.txt)
#    - Open and read the contents.  
#    - Uppercase each line
#    - Print each line to the STDOUT

in_file = open('Python_06.txt', 'r')

for line in in_file:
    print(line.strip().upper()) ## strip whitespace and uppercase the line
