#!/usr/bin/env python3

import sys

file = open(sys.argv[1], "r")

seqs={}
seqid = ""

for line in file:
  line = line.rstrip("\n")
  if line.startswith('>'):
    
    def_line = line.split(' ') #split on spaces to get the ID on it's own
    seqid = def_line[0][1:] #use the [1:] to get rid of the > sign

    
  else:
    if seqid in seqs: #check to see if there is already sequece in this key. if there is append more
      seqs[seqid] += line 
    else: 
      seqs[seqid] = line #if there isn't sequence start the party

#Now you have your dictionary you can loupe through it
for key in seqs:
  print(key,"\t",seqs[key])
