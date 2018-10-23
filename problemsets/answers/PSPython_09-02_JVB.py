#!/usr/bin/env python3


def fold_sequence(linear_sequence):
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
    # incrementing by 60:
    for beg in range(0, linear_sequence_length, 60):
        end = beg + 60  # end of line subsequence

        folded_sequence.append(linear_sequence[beg:end])

    return '\n'.join(folded_sequence)



dna='''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

print("INPUT:")
print(dna)
print()

folded_seq = fold_sequence(dna)

print("OUTPUT:")
print(folded_seq)

