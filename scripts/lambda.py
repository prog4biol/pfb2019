#!/usr/bin/env python3

def get_first_codon(dna):
  return dna[0:3]
print(get_first_codon('ATGTTT'))


get_first_codon = lambda dna : dna[0:3]
print(get_first_codon('ATGTTT'))


print((lambda dna : dna[0:3])('ATGTTT'))
