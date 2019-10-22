#!/usr/bin/env python3

import sys

file = sys.argv[1]

seq_dict= {}
sequence = ''
sequence_desc = ''
sequence_ID = ''

with open(file, 'r') as myFile:

  for line in myFile:
    if line.startswith('>'):
      if len(sequence) > 0:
        seq_dict[sequence_ID] = { 'sequence' : sequence , 'description' : sequence_desc }
        sequence = ''
      line = line.lstrip('>')
      line = line.rstrip()
      sequence_ID, sequence_desc = line.split(maxsplit = 1)

    else:
      sequence += line.rstrip()

  if len(sequence) > 0:
        seq_dict[sequence_ID] = { 'sequence' : sequence , 'description' : sequence_desc }
  
  for key in seq_dict:
    seq_to_count = seq_dict.get(key).get('sequence')
        
    countA = seq_to_count.count('A')
    countT = seq_to_count.count('T')     
    countC = seq_to_count.count('C')
    countG = seq_to_count.count('G')

    seq_dict[key] = { 'sequence_composition' : { 'A' : countA , 'T' : countT , 'C' : countC , 'G' : countG } }

    print(key+'\t'+str(countA)+'\t'+str(countT)+'\t'+str(countG)+'\t'+str(countC))
