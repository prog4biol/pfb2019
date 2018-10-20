#!/usr/bin/env python3

import sys

def reverse_complement(sequence):
    lower_seq = sequence.lower()
    lower_seq = lower_seq.replace('a','T')
    lower_seq = lower_seq.replace('t','A')
    lower_seq = lower_seq.replace('g','C')
    lower_seq = lower_seq.replace('c','G')

    return lower_seq[::-1]
    

fasta_filename = sys.argv[1]

fasta_fileobj = open(fasta_filename, 'r')
output_file = sys.stdout
if len(sys.argv) == 3:
    output_file = open(sys.argv[2], 'w')


sequence_name = ''
sequence_desc = ''
sequence_string = ''
for line in fasta_fileobj:
    line = line.rstrip()
    if line.startswith('>'):
        if len(sequence_string) > 0:
            # do something interesting with the stored info
            rc_sequence = reverse_complement(sequence_string)
            output_file.write(">{} {}\n{}\n".format(
                sequence_name, sequence_desc, rc_sequence))
            sequence_string = ''
            
        line = line.lstrip('>')
        sequence_info = line.split(maxsplit=1)
        sequence_name = sequence_info[0]
        if len(sequence_info) > 1:
            sequence_desc = sequence_info[1]

    else:
        sequence_string += line  # grow the sequence

if len(sequence_string) > 0:
    # do something interesting with the stored info
    rc_sequence = reverse_complement(sequence_string)
    output_file.write(">{} {}\n{}\n".format(
        sequence_name, sequence_desc, rc_sequence))
    # sequence_string = ''
