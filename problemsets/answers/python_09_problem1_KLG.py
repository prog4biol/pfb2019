#!/usr/bin/env python3


## Problem 1

## Create a function to format a string of DNA so that each line is no more than 60 nt long.
## INPUT: a string of DNA without newlines
## RETURNS: a string of DNA with lines no more than 60 nucleoties long


### PLAN:
### - I decided to make a function because I was going to copy and paste a some code
### - I instead put the code into a function so I can easily reuse it over and over again
### - To repeat, I first wrote the code for the function and tested it with a tiny test set
### - Once I knew it would work, and I could easily reuse it, a made it a function


dna='GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'


## Define my function
def format_dna(dna):
    ## A function to format a string of DNA so that each line is no more than 60 nt long.
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
