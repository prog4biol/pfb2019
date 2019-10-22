#!/usr/bin/env python3

import sys

seq_dict= {}
sequence = ''
sequence_desc = ''
sequence_ID = ''
valid_nt = set('ACTGN')

file = ''

try:
  file = sys.argv[1]

  if not (file.endswith('.fa') or file.endswith('.fasta') or file.endswith('.nt')):
    raise ValueError('Not a freaking fasta')
  
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
        line = line.rstrip().upper()

        for nt in line:
          if nt not in valid_nt:
            raise Exception('Invalid nucleotide characters')
          
        
        sequence += line

    if len(sequence) > 0:
      seq_dict[sequence_ID] = { 'sequence' : sequence , 'description' : sequence_desc }
  
  with open('Python_08.codons-frame-1.nt', 'w') as wFile:
    for key in seq_dict:
      split_seq = ''
      seq_to_split = seq_dict.get(key).get('sequence')
      for i in range(0, len(seq_to_split), 3):
        split_seq += seq_to_split[i:i+3] + ' '
      wFile.write(key+'-'+'frame 1 codons'+'\n'+split_seq+'\n')

  with open('Python_08.codons-frame-3.nt', 'w') as wFile:
    for key in seq_dict:
      seq_to_split = seq_dict.get(key).get('sequence')
      for j in [0,1,2]:
        split_seq = ''
        for i in range(j, len(seq_to_split), 3):
          split_seq += seq_to_split[i:i+3] + ' '
        wFile.write(key+'-'+'frame '+str(1+j)+' codons'+'\n'+split_seq+'\n')

except IndexError:
  print('Please provide a file')
 
  
  
