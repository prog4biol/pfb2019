#!/usr/bin/env python3

## define my function
def gc_content(dna):
    dna    = dna.upper()    ## first make sure the DNA is all upper case
    G      = dna.count('G') ## count the Gs
    C      = dna.count('C') ## count the Cs
    length = len(dna)       ## count the length
    gc     = (G+C)/length   ## calculate the GC content
    return(gc)              ## return the content


## test and run my function
dna = 'GGCCGGCCGAATT'

print(gc_content(dna))
