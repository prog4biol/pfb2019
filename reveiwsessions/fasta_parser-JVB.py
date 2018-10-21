#!/usr/bin/env python3

import sys

# we must define our functions above the main script code:
def reverse_complement(sequence):
    lower_seq = sequence.lower()
    lower_seq = lower_seq.replace('a','T')
    lower_seq = lower_seq.replace('t','A')
    lower_seq = lower_seq.replace('g','C')
    lower_seq = lower_seq.replace('c','G')

    return lower_seq[::-1]
    

# Read a FASTA file name from the command line:
fasta_filename = sys.argv[1]

# Open the FASTA file, and Python gives us a file object
# in order to interact with that file (fasta_fileobj is not
# the contents of the file!!!!):
fasta_fileobj = open(fasta_filename, 'r')

# Instead of using the `print()` built-in function, let's
# copy sys.stdout's file object to a new variable to use
# to write to. This enables our script to write to stdout
# by default, but allows the variable to be redefined to
# a new file object if we wish to write to a file directly:
output_fileobj = sys.stdout
if len(sys.argv) == 3:  # user gave an output file name:
    output_fileobj = open(sys.argv[2], 'w')

# Define empty string variables for our script to remember
# sequence information for each sequence between iterations
# of line-by-line reading with the `for` loop:
sequence_name = ''
sequence_desc = ''
sequence_string = ''
for line in fasta_fileobj:  # pull a line out from the file
    line = line.rstrip()

    # When reading a FASTA file, each line can represent only
    # either a sequence header, or (sub-)sequence. The binary
    # nature of the file format can be reflected by our code
    # by using `if`/`else` conditional logic:
    
    if line.startswith('>'):
        # `line` contains a sequence header line. If this iteration
        # of the `for` loop is NOT the first time we have observed
        # a sequence header line in the file, then we must have
        # information about the previous sequence stored in the
        # sequence_name, sequence_desc, and sequence_string
        # variables. We must first process the information from
        # the previous sequence before we can start handling the
        # header info of the current sequence, otherwise we will
        # end up overwriting that info. We can determine we have
        # observed a sequence previously by whether or not
        # sequence_string has a non-zero length:
        if len(sequence_string) > 0:
            # do something interesting with the stored info
            rc_sequence = reverse_complement(sequence_string)

            # Now output the processed sequence to a file:
            output_fileobj.write(">{} {}\n{}\n".format(
                sequence_name, sequence_desc, rc_sequence))
            sequence_string = ''  # reset for the new sequence

        # A sequence header line contains the general pattern 
        # ">genename multi-word sequence description",
        # where the sequence name is defined as any non-
        # whitespace characters before the first whitespace 
        # (i.e., "genename" above), the rest of the line
        # represents that sequence's description/meta info:
            
        line = line.lstrip('>')  # remove leading `>` char
        sequence_info = line.split(maxsplit=1)  # split on only first space

        # According to the FASTA spec, every sequence must have
        # a sequence name, so no need to check that it's there;
        # however, the sequence description is optional, so we
        # must explicitly check if it is present. If it is not,
        # our sequence_info list will contain one element instead
        # of two:
        sequence_name = sequence_info[0]
        if len(sequence_info) > 1:
            sequence_desc = sequence_info[1]
        else:
            # sequence has no description, set to empty
            sequence_desc = ''
            
    else:
        sequence_string += line  # incrementally elongate seq

# When we reach the end of the FASTA file, we drop out of the
# `for` loop. However, we still have the last sequence record
# stored in memory, which we haven't processed yet, because we
# haven't observed a `>` symbol, so we must copy and paste any
# code that we used to process sequences above to the code block
# below. But what if our FASTA file was empty? We wouldn't have
# any sequence info defined and so we must, again, check if
# sequence_string has a non-zero length to determine whether to
# execute the sequence processing code:
if len(sequence_string) > 0:
    # Note about duplicate code: It's less work to define and
    # debug code written in a function and call that function
    # in multiple places, rather than copy-and-paste large
    # blocks of code to many different places in your script.
    rc_sequence = reverse_complement(sequence_string)
    output_fileobj.write(">{} {}\n{}\n".format(
        sequence_name, sequence_desc, rc_sequence))

# Make sure to close your output files or risk losing data!    
output_fileobj.close()

