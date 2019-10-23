#!/usr/bin/env python
# 3. Modify your function so that it takes two arguments, the DNA string and the
#    max length of each line.

# INPUT:
# dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
# width = 80

# OUTPUT:
# GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
# GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
# CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
# TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
# TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
# CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
# GTCATCTTCT


import sys


def wrap(maybe_linear_sequence, width=None):
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
    
    if width is None:
        # Set the default width of each line to be the max integer size of
        # your machine (typically either 2**(64-1) on 64-bit machines or
        # 2**(32-1) on 32-bit machines) by convention.
        width = sys.maxsize
        
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


dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'

print(wrap(dna, width=60))
