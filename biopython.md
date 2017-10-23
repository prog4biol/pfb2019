# Biopython

## What is biopython?

Biopython is a collection of python modules that contain code for manipulating biological data. Many handle sequence data and common analysis and processing of the data including reading and writing all common file formats. 

## Installing Biopython

This is very straightforward once you have anaconda or minconda installed. I use miniconda because it's smaller. We are going to use `sudo` because this will give us permission to install in the 'correct' directory python is expecting to find the modules. Other users will be able to use it too. Using `sudo` can cause problems, but it's ok here. You will need the administrator password for the machine. If you don't have this, ask the person who does administration on your machine.

```bash
% sudo conda install biopython
WARNING: Improper use of the sudo command could lead to data loss
or the deletion of important system files. Please double-check your
typing when using sudo. Type "man sudo" for more information.

To proceed, enter your password, or type Ctrl-C to abort.

Password:
Fetching package metadata ...........
Solving package specifications: .

Package plan for installation in environment /anaconda3:

The following NEW packages will be INSTALLED:

    biopython: 1.69-np113py36_0              

The following packages will be UPDATED:

    conda:     4.3.29-py36hbf39572_0 anaconda --> 4.3.30-py36h173c244_0

The following packages will be SUPERSEDED by a higher-priority channel:

    conda-env: 2.6.0-h36134e3_0      anaconda --> 2.6.0-h36134e3_0     

Proceed ([y]/n)? 

conda-env-2.6. 100% |#################################################| Time: 0:00:00   4.02 MB/s
biopython-1.69 100% |#################################################| Time: 0:00:00  21.02 MB/s
conda-4.3.30-p 100% |#################################################| Time: 0:00:00  43.61 MB/s

```



See if the install worked

```python
python3
>>> import Bio
>>> print(Bio.__version__)
1.69
```

If we get no errors, biopython is installed correctly.

## Navigating the BioPython website



## Biopython documentation



## Working with DNA and protein sequences

This is the core of biopython. And uses the Seq object. Seq is part of Bio. This is denoted Bio.Seq

```python
#!/usr/bin/env python3
import Bio.Seq                           # }
seqobj = Bio.Seq.Seq('ATGCGATCGAGC')     # } that's a lot of Seqs
# convert to string with str(seqobj)
seq_str = str(seqobj)
print('{:s} has {:d} nucleotides'.format( seq_str , len(seq_str)))
```

produces 

```
ATGCGATCGAGC has 12 nucleotides
```

### From ... import ...

Another way to import modules is with `from ... import ...` . This saves typing the Class name every time. Bio.Seq is the class name. Bio is the superclass. Seq is a subclass inside Bio. It's written Bio.Seq. Seq has several different subclasses, of which one is called Seq. So we have Bio.Seq.Seq. To make the creation simpler, we call Seq() after we import with `from ... import ...` like this

```python3
#!/usr/bin/env python3
from Bio.Seq import Seq
seqobj=Seq('ATGCGATCGAGC')
seq_str=str(seqobj)
protein = seqobj.translate()
prot_str = str(protein)
print('{:s} translates to {:s}'.format(seq_str,prot_str))
```

produces

```
ATGCGATCGAGC
```

#### Bio.Alphabets

A Seq object likes to know what alphabet it uses A,C,G,T for DNAAlpabet etc. Not essential for most uses.

```
>>> seqobj
Seq('ATG', Alphabet())
>>> from Bio.Alphabet import DNAAlphabet
>>> so=Seq('ATG',DNAAlphabet())
>>> so
Seq('ATG', DNAAlphabet())
>>> so.translate()
Seq('M', ExtendedIUPACProtein())


```

For proteins

```
from Bio.Alphabet import ProteinAlphabet
seqobj = Seq('MGT', ProteinAlphabet())
```



## Read a FASTA file

We were learning how to read a fasta file line by line. SeqIO.parse() is the main method for reading from almost any file format. We'll need a fasta file. We can use Python_05.fasta which looks like this

