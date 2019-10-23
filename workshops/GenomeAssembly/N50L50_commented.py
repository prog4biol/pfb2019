#!/usr/bin/env python3
#N50L50_commented.py
#Genome assembly exercise to calculate N50, L50 and contig totals, min and max from fasta file
#23 March 2019

#importing module
import sys

#importing modules
#Bio is class name, Bio.Seq is subclass name, Seq module
from Bio.Seq import Seq
from Bio import SeqIO

#taking input fasta file of contigs from command line
fasta_file = sys.argv[1]

#counter for number of nucleotides
nt_count = 0
#counter for number of contigs for L50 and N50 measures
contig_count = 0
#list of contig lengths 
contig_lens = []
#counter for total number of contigs
total_contigs = 0

#setting N50 and L50 to zero
N50 = 0
L50 = 0

#get a list of the lengths of all the contigs --> contig_lens
for record in SeqIO.parse(fasta_file, "fasta"):
#appending the length of each contig to running total  
  contig_lens.append(len(record))
  #incrementing total number of contigs
  total_contigs += 1

#summing contig lenghs for genome size
genome = sum(contig_lens)
#getting half of genome size for L50 and N50 measures
half_genome = genome / 2

#sort the list contig_lens (reverse short to long)
sorted_contig_lens = sorted(contig_lens, reverse=True)

#get max contig length with min(list)
longest = max(contig_lens)

#get min contig length with max(list)
shortest= min(contig_lens)

#get L50 and N50 values
for contig_len in sorted_contig_lens:
#incrementing number of nucleotides by each contig length
  nt_count += contig_len
  #incrementing contig count 
  contig_count += 1
  if nt_count >= half_genome:
    #when reach half size of genome, get values of N50 and L50
    L50 = contig_len
    N50 = contig_count
    #break out of loop once hit half size of genome
    break

#print out all values
print("L50:" , L50)
print("N50:" , N50)
print("Total number of contigs:", total_contigs)
print("Shortest contig:", shortest)
print("Longest contig:", longest)
print("Genome size:", genome)
