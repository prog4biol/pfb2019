#!/usr/bin/env python3

# Python 6 - IO - Problem Set
# ===================

# 5. Write your first FASTA parser. This is a script that reads in a FASTA file and stores each FASTA record separately for easy access for future analysis.

# Things to keep in mind:
#    - open your file
#    - read each line
#    - is your line a header line? is it a sequence line?
#    - does a single FASTA record have one line of sequence or multiple lines of sequence?
   
#    HINTS: use file I/O, if statements and dictionaries to write your first FASTA parser. Some other useful functions and methods are find, split, string concatenation.
   
#    At the end, your script should return the following:
   
#    fastaDict = {
#       'seq1' : 'AAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGCCACCAATTATGGTGTATGAGTGAATCTCTGGTCCGAGATTCACTGAGTAACTGCTGTACACAGTAGTAACACGTGGAGATCCCATAAGCTTCACGTGTGGTCCAATAAAACACTCCGTTGGTCAAC' ,
#       'seq2' : 'GCCACAGAGCCTAGGACCCCAACCTAACCTAACCTAACCTAACCTACAGTTTGATCTTAACCATGAGGCTGAGAAGCGATGTCCTGACCGGCCTGTCCTAACCGCCCTGACCTAACCGGCTTGACCTAACCGCCCTGACCTAACCAGGCTAACCTAACCAAACCGTGAAAAAAGGAATCT' ,
#       'seq3' : 'ATGAAAGTTACATAAAGACTATTCGATGCATAAATAGTTCAGTTTTGAAAACTTACATTTTGTTAAAGTCAGGTACTTGTGTATAATATCAACTAAAT' ,
#       'seq4' : 'ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAAACAACATGCCAAATAGAAACGATCAATTCGGCGATGGAAATCAGAACAACGATCAGTTTGGAAATCAAAATAGAAATAACGGGAACGATCAGTTTAATAACATGATGCAGAATAAAGGGAATAATCAATTTAATCCAGGTAATCAGAACAGAGGT' }

in_file = open('python6.fasta', 'r')

seq_dict = {}
for line in in_file:
    line = line.strip() ## strip whitespace and uppercase the line
    if line.startswith(">"):
        header = line
        seq_dict[header] = ''
    else:
        seq_dict[header] += line

print(seq_dict)
