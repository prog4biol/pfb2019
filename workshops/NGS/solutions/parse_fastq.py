#!/usr/bin/env python3

import sys

file = open(sys.argv[1], "r")

seqs=[]

for line in file:
  line = line.rstrip("\n")
  if len(seqs) == 3: #this means you have the 4th line in the line variable
    seqs.append(line) #you might was well add it to the list
    #trim off five nucleotides
    print(seqs[0],seqs[1][5:],seqs[2],seqs[3][5:],sep="\n")

    seqs=[] #clear out the list to get ready for the next read
  else: #add the line to the list since you don't have all 4 lines yet
    seqs.append(line)
