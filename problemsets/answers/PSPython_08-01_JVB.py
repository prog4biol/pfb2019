#!/usr/bin/env python3

# Python 08, problem 1
# ====================
# Take a mulit-FASTA Python_08.fasta file from user input and
# calculate the nucleotide composition for each sequence. Use
# a datastructure to keep count. Print out each sequence name
# and its compostion in this format
#  seqName\tA_count\tT_count\tG_count\C_count


# In order to receive data in the script, given by the user
# from the command line, we need to first make sure we import
# the sys module to access information from the outside system
import sys


# Remember that sys.argv's first position (index 0) contains
# the script name, but we want the second position (index 1).
fasta_filename = sys.argv[1]
fasta_filehandle = open(fasta_filename, 'r') 

# The problemset gives us the hint to use a nested data
# strucure of the form `seqs[geneName][nucleotide]=count`,
# which uses keys for both levels, so we need to use
# dictionaries:
sequence_composition = dict()

# Because python reads files line-by-line, and fasta sequences
# are arranged after their sequence IDs on different lines
# (and not the same lines as the IDs), we need to initialize
# a global variable in order for our script to "remember" which
# sequence ID we are working with when we get to each sequence
# line
sequence_id = None

# In order to iterate over all sequences in our file, use a
# "for" loop to read line-by-line:
for line in fasta_filehandle:
    line = line.rstrip()  # strip of ending \n char

    if line.startswith('>'):
        # ...then it's a sequence definition/description line
        # and the first set of non-whitespace characters is the
        # sequence ID; everything after the first whitespace
        # represents the sequence comment/description:
        sequence_def = line.lstrip('>').split(' ', maxsplit=1)
        sequence_id = sequence_def[0]
        
        # if the sequence is not yet in the sequence_composition
        # dict-of-dicts, then we need to add it's id as the key,
        # and another dict as its value:
        sequence_composition[sequence_id] = {
            'A': 0,
            'T': 0,
            'G': 0,
            'C': 0
        }
            
    else:
        # this is a sequence line, so let's iterate over each
        # nucleotide and count which kind it is:
        for nucleotide in line:
            sequence_composition[sequence_id][nucleotide] += 1

# If we reach here, we have dropped out of the `for` loop and
# are done reading through the file. Let's print out our results.
# This requires us to iterate over the sequence_id keys in the
# dict-of-dicts:
print("seqName\tA_count\tT_count\tG_count\tC_count")
for sequence_id in sequence_composition:
    # The nucleotide counts are integers, but we want to
    # print tab-delimited values, which means we need the
    # counts in str form:
    print('\t'.join((
        sequence_id,
        str(sequence_composition[sequence_id]['A']),
        str(sequence_composition[sequence_id]['C']),
        str(sequence_composition[sequence_id]['G']),
        str(sequence_composition[sequence_id]['T'])
    )))
