#!/usr/bin/env python
#CalculatingAssemblyStats_20181021.py
#Genome assembly exercise to calculate N50, L50 and contig totals, min and max from fasta file
#21 October 2018

import sys

from Bio.Seq import Seq
from Bio import SeqIO

fasta_file = sys.argv[1]

genome_len = 0
contig_count = 0
contig_lens = []
total_contigs = 0


N50 = 0
L50 = 0

#get a list of the lengths of all the contigs --> contig_lens
for record in SeqIO.parse(fasta_file, "fasta"):
  contig_lens.append(len(record))
  total_contigs += 1

genome = sum(contig_lens)
half_genome = genome / 2

sorted_contig_lens = sorted(contig_lens, reverse=True)
longest = max(contig_lens)
shortest= min(contig_lens)

#calculate L50 and N50 values
for contig_len in sorted_contig_lens:
  genome_len += contig_len
  contig_count += 1
  if genome_len >= half_genome:
    N50 = contig_len
    L50 = contig_count
    break

print("L50:" , L50)
print("N50:" , N50)
print("Total number of contigs:", total_contigs)
print("Shortest contig:", shortest)
print("Longest contig:", longest)
print("Genome size:", genome)
