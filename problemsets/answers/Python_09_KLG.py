#!/usr/bin/env python3
# Python 9 - Exceptions -Problem Set
# ===================


# 1. Add in exception handling to a script from Problem Set 8 or any script you have written that uses I/O to open and read a FASTA file. 
   
#    Throw and handle (try/except) the exception
#    - if no input is provided  
#    - if the file cannot be opened
#    - if the file does not end in '.fasta' or '.fa' or '.nt'
#    - if a non ATGCN charcter is found in the sequence

## I'm going to add some error handling to a fasta parser that prints the fasta to the screen in the tabular format "seqid\tsequence"

import re
import sys

## This is an easy way to try/except if something fails to run
try:
    in_file = sys.argv[1] # if no input is provided
except:
    print('No input provided')
    sys.exit(1) ## make sure you have the 1 to return an error code



## Here's an example of how to define your own error class
## this can come in handy if you want to check for the same error over and over again
class NotFASTAError(Exception):
  pass
    
try:
    ## has the extension that we want
    if not in_file.split(".")[-1] in ["nt", "fasta", "fa"]:
         raise NotFASTAError
     
except NotFASTAError:
    print("File needs to end with [fa, nt, fasta], is this a fasta file?")
    sys.exit(1)
    
try:
    fasta_file= open(in_file, 'r') ## try to open the file, if we can't open it the user likely hasn't provided an input. Exit from the script. 
except:
    print('Cannot open file')
    sys.exit(1)


seq_dict = {}
for line in fasta_file:
    line = line.rstrip()
    match = re.match(r'>(\S+)', line)
    if match:
        seqid = match.group(1)
        seq_dict[seqid] = ''
    else:
        for nucleotide in line:
            if nucleotide not in ['A', 'T', 'G', 'C', 'N']:
                raise Exception(("Offending nucleotide", nucleotide, "not one of ['A', 'T', 'G', 'C', 'N']")) ## this is a way to raise an anonymous exception the fly
                sys.exit(1)
        seq_dict[seqid] += line

## print out to columns/tab delimited format
for seq_id in seq_dict:
    print(seq_id, seq_dict[seq_id], sep = "\t")


    
