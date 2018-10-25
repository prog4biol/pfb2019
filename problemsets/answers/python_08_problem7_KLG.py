#!/usr/bin/env python3

# Problem 7

# Find the longest peptide sequence (M-->Stop) of all the six translated reading frames for a single sequence. Do this for all the sequence records. For each sequence, print out in FASTA format the six frames of codons to one file (Python_08.codons-6frames.nt), the translations to a second file (Python_08.translated.aa), and the single longest translated peptide to a third file (Python_08.translated-longest.aa).


## Plan:
## I want to find the first 'M' to define the start of my amino acid sequence
## After I find M, I can look fo '*' to find the stop directly after the M
## I will use a regex to find the first M
## Then I will loop over my sequence to look for the '*' directly after the M
## within my loop, I will keep track of my position with an counter 

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
    if line.startswith('>'):  ## if we have a sequence identifier, continue
        id = line[1:].strip() ## remove the end characters on either end
        seq_index = 0         ## initialize a sequence count
    else:
        seq = line.strip().upper() ## remove the end characters and make all upper cas
        if seq_index == 0:
            seqs[id] = seq  ## put the first line of sequence into the dictionary
            seq_index = 1   ## next
        else:
            seqs[id] = seqs[id] + seq ## add on any subsequence sequences


fasta.close()

## find the codon frames

## open our outfiles
f_nt_out     = open('output/Python_08.codons-6frames.nt', 'w')
f_aa_out     = open('output/Python_08.translated.aa', 'w')
f_longest_aa = open('output/Python_08.translated-longest.aa', 'w')




## loop over our dictionary of sequences

for seq_id in seqs:
    sequence = seqs[seq_id] ## pull our sequence out of the dictionary

    
    for nucleotide in sequence:
        if nucleotide not in nucleotides:
          raise Exception('Nucleotides not one of "A/T/G/C"')
          sys.exit(1)

    ## Code to find the reverse complement
    DNA = sequence.lower()
    DNA_comp= DNA.replace('a', 'T').replace('c','G').replace('g', 'C').replace('t','A')
    sequence_rev = DNA_comp[::-1]

        
    aa_list = [] ## initialize a list to store our amino acid coding sequences
    ## iterate over the possible forward and reverse reading frames
    for i in range(0, 3):


      ## use regular expressions to pull out each reading frame
      codons_f = re.findall(r"(.{3})", sequence[i:len(sequence)])
      codons_r = re.findall(r"(.{3})", sequence_rev[i:len(sequence)])

      ## keep our frame strings for writing out 'biological taxonomically relevant' 
      f_i = str('foward_' + str((i+1)))
      r_i = str('reverse_' + str((i+1)))


      ## write the codons to files
      f_nt_out.write(">" + seq_id + '-frame-' + f_i + '-codons\n')
      f_nt_out.write("".join(codons_f) + "\n")
      f_nt_out.write(">" + seq_id + '-frame-' + r_i + '-codons\n')
      f_nt_out.write("".join(codons_r) + "\n")

      ## amino acid operations
      ## perform a list comprehension on both of the codon translations.
      ## this succinct version of a for loop will retrieve all of the the translation table values for our codons
      aa_f = [translation_table.get(x) for x in codons_f]
      aa_r = [translation_table.get(x) for x in codons_r]

      ## append my amino acid sequences to a list to find the longest one later
      aa_list.append(aa_f)
      aa_list.append(aa_r)
      
      ## write out amino acids

      f_aa_out.write(">" + seq_id + '-frame-' + f_i + '-amino_acids\n')
      f_aa_out.write("".join(aa_f) + "\n")
      f_aa_out.write(">" + seq_id + '-frame-' + r_i + '-amino_acids\n')
      f_aa_out.write("".join(aa_r) + "\n")

      
    ## initialize a list to store our coding sequences   
    aa_coding = []
    for seq in aa_list:   ## iterate over our amino acid translations
      seqn = "".join(seq) ## make our amino acid translations strings for regex searches
      ## search for the first start amino acid
      start_finder = re.search("M", seqn)

      ## if we have values for both the start and stops continue
      if start_finder:
        aa_start = int(start_finder.start())
        ## this one searches for our first stop codon by looping through the sequences and looking for the first one after the start codon
        aa_stop = int()               ## initialize a variable to hold our stop value
        index = 0                     ## initialize a count as we go across the sequence
        stop_temp = int()             ## initialize a variable to hold the current stop 
        for nt in seqn:   
          if nt == '*':               ## if we have a stop value
            stop_temp = index         ## set our temporary value
          if stop_temp > aa_start:    ## if the temp value is greater than the start position
            aa_stop = stop_temp       ## assign our stopping point
            break                     ## I have the stop, so break
          index += 1                  ## increment the position in the sequence
          
        if aa_stop:
          #print(aa_start, aa_stop) ## check the starts and stops
          if(aa_stop - aa_start > 0):## if the amino acid is a real length, continue
            aa_coding.append(seqn[aa_start:aa_stop]) ## append the coding sequence to the list
    # find the length of all of our coding sequences

    coding_lens = [len(x) for x in aa_coding]
    ## pull the index out for the longest coding sequence
    longest_aa = aa_coding[coding_lens.index(max(coding_lens))]                                              
    ## write out everything that we want
    f_longest_aa.write(">" + seq_id + "\n") 
    f_longest_aa.write(longest_aa + "\n")

      
        
          



    
      

## close all open files
fasta.close()
f_nt_out.close()
f_aa_out.close()
f_longest_aa.close()
