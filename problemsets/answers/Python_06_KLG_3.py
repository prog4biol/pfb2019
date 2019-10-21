#!/usr/bin/env python3

# Python 6 - IO - Problem Set
# ===================

# 3. Open and print the reverse complement of each sequence in [Python_06.seq.txt](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_06.seq.txt). Each line is the following format:    `seqName\tsequence\n.` Make sure to print the output in fasta format including the sequence name and a note in the description that this is the reverse complement. Print to STDOUT and capture the output into a file with a command line redirect '>'. 
#    - **Remember is is always a good idea to start with a test set for which you know the correct output.**


in_file = open('Python_06.seq.txt', 'r')


for line in in_file:
    line = line.strip() ## strip whitespace and uppercase the line
    items = line.split()
    dna = items[1]
    dna_lower = dna.lower()
    dna_c = dna_lower.replace('a', 'T')
    dna_c = dna_c.replace('t', 'A')
    dna_c = dna_c.replace('g', 'C')
    dna_c = dna_c.replace('c', 'G')
    print(items[0] + "\t" + dna_c[::-1] )


    ## here's how I would redirect to a file
    ## ./Python_06_KLG_3.py >new_python6_seq.txt

