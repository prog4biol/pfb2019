#!/usr/bin/env python3

import sys

def fold_sequence(linear_sequence, width=60):
    # There are a couple of ways of solving this
    # problem; it can be done with a regex or
    # by string slicing (which is the approach
    # favored below). The idea is to "slide" a
    # non-overlapping window over the sequence
    # and output the subsequences 60 bp long:
    #
    # subseq:   line1  line2  line3
    #    beg:   0      60     120       
    #           |------|------|------|
    #           GCATCGTAGCTTATCTCG
    # result:
    #           GCATCGT
    #           AGCTTAT
    #           CTCG
    #
    # In order to re-fold an sequence, we must first
    # un-fold it (make it linear) by deleting the
    # "\n" chars:
    linear_sequence = linear_sequence.replace('\n', '')    

    # store sub-sequences in a temporary list:
    folded_sequence = []
    linear_sequence_length = len(linear_sequence)    
    # Using the `range()` function, we can iterate over
    # the sequence, from 0 to the en of the sequence,
    # incrementing by `width`:
    for beg in range(0, linear_sequence_length, width):
        end = beg + width  # end of line subsequence

        folded_sequence.append(linear_sequence[beg:end])

    return '\n'.join(folded_sequence)


try:
    fasta_filename = sys.argv[1]
    line_width = int(sys.argv[2])
except IndexError:
    sys.stderr.write("Please provide two input arguments: 1) fasta file name, 2) line width\n")
    sys.exit(1)

except ValueError:
    sys.stderr.write("Line width argument must be an unsigned integer value\n")
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
            print(">{} {}".format(sequence_id, sequence_desc))
            print(fold_sequence(sequence_string, width=line_width))

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
    print(">{} {}".format(sequence_id, sequence_desc))
    print(fold_sequence(sequence_string, width=line_width))


