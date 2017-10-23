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
print(seq_str)
```

produces

```
ATGCGATCGAGC
```





## Querying a local FASTA



## Creating a sequence record



## File Format Conversions



## Parsing BLAST output



## Manipulation of Multiple Sequence Alignments



## Retrieving annotations from GenBank file



## Other Cool Things