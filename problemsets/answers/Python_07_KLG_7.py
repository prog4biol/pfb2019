#!/usr/bin/env python3

# Python 7 - Regular Expressions - Problem Set
# ===================

# 8. Now that you've done your restriction digest, determine the lengths of your fragments and sort them by length (in the same order they would separate on an electrophoresis gel).

# Hint: Convert this string:

# ```
# AAAAAAAAGACGT^CTTTTTTTAAAAAAAAGACGT^CTTTTTTT
# ```

# Into this list:

# ```
# ["AAAAAAAAGACGT","CTTTTTTTAAAAAAAAGACGT","CTTTTTTT"]
# ```


import re


# ```
# >seq1
# GAATTCAAGTTCTTGTGCGCACACAAATCCAATAAAAACTATTGTGCACACAGACGCGAC
# TTCGCGGTCTCGCTTGTTCTTGTTGTATTCGTATTTTCATTTCTCGTTCTGTTTCTACTT
# AACAATGTGGTGATAATATAAAAAATAAAGCAATTCAAAAGTGTATGACTTAATTAATGA
# GCGATTTTTTTTTTGAAATCAAATTTTTGGAACATTTTTTTTAAATTCAAATTTTGGCGA
# AAATTCAATATCGGTTCTACTATCCATAATATAATTCATCAGGAATACATCTTCAAAGGC
# AAACGGTGACAACAAAATTCAGGCAATTCAGGCAAATACCGAATGACCAGCTTGGTTATC
# AATTCTAGAATTTGTTTTTTGGTTTTTATTTATCATTGTAAATAAGACAAACATTTGTTC
# CTAGTAAAGAATGTAACACCAGAAGTCACGTAAAATGGTGTCCCCATTGTTTAAACGGTT
# GTTGGGACCAATGGAGTTCGTGGTAACAGTACATCTTTCCCCTTGAATTTGCCATTCAAA
# ATTTGCGGTGGAATACCTAACAAATCCAGTGAATTTAAGAATTGCGATGGGTAATTGACA
# TGAATTCCAAGGTCAAATGCTAAGAGATAGTTTAATTTATGTTTGAGACAATCAATTCCC
# CAATTTTTCTAAGACTTCAATCAATCTCTTAGAATCCGCCTCTGGAGGTGCACTCAGCCG
# CACGTCGGGCTCACCAAATATGTTGGGGTTGTCGGTGAACTCGAATAGAAATTATTGTCG
# CCTCCATCTTCATGGCCGTGAAATCGGCTCGCTGACGGGCTTCTCGCGCTGGATTTTTTC
# ACTATTTTTGAATACATCATTAACGCAATATATATATATATATATTTAT
# ```


fasta_file = open('apo1.fa', 'r')

seq_dict = {}
for line in fasta_file:
    line = line.rstrip()
    match = re.match(r'>(\S+)', line) ## answer for number 3
    if match:
        seqid = match.group(1)
        seq_dict[seqid] = ''
    else:
        seq_dict[seqid] += line

## print out to columns
for seq_id in seq_dict:
    sequence = seq_dict[seq_id]
    matches = re.finditer(r"([A|G])(AATT[C|T])", sequence) ## find all the matched
    new_sequence = sequence
    for x in matches:
        pattern = "".join(x.groups(0))
        replacement = "".join([x.groups(1)[0], "^", x.groups(1)[1]])
        new_sequence = re.sub(pattern, replacement, new_sequence)
    frags_list = new_sequence.split("^")
    frags_len = [len(x) for x in frags_list]          ## get the lengths of the fragments with a list comprehension
    f_len_s = sorted(frags_len)                       ## sort the lengths by size
    ind = [frags_len.index(x) for x in f_len_s][::-1] ## reverse the list smalles to largest and retrieve the index for each value
    [print(frags_list[x]) for x in ind]               ## print the fragments according to their length index
    
    
    


# 9. Download this file: ftp://ftp.neb.com/pub/rebase/bionet.txt of enzymes and their cut sites to fill a dictionary of enzymes paired with their recognition patterns. Be aware of the header lines, and be aware of how the columns are delimited. You'll modify this script in the next question.

# 10. Write a script which takes two command line arguments: the name of an enzyme and a fasta file with a sequence to be cut. Load a dictionary of enzyme names and cut sites from the code you developed in question 9.
#    If the enzyme is present in the dictionary, and can cut the sequence, print out:
#      - the sequence, annotated with cut sites
#      - the number of fragments
#      - the fragments in their natural order (unsorted)
#      - the fragments in sorted order (largest to smallest)
