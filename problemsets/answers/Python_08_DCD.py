"""
1. Take a multi-FASTA [Python_08.fasta](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_08.fasta) file from user input and calculate the nucleotide comp for each seq. Use a datastructure to keep count. Print out each seq name and its compostion in this format `seqName\tA_count\tT_count\tG_count\C_count`

Here is a structure of a handy datastructure to store this information

```
seqs[geneName][nucleotide]=count

seqs['geneA']['A'] = 2
seqs['geneA']['T'] = 3
seqs['geneA']['G'] = 3
seqs['geneA']['C'] = 1

seqs['geneB']['A'] = 1
seqs['geneB']['T'] = 5
seqs['geneB']['G'] = 2
seqs['geneB']['C'] = 2
``` 
"""

import sys

fasta_filename = sys.argv[1]
fasta_filename = 'Python_08_short.fasta'
fasta_filehandle = open(fasta_filename, 'r')
seq_comp = dict()
seq_id = None

for line in fasta_filehandle:
    line = line.rstrip()
    if line.startswith('>'):
        seq_def = line.lstrip('>').split(' ', maxsplit=1)
        seq_id = seq_def[0]
        seq_comp[seq_id] = {
            'A': 0, 'T': 0, 'G': 0, 'C': 0}    
    else:
        for nucleotide in line:
            seq_comp[seq_id][nucleotide] += 1
            print(seq_comp)

print("seqName\tA_count\tT_count\tG_count\tC_count")

for seq_id in seq_comp:
    print('\t'.join((seq_id,
        str(seq_comp[seq_id]['A']),
        str(seq_comp[seq_id]['C']),
        str(seq_comp[seq_id]['G']),
        str(seq_comp[seq_id]['T'])
    )))


"""
2. Write a script that takes a multi-FASTA file [Python_08.fasta](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_08.fasta) from user input and breaks each seq into codons (every three nucleotides is a codon) in just the first reading frame. Your output should look like this
```
seq1-frame-1-codons
CAT GCT TGA GTC
```
Write the output to a file called 'Python_08.codons-frame-1.nt'.
"""
import sys

fasta_filename = sys.argv[1]
fasta_filehandle = open(fasta_filename, 'r') 

seq_id = None
seq_string = ''

for line in fasta_filehandle:
    line = line.rstrip()  # strip of ending \n char

    if line.startswith('>'):
        if len(seq_string) > 0:
            print(seq_id + "-frame" + str(1) + "-codons")
            sep = ''  
            for offset in range(0, len(seq_string), 3):
                print("{0}{1}".format(sep, seq_string[offset:offset+3]), end='')
                sep=' '
            print()  # prints a \n

        seq_def = line.lstrip('>').split(' ', maxsplit=1)
        seq_id = seq_def[0]
        seq_string = ''  # make empty again for new seq
        
    else:
        seq_string += line.upper()

if len(seq_string) > 0:
    print(seq_id + "-frame" + str(1) + "-codons")
    sep = ''  
    for offset in range(0, len(seq_string), 3):
        print("{0}{1}".format(sep, seq_string[offset:offset+3]), end='')
        sep=' '
                
    print()



"""
3. Now produce codons in the first three reading frames for each seq and
print out ids and seq records for each frame and print to a file called
'Python_08.codons-3frames.nt'

For example
```
seq1-frame-1-codons
ATG TTG
seq-frame-2-codons
TGT TGA
``` 
"""
import sys

try:
    fasta_filename = sys.argv[1]
    if not (fasta_filename.endswith('.fa') or
            fasta_filename.endswith('.nt') or
            fasta_filename.endswith('.fasta')):
        raise Exception("Filename does not end in either .nt, .fa, nor .fasta")

    fasta_filehandle = open(fasta_filename, 'r') 

except Exception as error:  
    print("Error: " + str(error), file=sys.stderr)
    sys.exit(1)

seq_id = None
seq_string = ''

valid_nucleotides = set('ATCGN')

