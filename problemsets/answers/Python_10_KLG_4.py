#!/usr/bin/env python3
# Python 10 - Functions - Problem Set
# ===================

import re
import sys

# 4. Modify your script so that it can take two command line arguments:
#      1) FASTA file name
#      2) Max length of each line

#    The script should reformat every sequence in the file to the specified max line length. Make sure your output is in proper FASTA format.


fa_file = open(sys.argv[1], 'r')
width = sys.argv[2]
 
def nuc_wrap(dna, width):
    dna = re.sub("\n", "", dna)
    regex = re.compile("\w{1," + str(width) + "}") ## precompile our regular expression
    nuc_strings = regex.findall(dna)
    [print(x) for x in nuc_strings]


## write a little fasta parser so we can run our wrapper on the sequences

seq_dict = {}
for line in fa_file:
    line = line.rstrip()
    match = re.match(r'>(\S+)', line)
    if line.startswith(">"):
        seq_id = line
        seq_dict[seq_id] = ''
    else:
        seq_dict[seq_id] += line


for key in seq_dict:
    print(key)
    nuc_wrap(dna = seq_dict[key], width = width)

        