```
>seq1
AAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGCCACCAATTATGGTGTATGAGTGAATCTCTGGTCCGAGATTCA
CTGAGTAACTGCTGTACACAGTAGTAACACGTGGAGATCCCATAAGCTTCACGTGTGGTCCAATAAAACACTCCGTTGGTCAAC
>seq2
GCCACAGAGCCTAGGACCCCAACCTAACCTAACCTAACCTAACCTACAGTTTGATCTTAACCATGAGGCTGAGAAGCGATGTCCTGACCGGCCTGT
CCTAACCGCCCTGACCTAACCGGCTTGACCTAACCGCCCTGACCTAACCAGGCTAACCTAACCAAACCGTGAAAAAAGGAATCT
>seq3
ATGAAAGTTACATAAAGACTATTCGATGCATAAATAGTTCAGTTTTGAAAACTTACATTTTGTTAAAGTCAGGTACTTGTGTATAATATCAACTAA
AT
>seq4
ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAAACAACATGCCAAATAGAAACGATCAATTCGGCGATGGAAATC
AGAACAACGATCAGTTTGGAAATCAAAATAGAAATAACGGGAACGATCAGTTTAATAACATGATGCAGAATAAAGGGAATAATCAATTTAATCCAG
GTAATCAGAACAGAGGT
```

Get help on the parse() method with 

```
>>> help(SeqIO.parse)

Help on function parse in module Bio.SeqIO:

parse(handle, format, alphabet=None)
    Turns a sequence file into an iterator returning SeqRecords.
    
        - handle   - handle to the file, or the filename as a string
          (note older versions of Biopython only took a handle).
        - format   - lower case string describing the file format.
        - alphabet - optional Alphabet object, useful when the sequence type
          cannot be automatically inferred from the file itself
          (e.g. format="fasta" or "tab")
    
    Typical usage, opening a file to read in, and looping over the record(s):
    
    >>> from Bio import SeqIO
    >>> filename = "Fasta/sweetpea.nu"
    >>> for record in SeqIO.parse(filename, "fasta"):
    ...    print("ID %s" % record.id)
    ...    print("Sequence length %i" % len(record))
    ...    print("Sequence alphabet %s" % record.seq.alphabet)
    ID gi|3176602|gb|U78617.1|LOU78617
    Sequence length 309
    Sequence alphabet SingleLetterAlphabet()

...
```

This uses the old `"..." % var` formatting syntax.

Here's a script to read fasta records and print out some information

```python
#!/usr/bin/env python3
# assumes we are in the pfb2017 directory
from Bio import SeqIO
for seq_record in SeqIO.parse("./files/Python_05.fasta", "fasta"):   # give filename and format
  print('ID',seq_record.id)
  print('Sequence',str(seq_record.seq))
  print('Length',len(seq_record))
    
```

Prints this output

```
ID seq1
Sequence AAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGCCACCAATTATGGTGTATGAGTGAATCTCTGGTCCGAGATTCACTGAGTAACTGCTGTACACAGTAGTAACACGTGGAGATCCCATAAGCTTCACGTGTGGTCCAATAAAACACTCCGTTGGTCAAC
Length 180
ID seq2
Sequence GCCACAGAGCCTAGGACCCCAACCTAACCTAACCTAACCTAACCTACAGTTTGATCTTAACCATGAGGCTGAGAAGCGATGTCCTGACCGGCCTGTCCTAACCGCCCTGACCTAACCGGCTTGACCTAACCGCCCTGACCTAACCAGGCTAACCTAACCAAACCGTGAAAAAAGGAATCT
Length 180
ID seq3
Sequence ATGAAAGTTACATAAAGACTATTCGATGCATAAATAGTTCAGTTTTGAAAACTTACATTTTGTTAAAGTCAGGTACTTGTGTATAATATCAACTAAAT
Length 98
ID seq4
Sequence ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAAACAACATGCCAAATAGAAACGATCAATTCGGCGATGGAAATCAGAACAACGATCAGTTTGGAAATCAAAATAGAAATAACGGGAACGATCAGTTTAATAACATGATGCAGAATAAAGGGAATAATCAATTTAATCCAGGTAATCAGAACAGAGGT
Length 209

```



To read sequences from a genbank file instead, not much changes.

```python
#!/usr/bin/env python3
from Bio import SeqIO
for seq_record in SeqIO.parse("test_genome.gb", "genbank"):
  print('ID',seq_record.id)
  print('Sequence',str(seq_record.seq))
  print('Length',len(seq_record))
```



## File Format Conversions



## Parsing BLAST output



## Manipulation of Multiple Sequence Alignments



## Retrieving annotations from GenBank file



## Other Cool Things