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
print('{} has {} nucleotides'.format( seqobj , len(seqobj)))
```
> Note: Sometimes you might have to convert an object to string to get sequence `seq_str = str(seqobj)`. The Seq Object predicts that if a user writes `print(seqobj)` they will want to print the sequence string not the entire Seq Object. Likewise, the Seq Object predicts that if a user writes `len(seqobj)` they will want to caluculate the length of the sequence not the length of the entire Seq Object


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
protein = seqobj.translate()
print('{} translates to {}'.format(seqobj,protein))
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
>>> print(seqobj[0:3])
ATG
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
> The Seq Object has not predicted that if we use seqobj as input to `findall()` that we want to search just the sequence. But it has predicted that if we use the `str()` we want to return the sequence that is contained within our object.

__Data types__

The Seq Object predicts that we want a string when we `print()` our seqobj or if we try to caculate `len()` or if we try to take a substr `seqobj[0:3]` of our seqobj. The authors have coded this functionality into the Class rules. They did not predict, or write into the Class rules that if we use `findall()` that we want to search just the sequence. The Class does not know how to handle this. But it has predicted that if we use the `str()` we want to return the sequence that is contained within our object.

```python
>>> seqobj=Seq('ATGCGATCGAGC')
>>> type(seqobj)
<class 'Bio.Seq.Seq'>
>>> str(seqobj)
'ATGCGATCGAGC'
>>> type(str(seqobj))
<class 'str'>
```

## Read a FASTA file

Earlier in the course were learning how to read a fasta file line by line. We are going to go over the BioPython way to do this. `SeqIO.parse()` is the main method for reading from almost any file format. The examples will use [seq.nt.fa](https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/seq.nt.fa): 

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
for seq_record in SeqIO.parse("../files/seq.nt.fa", "fasta"):   # give filename and format
  print('ID',seq_record.id)
  print('Sequence',seq_record.seq)
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

__How do you know what methods and attributes are available?__

In the last example we used the `id()` and `seq()`. How do we find out that we could use these or what are other options are?

You can use option+tab in the interpreter to find out. Type the object then a '.' then option+tab. You will get a list of attributes and methods you can use with this specific object.

```python
>>> from Bio import SeqIO
>>> for seq_record in SeqIO.parse("../files/seq.nt.fa", "fasta"):
...   print(seq_record.
seq_record.annotations          seq_record.id                   seq_record.seq
seq_record.dbxrefs              seq_record.letter_annotations   seq_record.translate(
seq_record.description          seq_record.lower(               seq_record.upper(
seq_record.features             seq_record.name
seq_record.format(              seq_record.reverse_complement(
...   print(seq_record.

```




__Seq Object vs SeqRecord Object__

The Seq Object and the SeqRecord Object two Objects are not the same. As you have seen we can directly print the sequence that is stored within a `Seq` Object. But this is not possible with `SeqRecord`. You need to use the `seq()` method to retrieve just the sequence bit of the `SeqRecord` Object.


```python
>>> from Bio.Seq import Seq
>>> seqobj=Seq('ATGCGATCGAGC')
>>> print(seqobj)
ATGCGATCGAGC
>>>
>>> type(seqobj)
<class 'Bio.Seq.Seq'>
>>>
>>> from Bio import SeqIO
>>> filename = "../files/seq.nt.fa"
>>> for seq_record in SeqIO.parse(filename, "fasta"):
...   type(seq_record)
...   print(seq_record.seq)
...   print(seq_record)
...
<class 'Bio.SeqRecord.SeqRecord'>
AAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGCCACCAATTATGGTGTATGAGTGAATCTCTGGTCCGAGATTCACTGAGTAACTGCTGTACACAGTAGTAACACGTGGAGATCCCATAAGCTTCACGTGTGGTCCAATAAAACACTCCGTTGGTCAAC
ID: seq1
Name: seq1
Description: seq1
Number of features: 0
Seq('AAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGC...AAC', SingleLetterAlphabet())
```


Here is another example of opening a FASTA file, retrieving each sequence record, and doing something the data. We are going to translate each sequence record

```python

#!/usr/bin/env python3
from Bio import SeqIO
filename = "../files/seq.nt.fa"
for seq_record in SeqIO.parse(filename, "fasta"):   
  print('ID',seq_record.id)
  print('len {}'.format(len(seq_record)))
  print('alphabet {}'.format(seq_record.seq.alphabet))
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


#### Convert FASTA file to Python dictionary in one line

`Bio.SeqIO.to_dict()` reads the entire FASTA file into memory and stores the contents in a dictionary.  


```
>>> id_dict = SeqIO.to_dict(SeqIO.parse('../files/seq.nt.fa', 'fasta'))
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

OR, as mentioned earlier in the interpreter you can use option+tab to find out what methods are available:

```python
>>> seqobj=Seq('ATGCGATCGAGC')
>>> seqobj.
seqobj.alphabet             seqobj.find(                seqobj.rstrip(              seqobj.transcribe(
seqobj.back_transcribe(     seqobj.lower(               seqobj.split(               seqobj.translate(
seqobj.complement(          seqobj.lstrip(              seqobj.startswith(          seqobj.ungap(
seqobj.count(               seqobj.reverse_complement(  seqobj.strip(               seqobj.upper(
seqobj.count_overlap(       seqobj.rfind(               seqobj.tomutable(
seqobj.endswith(            seqobj.rsplit(              seqobj.tostring(
>>> seqobj.

```

AND, you can use the help() in the interpreter to find out more:  

```python
>>> help(seqobj.count_overlap)
Help on method count_overlap in module Bio.Seq:

count_overlap(sub, start=0, end=9223372036854775807) method of Bio.Seq.Seq instance
    Return an overlapping count.

    For a non-overlapping search use the count() method.

    Returns an integer, the number of occurrences of substring
    argument sub in the (sub)sequence given by [start:end].
    Optional arguments start and end are interpreted as in slice
    notation.

    Arguments:
     - sub - a string or another Seq object to look for
     - start - optional integer, slice start
     - end - optional integer, slice end

    e.g.

    >>> from Bio.Seq import Seq
    >>> print(Seq("AAAA").count_overlap("AA"))
    3
    >>> print(Seq("ATATATATA").count_overlap("ATA"))
    4
    >>> print(Seq("ATATATATA").count_overlap("ATA", 3, -1))
    1

    Where substrings do not overlap, should behave the same as
    the count() method:
:
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

In the interpreter:

```python
...   seq_record.
seq_record.annotations          seq_record.id                   seq_record.seq
seq_record.dbxrefs              seq_record.letter_annotations   seq_record.translate(
seq_record.description          seq_record.lower(               seq_record.upper(
seq_record.features             seq_record.name
seq_record.format(              seq_record.reverse_complement(
```



## Retrieving annotations from GenBank file

To read sequences from a genbank file instead, not much changes.

```python
#!/usr/bin/env python3
from Bio import SeqIO
for seq_record in SeqIO.parse("../files/sequence.gb", "genbank"):
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
fasta_records = SeqIO.parse("../files/seq.nt.fa", "fasta")  
count = SeqIO.write(fasta_records , '../files/seqs.tab' , 'tab')
```



Produces

```
% more seqs.tab
seq1    AAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGCCACCAATTATGGTGTATGAGTGAATCTCTGGTCCGAGATTCACTGAGTAACTGCTGTACACAGTAGTAACACGTGGAGATCCCATAAGCTTCACGTGTGGTCCAATAAAACACTCCGTTGGTCAAC
seq2    GCCACAGAGCCTAGGACCCCAACCTAACCTAACCTAACCTAACCTACAGTTTGATCTTAACCATGAGGCTGAGAAGCGATGTCCTGACCGGCCTGTCCTAACCGCCCTGACCTAACCGGCTTGACCTAACCGCCCTGACCTAACCAGGCTAACCTAACCAAACCGTGAAAAAAGGAATCT
seq3    ATGAAAGTTACATAAAGACTATTCGATGCATAAATAGTTCAGTTTTGAAAACTTACATTTTGTTAAAGTCAGGTACTTGTGTATAATATCAACTAAAT
seq4    ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAAACAACATGCCAAATAGAAACGATCAATTCGGCGATGGAAATCAGAACAACGATCAGTTTGGAAATCAAAATAGAAATAACGGGAACGATCAGTTTAATAACATGATGCAGAATAAAGGGAATAATCAATTTAATCCAGGTAATCAGAACAGAGGT
```

Even easier is the convert() method. Let's try FASTQ to FASTA.

```python
#!/usr/bin/env python3
from Bio import SeqIO
count = SeqIO.convert('../files/pfb.fastq', 'fastq', '../files/pfb.converted.fa', 'fasta')
```

Was that easy or what??!??!!?

## Parsing BLAST output

For simple parsing, or non BioPython parsing of NCBI BLAST results, use output formated in tab-separated columns (`-outfmt 6` or `-outfmt 7`) Both these formats are customizable when running the BLAST locally.

If you want to parse the full output of BLAST with biopython, it's necessary work with __XML__ formatted BLAST output `-outfmt 5`.

You can get biopython to run the blast for you too. See `Bio.NCBIWWW`

To parse the output, you'll write something like this

```python
from Bio.Blast import NCBIXML
result_handle = open("UTKBKAM5014-Alignment.xml")
blast_records = NCBIXML.parse(result_handle)
for blast_record in blast_records:
   query_id = blast_record.query_id
   for alignment in blast_record.alignments:
     for hsp in alignment.hsps:
        if hsp.expect < 1e-10:
           print('qid:' , query_id , 'hit_id:' , alignment.title, 'E:' , hsp.expect )
```

Output:

```
qid: Query_26141 hit_id: sp|Q13547.1| RecName: Full=Histone deacetylase 1; Short=HD1 [Homo sapiens] >sp|Q5RAG0.1| RecName: Full=Histone deacetylase 1; Short=HD1 [Pongo abelii] E: 0.0
qid: Query_26141 hit_id: sp|O09106.1| RecName: Full=Histone deacetylase 1; Short=HD1 [Mus musculus] E: 0.0
qid: Query_26141 hit_id: sp|Q4QQW4.1| RecName: Full=Histone deacetylase 1; Short=HD1 [Rattus norvegicus] E: 0.0
qid: Query_26141 hit_id: sp|Q32PJ8.1| RecName: Full=Histone deacetylase 1; Short=HD1 [Bos taurus] E: 0.0
qid: Query_26141 hit_id: sp|P56517.1| RecName: Full=Histone deacetylase 1; Short=HD1 [Gallus gallus] E: 0.0
qid: Query_26141 hit_id: sp|O42227.1| RecName: Full=Probable histone deacetylase 1-B; Short=HD1-B; AltName: Full=RPD3 homolog [Xenopus laevis] E: 0.0
...

```


About BLAST Search Report and BioPython:
 - `blast_records` (type <class 'generator'>) can contain handle multiple queries (the sequence you are using as input)
 - The results for each query are considered a `blast_record` (<class Bio.Blast.Record.Blast>)
 - Each `blast_record`  will have info about the query, like blast_record.query_id
 - Each `blast_record` will have information about each hit.
 - A Hit is considered an `alignment` (<class 'Bio.Blast.Record.Alignment'>)
 - An `alignment` has the following info: alignment.accession, alignment.hit_id, alignment.length, alignment.hit_def, alignment.hsps, alignment.title
 - Each `alignment` will have 1 or more `hsp` (<class 'Bio.Blast.Record.HSP'>). 
 - An HSP is a "high scoring pair" or a series of smaller alignments that make up the complete alignment.
 - `hsp` have the following info: hsp.align_length, hsp.frame, hsp.match, hsp.query, hsp.sbjct, hsp.score, hsp.bits            hsp.gaps, hsp.num_alignments, hsp.query_end, hsp.sbjct_end, hsp.strand, hsp.expect, hsp.identities, hsp.positives, hsp.query_start, hsp.sbjct_start
 
   
   ![NCBI BLAST HIT ALIGNMENT](../images/NCBIBLAST.hit.aln.png)
 


Sample of BLAST XML output:  

```xml
<Iteration>
  <Iteration_iter-num>1</Iteration_iter-num>
  <Iteration_query-ID>Query_26141</Iteration_query-ID>
  <Iteration_query-def>CAG46518.1 HDAC1 [Homo sapiens]</Iteration_query-def>
  <Iteration_query-len>482</Iteration_query-len>
<Iteration_hits>
<Hit>
  <Hit_num>1</Hit_num>
  <Hit_id>sp|Q13547.1|</Hit_id>
  <Hit_def>RecName: Full=Histone deacetylase 1; Short=HD1 [Homo sapiens] &gt;sp|Q5RAG0.1| RecName: Full=Histone deacetylase 1; Short=HD1 [Pongo abelii]</Hit_def>
  <Hit_accession>Q13547</Hit_accession>
  <Hit_len>482</Hit_len>
  <Hit_hsps>
    <Hsp>
      <Hsp_num>1</Hsp_num>
      <Hsp_bit-score>1008.82</Hsp_bit-score>
      <Hsp_score>2607</Hsp_score>
      <Hsp_evalue>0</Hsp_evalue>
      <Hsp_query-from>1</Hsp_query-from>
      <Hsp_query-to>482</Hsp_query-to>
      <Hsp_hit-from>1</Hsp_hit-from>
      <Hsp_hit-to>482</Hsp_hit-to>
      <Hsp_query-frame>0</Hsp_query-frame>
      <Hsp_hit-frame>0</Hsp_hit-frame>
      <Hsp_identity>482</Hsp_identity>
      <Hsp_positive>482</Hsp_positive>
      <Hsp_gaps>0</Hsp_gaps>
      <Hsp_align-len>482</Hsp_align-len>
      <Hsp_qseq>MAQTQGTRRKVCYYYDGDVGNYYYGQGHPMKPHRIRMTHNLLLNYGLYRKMEIYRPHKANAEEMTKYHSDDYIKFLRSIRPDNMSEYSKQMQRFNVGEDCPVFDGLFEFCQLSTGGSVASAVKLNKQQTDIAVNWAGGLHHAKKSEASGFCYVNDIVLAILELLKYHQRVLYIDIDIHHGDGVEEAFYTTDRVMTVSFHKYGEYFPGTGDLRDIGAGKGKYYAVNYPLRDGIDDESYEAIFKPVMSKVMEMFQPSAVVLQCGSDSLSGDRLGCFNLTIKGHAKCVEFVKSFNLPMLMLGGGGYTIRNVARCWTYETAVALDTEIPNELPYNDYFEYFGPDFKLHISPSNMTNQNTNEYLEKIKQRLFENLRMLPHAPGVQMQAIPEDAIPEESGDEDEDDPDKRISICSSDKRIACEEEFSDSEEEGEGGRKNSSNFKKAKRVKTEDEKEKDPEEKKEVTEEEKTKEEKPEAKGVKEEVKLA</Hsp_qseq>
      <Hsp_hseq>MAQTQGTRRKVCYYYDGDVGNYYYGQGHPMKPHRIRMTHNLLLNYGLYRKMEIYRPHKANAEEMTKYHSDDYIKFLRSIRPDNMSEYSKQMQRFNVGEDCPVFDGLFEFCQLSTGGSVASAVKLNKQQTDIAVNWAGGLHHAKKSEASGFCYVNDIVLAILELLKYHQRVLYIDIDIHHGDGVEEAFYTTDRVMTVSFHKYGEYFPGTGDLRDIGAGKGKYYAVNYPLRDGIDDESYEAIFKPVMSKVMEMFQPSAVVLQCGSDSLSGDRLGCFNLTIKGHAKCVEFVKSFNLPMLMLGGGGYTIRNVARCWTYETAVALDTEIPNELPYNDYFEYFGPDFKLHISPSNMTNQNTNEYLEKIKQRLFENLRMLPHAPGVQMQAIPEDAIPEESGDEDEDDPDKRISICSSDKRIACEEEFSDSEEEGEGGRKNSSNFKKAKRVKTEDEKEKDPEEKKEVTEEEKTKEEKPEAKGVKEEVKLA</Hsp_hseq>
      <Hsp_midline>MAQTQGTRRKVCYYYDGDVGNYYYGQGHPMKPHRIRMTHNLLLNYGLYRKMEIYRPHKANAEEMTKYHSDDYIKFLRSIRPDNMSEYSKQMQRFNVGEDCPVFDGLFEFCQLSTGGSVASAVKLNKQQTDIAVNWAGGLHHAKKSEASGFCYVNDIVLAILELLKYHQRVLYIDIDIHHGDGVEEAFYTTDRVMTVSFHKYGEYFPGTGDLRDIGAGKGKYYAVNYPLRDGIDDESYEAIFKPVMSKVMEMFQPSAVVLQCGSDSLSGDRLGCFNLTIKGHAKCVEFVKSFNLPMLMLGGGGYTIRNVARCWTYETAVALDTEIPNELPYNDYFEYFGPDFKLHISPSNMTNQNTNEYLEKIKQRLFENLRMLPHAPGVQMQAIPEDAIPEESGDEDEDDPDKRISICSSDKRIACEEEFSDSEEEGEGGRKNSSNFKKAKRVKTEDEKEKDPEEKKEVTEEEKTKEEKPEAKGVKEEVKLA</Hsp_midline>
    </Hsp>
  </Hit_hsps>
</Hit>
<Hit>
  <Hit_num>2</Hit_num>
  <Hit_id>sp|O09106.1|</Hit_id>
  <Hit_def>RecName: Full=Histone deacetylase 1; Short=HD1 [Mus musculus]</Hit_def>
  <Hit_accession>O09106</Hit_accession>
  <Hit_len>482</Hit_len>
  <Hit_hsps>
    <Hsp>
      <Hsp_num>1</Hsp_num>
  ...

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
