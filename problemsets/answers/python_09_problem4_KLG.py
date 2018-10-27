#!/usr/bin/env python3


## Problem 4
# Modify your script so that it can take two command line arguments:

# FASTA file name
# Max length of each line
# The script should reformat every sequence in the file to the specified max line length. Make sure your output is in proper FASTA format. 



import re
import sys

fasta = open(sys.argv[1], 'r')
length = int(sys.argv[2])


## Define my function
def format_dna(dna, length):
    ## A function to format a string of DNA so that each line is no more than 60 nt long.
    ## remove the newlines
    dna = re.sub("\n", "", dna)
    count = 0 ## initialize a count to count each nucleotide
    line = '' ## initialize a string to hold our nucleotides
    lines = [] ## initialize a list to hold our nt strings
    ## interate over the string of DNA
    for nuc in dna:
        if count < length: ## if our count is less than 'length'
            line += nuc ## extend our string
        else: ## otherwise
            lines.append(line) ## add our nt line to our list
            line = '' ## reset our string
            count = 0 ## reset our count
        
        count += 1 ## increment count after each nucleotide has passed through the loop
    ## the last line is short, so we add it after the loop
    lines.append(line)    
    ## join our list together and print it out
    return("\n".join(lines))


###############DONE WITH MY FUNCTION DEFINITION, running code ################


## first parse the file

fasta_seq = '' ## initialize a string to hold the sequence

## iterate over the fasta
for record in fasta:
    reco = record.strip()    ## remove the newlines 
    if reco.startswith('>'): ## if we have a sequence identifier, continue
        if fasta_seq != '':  ## if we have a sequence in our string, print it
            ## prints the sequence for the record above the one we are on
            print(format_dna(dna = fasta_seq, length = length))
        print(reco)          ## print the header
        fasta_seq = ''       ## reset the sequence string
    else:
        fasta_seq += reco    ## add each next line to the string 

## print out the last string that was left uncaptured by the loop
print(format_dna(dna = fasta_seq, length = length))

            




