#!/usr/bin/env python3

# Python 6 - IO - Problem Set
# ===================

# 2. Modifiy the script in the previous problem to write the contents to a new file called "Python_06_uc.txt"

in_file = open('Python_06.txt', 'r')
out_file = open('Python_06_uc.txt', 'w')

for line in in_file:
    new_line = line.strip().upper() ## strip whitespace and uppercase the line
    out_file.write(new_line + "\n")
