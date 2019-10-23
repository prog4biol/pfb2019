#!/usr/bin/env python
# 2. Modify your function so that it will work whether the DNA string
#    does or does not have newlines.

# INPUT:
# dna = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
# GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
# CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
# TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
# TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
# CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
# GTCATCTTCT'''


# OUTPUT:
# GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTT
# CTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTT
# GCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCA
# GACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
# TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTC
# CCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATG
# GTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGT
# GGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
# GTCATCTTCT

import sys


def wrap(maybe_linear_sequence):
    """
    Input: (Required) A linear sequence string without any existing newline 
           characters.
           (Optional) An integer `width` argument to specify the maximum
           line length to wrap the sequence flush to.
       
    Returns: A string of the input sequence, but with newline characters
           at fixed intervals specified by the `width` keyword argument.
    """

    # If the input sequence has newlines in it, we can quickly "delete" them
    # by replacing them with empty string "characters":
    linear_sequence = maybe_linear_sequence.replace('\n','')
    
    width = 60
    wrapped_sequence = ''
    linear_sequence_length = len(linear_sequence)  # pre-calc it
    for offset in range(0, linear_sequence_length, width):
        # Our function iterated over each sequence, jumping every `width`
        # nucleotides along the string. This is effectively like a sliding-
        # window approach, where windows do not overlap. The left coordinate
        # of the window is `offset`, the right coordinate is `offset+width`
        if offset+width < linear_sequence_length:
            # then the sliding window sits completely within the sequence:
            # Iter 1:
            # +---------+
            #    Iter 2: +---------+
            #               Iter 3: +---------+
            # ===================================   Sequence
            wrapped_sequence += linear_sequence[offset:(offset+width)] + "\n"
        else:
            # then the sliding window projects off the end of the sequence
            # and we need to bound the window to the end of the string.
            # Also, we don't want to add the newline to the last line
            #                          Iter 4: +---------+
            # ===================================   Sequence
            wrapped_sequence += linear_sequence[offset:linear_sequence_length]

    return wrapped_sequence


dna = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

print(wrap(dna))
