#!/usr/bin/env python3


## Problem 1

# Take a multi-FASTA Python_08.fasta file from user input and calculate the nucleotide composition for each sequence. Use a datastructure to keep count. Print out each sequence name and its compostion in this format seqName\tA_count\tT_count\tG_count\C_count

## Plan:
## - Bring the FASTA file in and iterate over each line

## For each FASTA record I want to: 
## - See if the line begins with ">", and save that as my sequence ID
## - Initialize a dictionary for my sequence compositions with my sequence ID
## - Add a count to my sequence composition dictionary for each type of nucleotide 
## - Create a second dictionary to sum all of the lengths of the sequence lines

## Once I have the nucleotide and sequence lengths in a dictionary
## - I want to move through each unique sequence ID and calculate the nucleotide percentage by dividing the count of each nucleotide by the total length of the sequence
## - print a tab delimited table with my nucleotide compositions

## import sys to pull files in from the command line
import sys

## create a handle for our file
fasta = open(sys.argv[1], 'r')





 ## initialize our sequence lengths and sequence composition dictionaries
seq_lens = {}
seq_comp = {}

## initialize an index to help us bookmark our position along the sequence
seq_index = 0


for line in fasta:
    if line.startswith('>'):     ## if we have a sequence identifier, continue
        tx_id = line[1:].strip() ## remove the end characters
        seq_comp[tx_id] = {}     ## initialize nucleotide composition dictionary
        seq_index = 0            ## initialize/reinitialize a sequence count for each new sequence ID
    else:
        seq = line.strip().upper() ## remove the end characters and make all the sequence upper case
        
        ## count all of the unique nucleotides
        A_comp = seq.count('A')
        T_comp = seq.count('T')
        G_comp = seq.count('G')
        C_comp = seq.count('C')
        
        ## if this is the first sequence line, initialize the count of each nucleotide in our dictionary and the length of the first part of our sequence
        if seq_index == 0:
            seq_index = 1                 ## Bookmark our position to tell our loop that we are after the first 'sequence line'
            ## initalize dictionaries with initial lengths
            seq_lens[tx_id] = len(seq)   
            seq_comp[tx_id]['A'] = A_comp
            seq_comp[tx_id]['T'] = T_comp
            seq_comp[tx_id]['G'] = G_comp
            seq_comp[tx_id]['C'] = C_comp

        ## if this is not the first sequence line, add the count of each nucleotide to our dictionary
        else:
            seq_lens[tx_id] = seq_lens[tx_id] + len(seq) ## increment our sequence length
            seq_comp[tx_id]['A'] += A_comp               ## increment each count
            seq_comp[tx_id]['T'] += T_comp
            seq_comp[tx_id]['G'] += G_comp
            seq_comp[tx_id]['C'] += C_comp


 
## for each unique sequence ID, iterate through our keys, pull out the values for each nucleotide and divide them by the total sequence length
for tx_id in seq_comp:
    seq_comp[tx_id]['A'] = seq_comp[tx_id]['A']/seq_lens[tx_id]                 
    seq_comp[tx_id]['T'] = seq_comp[tx_id]['T']/seq_lens[tx_id]
    seq_comp[tx_id]['G'] = seq_comp[tx_id]['G']/seq_lens[tx_id]
    seq_comp[tx_id]['C'] = seq_comp[tx_id]['C']/seq_lens[tx_id]          

## Print our results with a header and tab delimitations

print("\t".join(['TranscriptID', 'A_content', 'T_content', 'G_content', 'C_content']))

for tx_id in seq_comp:
    print(tx_id, "\t", seq_comp[tx_id]['A'], "\t", seq_comp[tx_id]['T'], '\t', seq_comp[tx_id]['G'], '\t', seq_comp[tx_id]['C'])
    



## close our fasta file
fasta.close()
