#!/usr/bin/env python3


## Problem 2

## Modify your function so that it will work whether the DNA string does or does not have newlines.


import re


dna='''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

## Define my function
def format_dna(dna):
    ## A function to format a string of DNA so that each line is no more than 60 nt long.
    ## remove the newlines
    dna = re.sub("\n", "", dna)
    count = 0 ## initialize a count to count each nucleotide
    line = '' ## initialize a string to hold our nucleotides
    lines = [] ## initialize a list to hold our 60 nt strings
    ## interate over the string of DNA
    for nuc in dna:
        if count < 60: ## if our count is less than 60
            line += nuc ## extend our string
        else: ## otherwise
            lines.append(line) ## add our 60 nt line to our list
            line = '' ## reset our string
            count = 0 ## reset our count
        
        count += 1 ## increment count after each nucleotide has passed through the loop
    ## the last line is short (>60nt), so we add it after the loop
    lines.append(line)    
    ## join our list together and print it out
    return("\n".join(lines))



###############DONE WITH MY FUNCTION DEFINITION, running code ################

## print out the result
print(format_dna(dna))
