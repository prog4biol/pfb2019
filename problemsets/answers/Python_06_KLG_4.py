#!/usr/bin/env python3

# Python 6 - IO - Problem Set
# ===================

# 4. Open the [FASTQ](https://en.wikipedia.org/wiki/FASTQ_format) file [Python_06.fastq](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_06.fastq) and go through each line of the file. Count the number of lines and the number of characters per line. Have your program report the:  
#     - total number of lines  
#     - total number of characters  
#     - average line length   

in_file = open('Python_06.fastq', 'r')

lines      = 1
characters = 1
line_lens = []
for line in in_file:
    line = line.strip() ## strip whitespace and uppercase the line
    lines += 1
    characters += len(line)
    line_lens.append(len(line))

print('Total lines:', str(lines))
print('Total characters:', str(characters))
print('Average line length:', str(sum(line_lens)/len(line_lens)))
