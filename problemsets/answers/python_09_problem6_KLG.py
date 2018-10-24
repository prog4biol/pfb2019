#!/usr/bin/env python3

## define my function
def get_reverse_complement(sequence):
    DNA          = sequence.lower()
    DNA_comp     = DNA.replace('a', 'T').replace('c','G').replace('g', 'C').replace('t','A')
    sequence_rev = DNA_comp[::-1]
    return sequence_rev
    


## test and run my function
dna = 'GGCCGGCCGAATT'

print(get_reverse_complement(dna))
