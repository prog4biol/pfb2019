#!/usr/bin/env python3

# Problem 6

# Translate each of the six reading frames into amino acids. Create one file for which you print the six reading frames (Python_08.codons-6frames.nt) and one file for which you print the translation of the six reading frames (Python_08.translated.aa).


## import the libraries I will use
import sys
import re

## make lists to tell our program what types of things we will accept from our fastas
fasta_extensions = ['fasta', 'fa', 'nt']
nucleotides      = ['A', 'T', 'C', 'G', 'N']



## initialize a translation table
translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}







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

## find the codon frames

## open our files
f_nt_out = open('output/Python_08.codons-6frames.nt', 'w')
f_aa_out = open('output/Python_08.translated.aa', 'w')



## iterate over our FASTA dictionary

for seq_id in seqs:
    sequence = seqs[seq_id] ## pull our sequence out of the dictionary

    ## Code to find the reverse complement
    DNA = sequence.lower()
    DNA_comp= DNA.replace('a', 'T').replace('c','G').replace('g', 'C').replace('t','A')
    sequence_rev = DNA_comp[::-1]
    codon_temp = ''
    nuc_index = 0
    
    for nucleotide in sequence:
        if nucleotide not in nucleotides:
          raise Exception('Nucleotides not one of "A/T/G/C"')
          sys.exit(1)

    ## To keep this more readable I will loop over a range to pull out
    ## three forward frames and three reverse frames
    
    for i in range(0, 3):## iterate over the possible forward and reverse reading frames


      ## use regular expressions to pull out each reading frame
      codons_f = re.findall(r"(.{3})", sequence[i:len(sequence)])
      codons_r = re.findall(r"(.{3})", sequence_rev[i:len(sequence)])


      ## create strings for writing out 'biologically relevant' sequence ids
      f_i = str('foward_' + str((i+1)))
      r_i = str('reverse_' + str((i+1)))

      ## write the codons to files
      f_nt_out.write(">" + seq_id + '-frame-' + f_i + '-codons\n')
      f_nt_out.write(" ".join(codons_f) + "\n")
      f_nt_out.write(">" + seq_id + '-frame-' + r_i + '-codons\n')
      f_nt_out.write(" ".join(codons_r) + "\n")

      ## amino acid operations
      ## perform a list comprehension on both of the codon translations.
      ## this succinct version of a for loop will retrieve all of the the translation table values for our codons using the dicionary method 'dict.get(key)'
      aa_f = [translation_table.get(x) for x in codons_f]
      aa_r = [translation_table.get(x) for x in codons_r]

      ## write out amino acids

      f_aa_out.write(">" + seq_id + '-frame-' + f_i + '-amino_acids\n')
      f_aa_out.write("".join(aa_f) + "\n")
      f_aa_out.write(">" + seq_id + '-frame-' + r_i + '-amino_acids\n')
      f_aa_out.write("".join(aa_r) + "\n")
      

## close all open files
fasta.close()
f_nt_out.close()
f_aa_out.close()
