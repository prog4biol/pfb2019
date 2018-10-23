#!/usr/bin/env python3

# Problem 5

# Now reverse complement each sequence and print out all six reading frames to a file called 'Python_08.codons-6frames.nt'

## import the libraries I will use
import sys
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
f_out = open('output/Python_08.codons-6frames.nt', 'w')


## Now that I have my sequences stored, I want to find all of the codon frames.
## I plan to use regular expressions and loop over a range from 0:3 to slice my sequence as I go



for seq_id in seqs:         ## iterate over our FASTA dictionary
  
    sequence = seqs[seq_id] ## pull our sequence out of the dictionary

    ## Code to find the reverse complement stolen from other TA's answersets
    DNA = sequence.lower()
    DNA_comp= DNA.replace('a', 'T').replace('c','G').replace('g', 'C').replace('t','A')
    sequence_rev = DNA_comp[::-1]
    
    for nucleotide in sequence:
        if nucleotide not in nucleotides:
          raise Exception('Nucleotides not one of "A/T/G/C"')
          sys.exit(1)
          
    ## To keep this more readable I will loop over a range to pull out
    ## three forward frames and three reverse frames
    
    for i in range(0, 3): 

      ## use regular expressions to pull out each reading frame
      ## here I'm subsetting the sequence starting with 'i' in our range
      ## 'i' will increment after each interation
      ## this will cut off 0, then 1, then 2 nucleotides to progressively shift the frame
      codons_f = re.findall(r"(.{3})", sequence[i:len(sequence)])
      codons_r = re.findall(r"(.{3})", sequence_rev[i:len(sequence)])

      ## create strings for writing out 'biologically relevant' sequence ids
      f_i = str('foward_' + str((i+1)))
      r_i = str('reverse_' + str((i+1)))

      ## write the codons to files
      ## think about how I could put these in a nicer order ::wink::
      
      ## forward
      f_out.write(">" + seq_id + '-frame-' + f_i + '-codons\n')
      f_out.write(" ".join(codons_f) + "\n")

      ## reverse
      f_out.write(">" + seq_id + '-frame-' + r_i + '-codons\n')
      f_out.write(" ".join(codons_r) + "\n")


    
## close all open files
f_out.close()
fasta.close()
    
