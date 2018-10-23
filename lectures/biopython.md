# Biopython

## What is biopython?

Biopython is a collection of python modules that contain code for manipulating biological data. Many handle sequence data and common analysis and processing of the data including reading and writing all common file formats. Biopython will also run blast for you and parse the output into objects inside your script. This requires just a few lines of code.

## Installing Biopython

This is very straightforward once you have anaconda or minconda installed. I use miniconda because it's smaller. We are going to use `sudo`, because this will give us permission to install in the 'correct' directory python is expecting to find the modules. Other users will be able to use it too. Using `sudo` can cause problems, but it's ok here. You will need the administrator password for the machine. If you don't have this, ask the person who does administration on your machine.

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

## Biopython documentation

[Biopython wiki page](http://biopython.org/)

[Getting started](http://biopython.org/wiki/Category%3AWiki_Documentation)

[Biopython tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html#chapter:Bio.SeqIO)

[Complete tree of Biopython Classes](http://biopython.org/DIST/docs/api/Bio-module.html)




## Working with DNA and protein sequences

This is the core of biopython. And uses the Seq object. Seq is part of Bio. This is denoted Bio.Seq

```python
#!/usr/bin/env python3
import Bio.Seq                          
seqobj = Bio.Seq.Seq('ATGCGATCGAGC')     
# convert to string with str(seqobj)
seq_str = str(seqobj)
print('{} has {} nucleotides'.format( seq_str , len(seq_str)))
```

produces 

```
ATGCGATCGAGC has 12 nucleotides
```

### From ... import ...

Another way to import modules is with `from ... import ...` . This saves typing the Class name every time. Bio.Seq is the class name. Bio is the superclass. Seq is a subclass inside Bio. It's written Bio.Seq. Seq has several different subclasses, of which one is called Seq. So we have Bio.Seq.Seq. To make the creation simpler, we call Seq() after we import with `from ... import ...` like this

```python
#!/usr/bin/env python3
from Bio.Seq import Seq
seqobj=Seq('ATGCGATCGAGC')
seq_str=str(seqobj)
protein = seqobj.translate()
prot_str = str(protein)
print('{} translates to {}'.format(seq_str,prot_str))
```

produces

```
ATGCGATCGAGC translates to MRSS
```

#### Bio.Alphabets

Visit biopython.org to read about [Sequences and Alphabets](http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc17)

A Seq object likes to know what alphabet it uses A,C,G,T for DNAAlpabet etc. Not essential for most uses, but prevents you trying to translate a protein sequence!

__Specific Alphabets__

For DNA

```python
>>> seqobj
Seq('ATG', Alphabet())
>>> from Bio.Alphabet import DNAAlphabet
>>> seqobj=Seq('ATG',DNAAlphabet())
>>> seqobj
Seq('ATG', DNAAlphabet())
>>> seqobj.translate()
Seq('M', ExtendedIUPACProtein())
```

For proteins

```python
>>> seqobj = Seq('MGT')
>>> seqobj.translate()
Seq('X', ExtendedIUPACProtein())
```

> 'X' That's not right! Wait! Why did python let us translate MGT? It's not DNA?


```python
>>> from Bio.Alphabet import ProteinAlphabet
>>> seqobj = Seq('MGT', ProteinAlphabet())
>>> seqobj.translate()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/smr/anaconda3/envs/py3.6/lib/python3.5/site-packages/Bio/Seq.py", line 1059, in translate
    raise ValueError("Proteins cannot be translated!")
ValueError: Proteins cannot be translated!
```

> That's better.

### Extracting a subsequence

You can use a range [0:3] to get the first codon

Visit biopython.org to read about [Slicing a sequence](http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc19)

```python
>>> seqobj=Seq('ATGCGATCGAGC')
>>> seqobj[0:3]
Seq('ATG', Alphabet())
```

Let's use Regular expressions in conjunction with BioPython to get every codon

```python
>>> seqobj=Seq('ATGCGATCGAGC')
>>> import re
>>> for codon in re.findall(r"(.{3})",str(seqobj)):
...   print(codon)
...
ATG
CGA
TCG
AGC
>>>
```



## Read a FASTA file

We were learning how to read a fasta file line by line. SeqIO.parse() is the main method for reading from almost any file format. We'll need a fasta file. We can use [seq.nt.fa](https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/seq.nt.fa) which looks like this

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

```python
>>> from Bio import SeqIO
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
    
...
```

Here's a script to read fasta records and print out some information

```python
#!/usr/bin/env python3
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

Here is another example of opening a FASTA file, retrieving each sequence record, and doing something the data.

```python

#!/usr/bin/env python3
from Bio import SeqIO
filename = "files/seq.nt.fa"
for seq_record in SeqIO.parse(filename, "fasta"):   
  print('ID',seq_record.id)
  print('len {}'.format(len(seq_record)))
  print('alphabet {}'.format(seq_record.alphabet)
  print('translation {}'.format(seq_record.seq.translate(to_stop=False)))
```
> We added the translation of the DNA sequence into protein
Output:  

```bash
ID seq1
len 180
alphabet SingleLetterAlphabet()
translation KSSSR*CDRWR*SKCPMGHQLWCMSESLVRDSLSNCCTQ**HVEIP*ASRVVQ*NTPLVN
ID seq2
len 180
alphabet SingleLetterAlphabet()
translation ATEPRTPT*PNLT*PTV*S*P*G*EAMS*PACPNRPDLTGLT*PP*PNQANLTKP*KKES
ID seq3
len 98
alphabet SingleLetterAlphabet()
translation MKVT*RLFDA*IVQF*KLTFC*SQVLVYNIN*
ID seq4
len 209
alphabet SingleLetterAlphabet()
translation MLTKVSVRTCR*ATLKKETTCQIETINSAMEIRTTISLEIKIEITGTISLIT*CRIKGIINLIQVIRTE
```


#### Convert fasta file to python dictionary in one line

There are three ways of doing this that use up more memory if you want more flexibility. `Bio.SeqIO.to_dict()` is the most flexible but also reads the entire fasta file into memory as a python dictionary so might take a lot of time and memory.

```
>>> id_dict = SeqIO.to_dict(SeqIO.parse('files/Python_05.fasta', 'fasta'))
>>> id_dict
{'seq1': SeqRecord(seq=Seq('AAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGC...AAC', SingleLetterAlphabet()), id='seq1', name='seq1', description='seq1', dbxrefs=[]), 'seq2': SeqRecord(seq=Seq('GCCACAGAGCCTAGGACCCCAACCTAACCTAACCTAACCTAACCTACAGTTTGA...TCT', SingleLetterAlphabet()), id='seq2', name='seq2', description='seq2', dbxrefs=[]), 'seq3': SeqRecord(seq=Seq('ATGAAAGTTACATAAAGACTATTCGATGCATAAATAGTTCAGTTTTGAAAACTT...AAT', SingleLetterAlphabet()), id='seq3', name='seq3', description='seq3', dbxrefs=[]), 'seq4': SeqRecord(seq=Seq('ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAA...GGT', SingleLetterAlphabet()), id='seq4', name='seq4', description='seq4', dbxrefs=[])}

```


Let's retrieve some info from our new dictionary

```python
>>> id_dict['seq4']
SeqRecord(seq=Seq('ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAA...GGT', SingleLetterAlphabet()), id='seq4', name='seq4', description='seq4', dbxrefs=[])
>>> id_dict['seq4'].seq
Seq('ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAA...GGT', SingleLetterAlphabet())
>>> str(id_dict['seq4'].seq)
'ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAAACAACATGCCAAATAGAAACGATCAATTCGGCGATGGAAATCAGAACAACGATCAGTTTGGAAATCAAAATAGAAATAACGGGAACGATCAGTTTAATAACATGATGCAGAATAAAGGGAATAATCAATTTAATCCAGGTAATCAGAACAGAGGT'
>>>
```
> need to use this format to get the string of the sequence: `str(id_dict['seq4'].seq)`



### Seq methods

Visit biopython.org to read how [Sequences act like strings](http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc18)

```python
seqobj.count("A")  # counts how many As are in sequence
seqobj.find("ATG") # find coordinate of ATG (-1 for not found)
```



### SeqRecord objects

SeqIO.Parse generates Bio.SeqRecord.SeqRecord objects. These are annotated Bio.Seq.Seq objects. 

Main attributes:

- id - Identifier such as a locus tag (string)
- seq - The sequence itself (Seq object or similar)

Access these with `sr.id` and `sr.seq`. `str(sr.seq)` gets the actual sequence string.

Additional attributes:

- name - Sequence name, e.g. gene name (string)
- description - Additional text (string)
- dbxrefs - List of database cross references (list of strings)
- features - Any (sub)features defined (list of SeqFeature objects)
- annotations - Further information about the whole sequence (dictionary). Most entries are strings, or lists of strings.
- letter_annotations - Per letter/symbol annotation (restricted dictionary). This holds Python sequences (lists, strings or tuples) whose length matches that of the sequence. A typical use would be to hold a list of integers representing sequencing quality scores, or a string representing the secondary structure.


SeqRecord objects have .format() to convert to a string in various formats

```python
>>> seq.format('fasta')
'>seq1\nAAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGCCACCAA\nTTATGGTGTATGAGTGAATCTCTGGTCCGAGATTCACTGAGTAACTGCTGTACACAGTAG\nTAACACGTGGAGATCCCATAAGCTTCACGTGTGGTCCAATAAAACACTCCGTTGGTCAAC\n'

```



## Retrieving annotations from GenBank file

To read sequences from a genbank file instead, not much changes.

```python
#!/usr/bin/env python3
from Bio import SeqIO
for seq_record in SeqIO.parse("files/sequence.gb", "genbank"):
  print('ID',seq_record.id)
  print('Sequence',str(seq_record.seq)[0:60],'...')
  print('Length',len(seq_record))
```

Output: 
```
ID NM_204156.1
Sequence GGCCCCGGCCGGTGGGGCGGGTTGCGTTGCGCTGCGCGGCGGTAGGGTCTGCGGCCGTGG ...
Length 3193
```


## File Format Conversions

Many are straightforward, others are a little more complicated because the alphabet can't be determined from the data. It's usually easier to go from richer formats to simpler ones.

```python
#!/usr/bin/env python3
from Bio import SeqIO
fasta_records = SeqIO.parse("files/seq.nt.fa", "fasta")  
count = SeqIO.write(seq_records , './files/seqs.tab' , 'tab')
```



Produces

```
% more seqs.tab
seq1    AAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGCCACCAATTATGGTGTATGAGTGAATCTCTGGTCCGAGATTCACTGAGTAACTGCTGTACACAGTAGTAACACGTGGAGATCCCATAAGCTTCACGTGTGGTCCAATAAAACACTCCGTTGGTCAAC
seq2    GCCACAGAGCCTAGGACCCCAACCTAACCTAACCTAACCTAACCTACAGTTTGATCTTAACCATGAGGCTGAGAAGCGATGTCCTGACCGGCCTGTCCTAACCGCCCTGACCTAACCGGCTTGACCTAACCGCCCTGACCTAACCAGGCTAACCTAACCAAACCGTGAAAAAAGGAATCT
seq3    ATGAAAGTTACATAAAGACTATTCGATGCATAAATAGTTCAGTTTTGAAAACTTACATTTTGTTAAAGTCAGGTACTTGTGTATAATATCAACTAAAT
seq4    ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAAACAACATGCCAAATAGAAACGATCAATTCGGCGATGGAAATCAGAACAACGATCAGTTTGGAAATCAAAATAGAAATAACGGGAACGATCAGTTTAATAACATGATGCAGAATAAAGGGAATAATCAATTTAATCCAGGTAATCAGAACAGAGGT
```

Even easier is the convert() method. Let's try fastq to fasta.

```python
#!/usr/bin/env python3
from Bio import SeqIO
count = SeqIO.convert('./files/pfb.fastq', 'fastq', './files/pfb.converted.fa', 'fasta')
```

Hmm, was that easy or what??!??!!?

## Parsing BLAST output

For simple BLAST parsing, ask for output format in tab-separated columns (`-outfmt 6` or `-outfmt 7`) Both these formats are customizable! See next section. 

If you want to parse the full output of blast with biopython, it's best to work with XML formatted BLAST output `-outfmt 5`. It breaks the parsing method less easily. Code is stable for working with NCBI blast.

You can get biopython to run the blast for you too. See `Bio.NCBIWWW`

To parse the output, you'll write something like this

```python

>>> from Bio.Blast import NCBIXML
>>> result_handle = open("my_blast.xml")
>>> blast_records = NCBIXML.parse(result_handle)
>>> for blast_record in blast_records:
>>>   for alignment in blast_record.alignments:
>>>     for hsp in alignment.hsps:
>>>        if hsp.expect < 1e-10:
>>>           print('id', alignment.title)
>>>           print('E = ' , hsp.expect)

```



### You can also use the more general SearchIO

The code exists, but is likely to change over the next few versions of biopython.

It will handle other sequence search tools such as FASTA, HMMER etc as well as BLAST. ReturnsQuery objects that contain one or more Hit objects that contain one or more HSP objects, like in a blast report. Can handle blast tab-separated text output. 

You'll write something like this

```python
>>> from Bio import SearchIO
>>> idx = SearchIO.index('tab_2226_tblastn_001.txt', 'blast-tab')
>>> sorted(idx.keys())
['gi|11464971:4-101', 'gi|16080617|ref|NP_391444.1|']
>>> idx['gi|16080617|ref|NP_391444.1|']
QueryResult(id='gi|16080617|ref|NP_391444.1|', 3 hits)
>>> idx.close()

```



## There are many other uses for Biopython

* reading multiple sequence alignments
* searching on remote biological sequence databases
* working with protein structure (requires numpy to be installed)
* biochemical pathways (KEGG)
* drawing pictures of genome and sequence features
* population genetics

## Why use biopython

Massive time saver once you know your way around the classes.

Reuse someone else's code. Very quick parsing of many common file formats.

Clean code.
