#!/usr/bin/env python3

import sys

gene = sys.argv[1] ## user input was brca1
genes = { 'hdac' : 'aaaaa' , 'piwi' : 'ttttt' }

print("Users favorite gene: " , gene)

for gene in genes:
  gene_length = len( genes[gene] )
  print(gene, gene_length)


print("Users favorite gene: " , gene)
