#!/usr/bin/env python3

# Problem 3

# Add in exception handling. Throw and handle (try/except) the exception
## - if no input is provided
## - if the file cannot be opened
## - if the file does not end in '.fasta' or '.fa' or '.nt'
## - if a non ATGCN character is found in the sequence

## Plan:

## I have never used try/except, so I need to learn it in lecture and implement
## Try/excepts make the code cleaner for the end user by hiding the ugly stack trace


## import sys to pull files in from the command line
import sys


## make lists to tell our program what types of things we will accept from our fastas
fasta_extensions = ['fasta', 'fa', 'nt']
nucleotides      = ['A', 'T', 'C', 'G', 'N']


## define some error handlers
class NotFASTAError(Exception):
  pass

class NotNucleotidesError(Exception):
  pass


## First open our FASTA file only if it...
try:
    fasta = str(sys.argv[1])
    ## has the extension that we want
    if not fasta.split(".")[-1] in fasta_extensions:
         raise NotFASTAError
    ## try to open our file
    fasta = open(sys.argv[1], 'r')

## Print my FASTA exception
except NotFASTAError:
    print("File needs to be a FASTA file and end with fa or nt or fasta")
    sys.exit(1)

## Print my index error if there isn't a new file
except IndexError:
    print("Please provide an infile")
    sys.exit(1)  # abort

## our last exception
except:
    print('Your fasta file cannot be opened!')
    sys.exit(1)  # abort




seqs = {} ## initialize our sequence dictionary


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
        ## if it isn't an acceptable nucleotide, throw our last exception
        if nucleotide not in nucleotides:
          raise Exception('Nucleotides not one of "A/T/G/C"')
          sys.exit(1)
        ## if our counter is less than or equal to 2 (remember python counts 0, 1, 2)
        if nuc_index <= 2:
          codon_temp = codon_temp + nucleotide ## add a nucleotide to our codon string
          nuc_index += 1 ## increment our counter by one
        else:
          codons.append(codon_temp) ## add our single codon to our codons list
          codon_temp = '' ## reinitialize our codon string
          nuc_index = 0 ## reinitialize our counter

    ## once we have made it through the whole sequence    
    print(seq_id + '-frame-1-codons') ## print our an ID for our first frame of codons
    print(" ".join(codons)) ## join and print our list of codons

## close our fasta file
fasta.close()