for line in fasta_filehandle:
    line = line.rstrip()  # strip of ending \n char

    if line.startswith('>'):
        if len(seq_string) > 0:

            for frame in range(3):
                print(seq_id + "-frame" + str(frame+1) + "-codons")
                sep = ''  
                for offset in range(0, len(seq_string), 3):
                    if offset+frame+3 <= len(seq_string):
                        print("{0}{1}".format(sep, seq_string[offset+frame:offset+frame+3]), end='')
                        sep=' '
                print()  # prints a \n
                
        seq_def = line.lstrip('>').split(' ', maxsplit=1)
        seq_id = seq_def[0]
        seq_string = ''  # make empty again for new seq
        
    else:
        line = line.upper()
        
        for nucleotide in line:
            if nucleotide not in valid_nucleotides:
                raise Exception("Invalid nucleotide character in {0}: {1}".format(
                    seq_id, nucleotide
                ))

        seq_string += line
        
if len(seq_string) > 0:
    for frame in range(3):
        print(seq_id + "-frame" + str(frame+1) + "-codons")
        sep = ''  
        for offset in range(0, len(seq_string), 3):
            if offset+frame+3 <= len(seq_string):
                print("{0}{1}".format(sep, seq_string[offset+frame:offset+frame+3]), end='')
                sep=' '
            
        print()





"""
4. Now reverse complement each seq and print out all six reading frames
to a file called 'Python_08.codons-6frames.nt'
"""

import sys

try:
    fasta_filename = sys.argv[1]
    if not (fasta_filename.endswith('.fa') or
            fasta_filename.endswith('.nt') or
            fasta_filename.endswith('.fasta')):
        raise Exception("Filename does not end in either .nt, .fa, nor .fasta")

    fasta_filehandle = open(fasta_filename, 'r') 

except Exception as error:  
    print("Error: " + str(error), file=sys.stderr)
    sys.exit(1)

seq_id = None
seq_string = ''

valid_nucleotides = set('ATCGN')
complement_table = str.maketrans({'A':'T','C':'G','T':'A','G':'C','N':'N'})

for line in fasta_filehandle:
    line = line.rstrip()  # strip of ending \n char

    if line.startswith('>'):
        if len(seq_string) > 0:

            for frame in range(3):
                print(seq_id + "-frame" + str(frame+1) + "-codons")
                sep = ''  

                for offset in range(0, len(seq_string), 3):
                    if offset+frame+3 <= len(seq_string):
                        print("{0}{1}".format(sep, seq_string[offset+frame:offset+frame+3]), end='')
                        sep=' '
                
                print()  # prints a \n

            seq_string = seq_string[::-1].translate(complement_table)
                
            for frame in range(3):
                print(seq_id + "-frame" + str(frame+4) + "-codons")

                sep = ''  

                for offset in range(0, len(seq_string), 3):
                    if offset+frame+3 <= len(seq_string):
                        print("{0}{1}".format(sep, seq_string[offset+frame:offset+frame+3]), end='')
                        sep=' '
                
                print()  # prints a \n
                
        seq_def = line.lstrip('>').split(' ', maxsplit=1)
        seq_id = seq_def[0]
        seq_string = ''  # make empty again for new seq
        
    else:
        line = line.upper()
        
        for nucleotide in line:
            if nucleotide not in valid_nucleotides:
                raise Exception("Invalid nucleotide character in {0}: {1}".format(
                    seq_id, nucleotide
                ))

        seq_string += line
        
if len(seq_string) > 0:
    for frame in range(3):
        print(seq_id + "-frame" + str(frame+1) + "-codons")
        sep = ''  
        for offset in range(0, len(seq_string), 3):
            if offset+frame+3 <= len(seq_string):
                print("{0}{1}".format(sep, seq_string[offset+frame:offset+frame+3]), end='')
                sep=' '
            
        print()

    seq_string = seq_string[::-1].translate(complement_table)
                
    for frame in range(3):
        print(seq_id + "-frame" + str(frame+4) + "-codons")
        sep = ''  
        for offset in range(0, len(seq_string), 3):
            if offset+frame+3 <= len(seq_string):
                print("{0}{1}".format(sep, seq_string[offset+frame:offset+frame+3]), end='')
                sep=' '
                
        print()  # prints a \n



"""
5. Translate each of the six reading frames into amino acids. Create one file
for which you print the six reading frames (Python_08.codons-6frames.nt) and
one file for which you print the translation of the six reading frames
(Python_08.translated.aa). Use the following translation table:

```python
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
```
"""
import sys

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
long_nt_filename = output_prefix + '.orf-longest.nt'

try:    
    fasta_file = open(fasta_filename, 'r')
    codon_file = open(codon_filename, 'w')
    trans_file = open(trans_filename, 'w')

