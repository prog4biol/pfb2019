#!/usr/bin/env python3
# Python 10 - Functions - Problem Set
# ===================


# 5. Create a new function that calculates the GC content of a DNA sequence. 
# 	- it will take a DNA sequence without spaces and no header as an argument and return the percentage of nucleotides that are a G or C.
# 	- example `percentGC = gc_conent('CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA')` or `percentGC = gc_content(dna)`

dna = 'GGCCAATTGG'

        
def gc_content(dna):
    dna = dna.upper()
    return((dna.count('G') + dna.count('C'))/len(dna)*100) ## use string methods to get the GC content

print(gc_content(dna))

