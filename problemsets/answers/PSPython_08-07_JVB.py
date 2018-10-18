#!/usr/bin/env python3

# Python 08, problem 7
# ====================
# Find the longest peptide sequence (M-->Stop) of all the six
# translated reading frames for a single sequence. Do this for
# all the sequence records. For each sequence, print out in
# FASTA format the six frames of codons to one file
# (Python_08.codons-6frames.nt), the translations to a second
# file (Python_08.translated.aa), and the single longest
# translated peptide to a third file
# (Python_08.translated-longest.aa).

# In order to receive data in the script, given by the user
# from the command line, we need to first make sure we import
# the sys module to access information from the outside system
import sys


# Remember that sys.argv's first position (index 0) contains
# the script name, but we want the second position (index 1).
try:
    fasta_filename = sys.argv[1]  # raises IndexError if no input

    # raise an exception if the file doesnt end iwth .fa, .nt, or .fasta
    if not (fasta_filename.endswith('.fa') or
            fasta_filename.endswith('.nt') or
            fasta_filename.endswith('.fasta')):
        raise Exception("Filename does not end in either .nt, .fa, nor .fasta")

except Exception:  # IndexError is a subclass of Exception
    print("Error: No input file or incorrect file suffix", file=sys.stderr)
    sys.exit(1)

    
try:
    output_prefix = sys.argv[2]  # raises IndexError in no input
    
except IndexError:
    print("Error: No output file prefix", file=sys.stderr)
    sys.exit(1)

    
codon_filename = output_prefix + '.codons-6frames.nt'
trans_filename = output_prefix + '.translated.aa'
long_aa_filename = output_prefix + '.translated-longest.aa'

try:    
    fasta_file = open(fasta_filename, 'r')
    codon_file = open(codon_filename, 'w')
    trans_file = open(trans_filename, 'w')
    long_aa_file = open(long_aa_filename, 'w')
    
except IOError as error:
    print("Error: " + str(error), file=sys.stderr)
    sys.exit(1)    
    
    
# Because python reads files line-by-line, and fasta sequences
# are arranged after their sequence IDs on different lines
# (and not the same lines as the IDs), we need to initialize
# global variables in order for our script to "remember" which
# sequence ID and sequence string we are working with when we
# get to each sequence line
sequence_id = None
sequence_string = ''

valid_nucleotides = set('ATCGN')
complement_table = str.maketrans({'A':'T','C':'G','T':'A','G':'C','N':'N'})
translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}
    

# In order to iterate over all sequences in our file, use a
# "for" loop to read line-by-line; store all sequences in a
# dictionary called sequence_strings
codon_length = 3
sequence_ids = list()
sequence_strings = dict()
for line in fasta_file:
    line = line.rstrip()  # strip of ending \n char

    if line.startswith('>'):
        # ...then it's a sequence definition/description line
        # and the first set of non-whitespace characters is the
        # sequence ID; everything after the first whitespace
        # represents the sequence comment/description:
        sequence_def = line.lstrip('>').split(' ', maxsplit=1)
        sequence_id = sequence_def[0]
        sequence_strings[sequence_id] = {'+':'', '-':''}
        sequence_ids.append(sequence_id)
        
    else:
        # this is a sequence line, so let's append the sequence
        # to the sequence_string variable to "grow" out the full
        # sequence
        line = line.upper()

        # check that every nucleotide in the sequence is a valid
        # nucleotide character:
        for nucleotide in line:
            if nucleotide not in valid_nucleotides:
                raise Exception("Invalid nucleotide character in {0}: {1}".format(
                    sequence_id, nucleotide
                ))

        sequence_strings[sequence_id]['+'] += line  # j.i.c. the fasta is wrapped


# Iterate over each sequence again, calculate the reverse-complement
# sequence and the 6-frame translations (3 frames per strand)
for sequence_id in sequence_ids:
    sequence_strings[sequence_id]['-'] = sequence_strings[sequence_id]['+'].translate(complement_table)

    info = list()  # for storing frame and orf number
    nt_list = list()
    aa_list = list()
    num_translations = 0
    for strand in ('+', '-'):
        sequence_string = sequence_strings[sequence_id][strand]

        for frame in range(codon_length):
            # iterate over every third character in the sequence
            # and use string slicing to extract out three chars
            # at a time:
            num_orfs = 0
            codons = []
            aminos = []
            for offset in range(0, len(sequence_string), codon_length):
                beg = offset + frame  # 'beg' = beginning of codon triplet
                end = beg + codon_length  # 'end' = end of codon triplet

                # If the sequence length is not divisible by 3, we could
                # get partial codons, so we have to check this explicitly
                if end <= len(sequence_string):
                    codon = sequence_string[beg:end]
                    amino = translation_table[codon]
                                    
                    codons.append(codon)
                    aminos.append(amino)
                    
                    if amino == '*':  # end of orf
                        info.append((frame, num_orfs))
                        nt_list.append(codons)  # list of lists
                        aa_list.append(aminos)  # list of lists
                        num_translations += 1
                        num_orfs += 1
                        codons = []  # clear old for new orf
                        aminos = []  # clear old for new orf
                    

            # The following condition will be true if the last orf
            # does not end in a stop:
            if len(codons) > 0:
                info.append((frame, num_orfs))
                nt_list.append(codons)
                aa_list.append(aminos)
                num_translations += 1
                num_orfs += 1                
        

    longest_frame = -1
    longest_length = -1
    longest_codons = []
    longest_aminos = []
    for i in range(num_translations):  
        codons = nt_list[i]
        aminos = aa_list[i]
        frame, orf = info[i]

        if aminos[0] == '*':
            continue
        
        # frame = 1-3 on (+) strand, 4-6 on (-) strand; add codon_length
        # to get correct frame number for each strand
        frame += (codon_length if info[i] == '-' else 0)  

        try:
            first_M = aminos.index('M')
        except ValueError:  # if no match
            # has no Met start codon
            continue  # to the next translation

        if aminos[-1] != '*':  # has no stop codon
            continue  # to the next translation

        # trim the condons and translation from M=>STOP
        orf_codons = codons[first_M:]
        orf_aminos = aminos[first_M:]
        
        codon_file.write('>{0}-frame-{1}-orf-{2}-codons\n'.format(sequence_id, frame+1, orf+1))
        codon_file.write(' '.join(orf_codons) + '\n')
        trans_file.write('>{0}-frame-{1}-orf-{2}-aminos\n'.format(sequence_id, frame+1, orf+1))
        trans_file.write(''.join(orf_aminos) + '\n')

        # As we iterate through each sequence, update
        # which is the longest we observe and keep
        # for printing later:
        if len(orf_aminos) > longest_length:
            longest_length = len(orf_aminos)
            longest_aminos = orf_aminos
            longest_frame  = frame
            longest_orf    = orf
            
    long_aa_file.write('>{0}-frame-{1}-orf-{2}-aminos\n'.format(sequence_id, longest_frame+1, longest_orf+1))
    long_aa_file.write(''.join(longest_aminos) + '\n')