except IOError as error:
    print("Error: " + str(error), file=sys.stderr)
    sys.exit(1)    
    
seq_id = None
seq_string = ''

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
    
codon_length = 3
seq_ids = list()
seq_strings = dict()
for line in fasta_file:
    line = line.rstrip()  # strip of ending \n char

    if line.startswith('>'):
        seq_def = line.lstrip('>').split(' ', maxsplit=1)
        seq_id = seq_def[0]
        seq_strings[seq_id] = {'+':'', '-':''}
        seq_ids.append(seq_id)
        
    else:
        line = line.upper()

        for nucleotide in line:
            if nucleotide not in valid_nucleotides:
                raise Exception("Invalid nucleotide character in {0}: {1}".format(
                    seq_id, nucleotide
                ))

        seq_strings[seq_id]['+'] += line  # j.i.c. the fasta is wrapped

for seq_id in seq_ids:
    seq_strings[seq_id]['-'] = seq_strings[seq_id]['+'].translate(complement_table)

    info = list()  # for storing frame and orf number
    nt_list = list()
    aa_list = list()
    num_translations = 0
    for strand in ('+', '-'):
        seq_string = seq_strings[seq_id][strand]

        for frame in range(codon_length):
            num_orfs = 0
            codons = []
            aminos = []
            for offset in range(0, len(seq_string), codon_length):
                beg = offset + frame  # 'beg' = beginning of codon triplet
                end = beg + codon_length  # 'end' = end of codon triplet

                if end <= len(seq_string):
                    codon = seq_string[beg:end]
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
        frame += (codon_length if info[i] == '-' else 0)  

        codon_file.write('{0}-frame-{1}-orf-{2}-codons\n'.format(seq_id, frame+1, orf+1))
        codon_file.write(' '.join(codons) + '\n')
        trans_file.write('{0}-frame-{1}-orf-{2}-aminos\n'.format(seq_id, frame+1, orf+1))
        trans_file.write(''.join(aminos) + '\n')        



"""
6. Find the longest peptide seq (M => Stop) of all the six translated
reading frames for a single seq. Do this for all the seq records. 
For each seq, print out in FASTA format the six frames of codons to one
file (Python_08.codons-6frames.nt), the translations to a second file
(Python_08.translated.aa), and the single longest translated peptide to a
third file (Python_08.translated-longest.aa).
"""
import sys

try:
    fasta_filename = sys.argv[1]  # raises IndexError if no input

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
    
seq_id = None
seq_string = ''

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
    
codon_length = 3
seq_ids = list()
seq_strings = dict()
for line in fasta_file:
    line = line.rstrip()  # strip of ending \n char

    if line.startswith('>'):
        seq_def = line.lstrip('>').split(' ', maxsplit=1)
        seq_id = seq_def[0]
        seq_strings[seq_id] = {'+':'', '-':''}
        seq_ids.append(seq_id)
        
    else:
        line = line.upper()

        for nucleotide in line:
            if nucleotide not in valid_nucleotides:
                raise Exception("Invalid nucleotide character in {0}: {1}".format(
                    seq_id, nucleotide
                ))

        seq_strings[seq_id]['+'] += line  # j.i.c. the fasta is wrapped

for seq_id in seq_ids:
    seq_strings[seq_id]['-'] = seq_strings[seq_id]['+'].translate(complement_table)

    info = list()  # for storing frame and orf number
    nt_list = list()
    aa_list = list()
    num_translations = 0
    for strand in ('+', '-'):
        seq_string = seq_strings[seq_id][strand]

        for frame in range(codon_length):
            num_orfs = 0
            codons = []
            aminos = []
            for offset in range(0, len(seq_string), codon_length):
                beg = offset + frame  # 'beg' = beginning of codon triplet
                end = beg + codon_length  # 'end' = end of codon triplet

                if end <= len(seq_string):
                    codon = seq_string[beg:end]
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
        
        frame += (codon_length if info[i] == '-' else 0)  

        try:
            first_M = aminos.index('M')
        except ValueError:  # if no match
            # has no Met start codon
            continue  # to the next translation

        if aminos[-1] != '*':  # has no stop codon
            continue  # to the next translation

        orf_codons = codons[first_M:]
        orf_aminos = aminos[first_M:]
        
        codon_file.write('>{0}-frame-{1}-orf-{2}-codons\n'.format(seq_id,
            frame+1, orf+1))
        codon_file.write(' '.join(orf_codons) + '\n')
        trans_file.write('>{0}-frame-{1}-orf-{2}-aminos\n'.format(seq_id,
            frame+1, orf+1))
        trans_file.write(''.join(orf_aminos) + '\n')

        if len(orf_aminos) > longest_length:
            longest_length = len(orf_aminos)
            longest_aminos = orf_aminos
            longest_frame  = frame
            longest_orf    = orf
            
    long_aa_file.write('>{0}-frame-{1}-orf-{2}-aminos\n'.format(seq_id,
        longest_frame+1, longest_orf+1))
    long_aa_file.write(''.join(longest_aminos) + '\n')



