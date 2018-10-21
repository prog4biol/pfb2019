#!/usr/bin/env python3

import sys


def gc_content(sequence):
    gc_count = 0

    GC = set('gcGC')
    for nt in sequence:
        if nt in GC:
            gc_count += 1

    return 100.0 * gc_count / len(sequence)


try:
    fasta_filename = sys.argv[1]
    
except IndexError:
    sys.stderr.write("Please provide one input argument: fasta file name\n")
    sys.exit(1)
    
try:
    fasta_file = open(fasta_filename, 'r')
except IOError:
    sys.stderr.write("Cannot open {} for reading or it is not readable".format(fasta_filename))
    sys.exit(1)

sequence_id = None
sequence_desc = ''
sequence_string = ''
for line in fasta_file:
    if line.isspace():  # line is empty
        continue
    
    line = line.rstrip()

    if line.startswith('>'):
        if len(sequence_string) > 0:
            percentGC = gc_content(sequence_string)
            print("{0}\t{1:.2f}".format(sequence_id, percentGC))

        sequence_header = line.lstrip('>').split(maxsplit=1)
        sequence_string = ''
        sequence_id = sequence_header[0]

        if len(sequence_header) > 1: # has description
            sequence_desc = sequence_header[1]
        else:  # only an ID, no description
            sequence_desc = ''

    else:
        sequence_string += line

if len(sequence_string) > 0:
    percentGC = gc_content(sequence_string)
    print("{0}\t{1:.2f}".format(sequence_id, percentGC))

