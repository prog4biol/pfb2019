#!/usr/bin/env python3

# Problem 4

# Now produce codons in the first three reading frames for each sequence and print out ids and sequence records for each frame and print to a file called 'Python_08.codons-3frames.nt'



## import sys to pull files in from the command line
import sys

## I'm going to use a regex later
import re

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


## I'm done with this file, so I'll just close it now
fasta.close()


## open the file I will write my answer to
f_out = open('output/Python_08.codons-3frames.nt', 'w')


## Here I'm doing something a little different from the last question.

## find the codon frames

## iterate over our FASTA dictionary

for seq_id in seqs:
    sequence = seqs[seq_id] ## pull out our sequence
    for nucleotide in sequence:
        if nucleotide not in nucleotides:
          raise Exception('Nucleotides not one of "A/T/G/C"')
          sys.exit(1)

    ## I was sitting in the regex lecture, and Sofia had this example to pull out codons.
    ## I had to use it immediately because it is so clever.
    codons_1 = re.findall(r"(.{3})", sequence) ## from lecture example
    ## Now I subset my starting sequence to remove the first nucleotide, then I regex out the codons
    codons_2 = re.findall(r"(.{3})", sequence[1:len(sequence)])
    ## Now I subset my starting sequence to remove the first and second nucleotides, then I regex out the codons
    codons_3 = re.findall(r"(.{3})", sequence[2:len(sequence)])

    ## write everything as I go through the dictionary
    
    ## first codon frame
    f_out.write(">" + seq_id + '-frame-1-codons\n')
    f_out.write(" ".join(codons_1))

    ## second codon frame
    f_out.write(">" + seq_id + '-frame-2-codons\n')
    f_out.write(" ".join(codons_2) + "\n")

    ## third codon frame
    f_out.write(">" + seq_id + '-frame-3-codons\n')
    f_out.write(" ".join(codons_3) + "\n")

## close the file I wrote to
f_out.close()
