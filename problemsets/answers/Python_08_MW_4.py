#!/usr/bin/env python3

import sys
from function import *

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
  
  total_nt_dict = {}
  with open('Python_08.codons-frame-6.nt', 'w') as wFile:
    for key in seq_dict:
      seq_to_split = seq_dict.get(key).get('sequence')
      rc_seq_to_split = rev_comp(seq_to_split)
      codon_dict = {}
      total_nt_dict[key] = codon_dict
      
      for j in [0,1,2]:
        split_seq = ''
        rc_split_seq = ''        
        for i in range(j, len(seq_to_split), 3):
          split_seq += seq_to_split[i:i+3] + ' '
          rc_split_seq += rc_seq_to_split[i:i+3] + ' '
          
        codon_frame_key = 'frame '+str(1+j)+' codons'
        rc_codon_frame_key = 'RC frame '+str(1+j)+' codons'        
        total_nt_dict[key][codon_frame_key] = split_seq
        total_nt_dict[key][rc_codon_frame_key] = rc_split_seq
        wFile.write(key+' '+codon_frame_key+'\n'+split_seq+'\n'+key+rc_codon_frame_key+'\n'+rc_split_seq+'\n')

  test = 'GCT CAG CTC'
  print(test)
  print(translate(test))
  
  with open('Python_08.translated.aa', 'w') as protFile:
    for key in total_nt_dict:
      for frame in total_nt_dict[key]:
        seq_to_trans = total_nt_dict[key][frame]
        prot_seq = translate(seq_to_trans)
        protFile.write(key+' '+frame+' translated'+'\n'+prot_seq+'\n')
                
except IndexError:
  print('Please provide a file')
 
  
  
