#!/usr/bin/env python3

# Write a script that takes a multi-FASTA file Python_08.fasta from user input and breaks each sequence into codons (every three nucleotides is a codon) in just the first reading frame. Your output should look like this
# seq1-frame-1-codons
# CAT GCT TGA GTC


## Plan:

## - Bring the FASTA file in and iterate over each line

## For each FASTA record I want to:
## - See if the line begins with ">", and save that as my sequence ID
## - Initialize a dictionary for my sequence compositions with my sequence ID
## - Add my FASTA sequences to my dictionary so I can use them later
## - Print out the first frame of codons for each sequence



## import sys to pull files in from the command line
import sys

## create a handle for our file
fasta = open(sys.argv[1], 'r')


## initialize our sequence dictionary
seqs = {} 


## parse a fasta file

for line in fasta:
    if line.startswith('>'):       ## if we have a sequence identifier, continue
        id = line[1:].strip()      ## remove the end characters on either end
        seq_index = 0              ## initialize a sequence count to bookmark my position
    else:
        seq = line.strip().upper() ## remove the end characters and make all upper case
        if seq_index == 0:
            seqs[id] = seq ## put the first line of sequence into the dictionary
            seq_index = 1  ## tell our loop we are past the first sequence
        else:
            seqs[id] = seqs[id] + seq ## add on any sequences following


## find the codons


## initialize a counter to keep track of how many nucleotides we have looked at
nuc_index = 0 

## iterate over our FASTA dictionary

for seq_id in seqs:
    sequence = seqs[seq_id]  ## pull out our sequence
    codons = []              ## initialize a list to store our codons
    codon_temp = ''          ## initialize a string to store our 3 nucleotides
    nuc_index = 0            ## reinitialize our counter for each unique sequence id
    ## for each nucleotide in our sequence
    for nucleotide in sequence:
        ## if our counter is less than or equal to 2 (remember python counts 0, 1, 2)
        if nuc_index <= 2:
            codon_temp = codon_temp + nucleotide ## add a nucleotide to our codon string
            nuc_index += 1 ## increment our counter by one
        ## if we have counted 3 and added 3 nucleotides to our string
        else:
            codons.append(codon_temp) ## add our single codon to our codons list
            codon_temp = ''           ## reinitialize our codon string
            nuc_index = 0             ## reinitialize our counter
            
    ## once we have made it through the whole sequence
    print(seq_id + '-frame-1-codons') ## print our an ID for our first frame of codons
    print(" ".join(codons))           ## join and print our list of codons


## close our fasta file
fasta.close()

