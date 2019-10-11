Python 8 - Data Structures -Problem Set
===================

__Don't forget to use a small test data set when you are testing your code. Make sure you know what the correct answer should be__

1. Take a multi-FASTA [Python_08.fasta](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_08.fasta) file from user input and calculate the nucleotide composition for each sequence. Use a datastructure to keep count. Print out each sequence name and its compostion in this format `seqName\tA_count\tT_count\tG_count\C_count`

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

2. Write a script that takes a multi-FASTA file [Python_08.fasta](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_08.fasta) from user input and breaks each sequence into codons (every three nucleotides is a codon) in just the first reading frame. Your output should look like this 
```
seq1-frame-1-codons
CAT GCT TGA GTC
``` 
Write the output to a file called 'Python_08.codons-frame-1.nt'.

3. Now produce codons in the first three reading frames for each sequence and print out ids and sequence records for each frame and print to a file called 'Python_08.codons-3frames.nt'

For example
```
seq1-frame-1-codons
ATG TTG
seq-frame-2-codons
TGT TGA
``` 

4. Now reverse complement each sequence and print out all six reading frames to a file called 'Python_08.codons-6frames.nt'

5. Translate each of the six reading frames into amino acids. Create one file for which you print the six reading frames (Python_08.codons-6frames.nt) and one file for which you print the translation of the six reading frames (Python_08.translated.aa). Use the following translation table:

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

6. Find the longest peptide sequence (M => Stop) of all the six translated reading frames for a single sequence. Do this for all the sequence records. For each sequence, print out in FASTA format the six frames of codons to one file (Python_08.codons-6frames.nt), the translations to a second file (Python_08.translated.aa), and the single longest translated peptide to a third file (Python_08.translated-longest.aa).

7. Finally determine which subset of codons produced the longest peptide for each sequence record. Print this to a fourth file in FASTA format (Python_08.orf-longest.nt).  
