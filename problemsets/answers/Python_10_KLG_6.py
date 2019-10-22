#!/usr/bin/env python3
# Python 10 - Functions - Problem Set
# ===================


# 5. Create a new function that calculates the GC content of a DNA sequence. 
# 	- it will take a DNA sequence without spaces and no header as an argument and return the percentage of nucleotides that are a G or C.
# 	- example `percentGC = gc_conent('CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA')` or `percentGC = gc_content(dna)`

dna = 'GGCCAATTGG'

        
def rev_comp(dna):
    """Return the reverse complement of a dna string"""
    dna_lower = dna.lower()
    dna_c = dna_lower.replace('a', 'T')
    dna_c = dna_c.replace('t', 'A')
    dna_c = dna_c.replace('g', 'C')
    dna_c = dna_c.replace('c', 'G')
    return(dna_c[::-1]) 

print(rev_comp(dna))
