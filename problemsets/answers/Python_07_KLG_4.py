#!/usr/bin/env python3

# Python 7 - Regular Expressions - Problem Set
# ===================



import re



# 5. Create a FASTA parser, or modify your FASTA parser from the previous problem set, to use regular expressions. Also make sure your parser can deal with a sequence that is split over many lines.

fasta_file = open('Python_07.fasta', 'r')

seq_dict = {}
sequence = ''
for line in fasta_file:
    line = line.rstrip()
    match = re.match(r'>(\S+)\s+(.*)', line) ## answer for number 3
    if match:
        if sequence: ## only evaluates if seqid has been set to add to the dictionary
            seq_dict[seqid] = sequence ## only open the dictionary once for each new sequence
            seqid = match.group(1)
            sequence = ''
        else:
            seqid = match.group(1)
            sequence = ''
    else:
        sequence += line
seq_dict[seqid] = sequence ## add the last sequence to the dictionary

## print out to columns
for seq_id in seq_dict:
    print(seq_id, seq_dict[seq_id], sep = "\t")



# 6. The enzyme ApoI has a restriction site: R^AATTY where R and Y are degenerate nucleotideides. See the IUPAC table to identify the nucleotide possibilities for the R and Y. Write a regular expression to find and print all occurrences of the site in the following sequence [Python_07_ApoI.fasta](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_07_ApoI.fasta). 

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


# 7. Determine the site(s) of the physical cut(s) by ApoI in the above sequence. Print out the sequence with "^" at the cut site.

#   Hints:  
#    - Use `sub()`  
#    - Use subpatterns (parentheses and `group()` ) to find the cut site within the pattern.
#    - Example: if the pattern is GACGT^CT the following sequence

# ```
# AAAAAAAAGACGTCTTTTTTTAAAAAAAAGACGTCTTTTTTT
# ```
# we want to display the cut site like this:

# ```
# AAAAAAAAGACGT^CTTTTTTTAAAAAAAAGACGT^CTTTTTTT
# ```

# 8. Now that you've done your restriction digest, determine the lengths of your fragments and sort them by length (in the same order they would separate on an electrophoresis gel).

# Hint: Convert this string:

# ```
# AAAAAAAAGACGT^CTTTTTTTAAAAAAAAGACGT^CTTTTTTT
# ```

# Into this list:

# ```
# ["AAAAAAAAGACGT","CTTTTTTTAAAAAAAAGACGT","CTTTTTTT"]
# ```

# 9. Download this file: ftp://ftp.neb.com/pub/rebase/bionet.txt of enzymes and their cut sites to fill a dictionary of enzymes paired with their recognition patterns. Be aware of the header lines, and be aware of how the columns are delimited. You'll modify this script in the next question.

# 10. Write a script which takes two command line arguments: the name of an enzyme and a fasta file with a sequence to be cut. Load a dictionary of enzyme names and cut sites from the code you developed in question 9.
#    If the enzyme is present in the dictionary, and can cut the sequence, print out:
#      - the sequence, annotated with cut sites
#      - the number of fragments
#      - the fragments in their natural order (unsorted)
#      - the fragments in sorted order (largest to smallest)