"""
7. Finally determine which subset of codons produced the longest peptide for
each seq record. Print this to a fourth file in FASTA format
(Python_08.orf-longest.nt).
"""
import sys

try:
    fasta_filename = sys.argv[1]  # raises IndexError if no input

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
long_nt_filename = output_prefix + '.orf-longest.nt'


try:    
    fasta_file = open(fasta_filename, 'r')
    codon_file = open(codon_filename, 'w')
    trans_file = open(trans_filename, 'w')
    long_aa_file = open(long_aa_filename, 'w')
    long_nt_file = open(long_nt_filename, 'w')
except IOError as error:
    print("Error: " + str(error), file=sys.stderr)
    sys.exit(1)    
    
seq_id = None
seq_string = ''

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
    
codon_length = 3
seq_ids = list()
seq_strings = dict()
for line in fasta_file:
    line = line.rstrip()  # strip of ending \n char

    if line.startswith('>'):
        seq_def = line.lstrip('>').split(' ', maxsplit=1)
        seq_id = seq_def[0]
        seq_strings[seq_id] = {'+':'', '-':''}
        seq_ids.append(seq_id)
        
    else:
        line = line.upper()
        for nucleotide in line:
            if nucleotide not in valid_nucleotides:
                raise Exception("Invalid nucleotide character in {0}: {1}".format(
                    seq_id, nucleotide
                ))

        seq_strings[seq_id]['+'] += line  # j.i.c. the fasta is wrapped

for seq_id in seq_ids:
    seq_strings[seq_id]['-'] = seq_strings[seq_id]['+'].translate(complement_table)

    info = list()  # for storing frame and orf number
    nt_list = list()
    aa_list = list()
    num_translations = 0
    for strand in ('+', '-'):
        seq_string = seq_strings[seq_id][strand]

        for frame in range(codon_length):
            num_orfs = 0
            codons = []
            aminos = []

            for offset in range(0, len(seq_string), codon_length):
                beg = offset + frame  # 'beg' = beginning of codon triplet
                end = beg + codon_length  # 'end' = end of codon triplet

                if end <= len(seq_string):
                    codon = seq_string[beg:end]
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
        
        frame += (codon_length if info[i] == '-' else 0)  

        try:
            first_M = aminos.index('M')
        except ValueError:  # if no match
            # has no Met start codon
            continue  # to the next translation

        if aminos[-1] != '*':  # has no stop codon
            continue  # to the next translation

        orf_codons = codons[first_M:]
        orf_aminos = aminos[first_M:]
        
        codon_file.write('>{0}-frame-{1}-orf-{2}-codons\n'.format(seq_id, frame+1, orf+1))
        codon_file.write(' '.join(orf_codons) + '\n')
        trans_file.write('>{0}-frame-{1}-orf-{2}-aminos\n'.format(seq_id, frame+1, orf+1))
        trans_file.write(''.join(orf_aminos) + '\n')

        if len(orf_aminos) > longest_length:
            longest_length = len(orf_aminos)
            longest_codons = orf_codons
            longest_aminos = orf_aminos
            longest_frame  = frame
            longest_orf    = orf
            
    long_aa_file.write('>{0}-frame-{1}-orf-{2}-aminos\n'.format(seq_id, longest_frame+1, longest_orf+1))
    long_aa_file.write(''.join(longest_aminos) + '\n')
    long_nt_file.write('>{0}-frame-{1}-orf-{2}-codons\n'.format(seq_id, longest_frame+1, longest_orf+1))
    long_nt_file.write(' '.join(longest_codons) + '\n')

