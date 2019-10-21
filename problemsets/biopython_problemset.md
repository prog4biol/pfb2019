# Biopython problem set

## Install Biopython on your machine

```
conda install biopython
```

## FASTA Parser

1. Create a new FASTA parser that uses BioPython to get the sequence name, description, and sequence.
2. Add in some code to print out stats about your FASTA records in your mult-FASTA file:
  1. total number of sequences
  2. total number of nucleotides
  3. average length of sequences
  4. shortest seqeunce length
  5. longest seqeunce length
  6. average GC content
  7. highest GC content
  8. lowest GC content
  ```
  seqeunce count:
  total number of nucleotides:
  avg len:
  shortest len:
  longest len:
  avg GC content:
  lowest GC content:
  highest GC content:

  ```
  
3. use a small test set
4. Run your code on https://github.com/prog4biol/pfb2019/blob/master/files/Python_08.fasta

## Parsing BLAST output
### Preparation for problem

Preparation:

1.  Download uniprot_sprot using the Unix command 'wget':

```
wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
```
**Make sure to not add this to your gitHub Repository. It is tooooo big and with cause problems**

2. Unzip the file using the Unix command 'gunzip':

```
gunzip uniprot_sprot.fasta.gz
```
This will create a file `uniprot_sprot.fasta`

**Do not add uniprot_sprot.fasta to your github repo. It is too big.*** To be safe, find your .gitignore in the root of your github repository. Add `uniprot_sprot.fasta*` anywhere in the file. Make sure to add this file to our index as you are updating your repo.


3. What does the file contain? How many records? Does it look intact? How do you know?

Extract IDs from fasta file

1. with the `Bio.SeqIO` module, generate a list of all the IDs in the fasta file. How many are there?

2. Make a list of all the descriptions. The description field almost always has a field OS=... that includes a species or strain designation. Here's an example

```
sp|A9N862|AAEB_SALPB p-hydroxybenzoic acid efflux pump subunit AaeB OS=Salmonella paratyphi B (strain ATCC BAA-1250 / SPB7) GN=aaeB PE=3 SV=1
```

Here the genus is _Salmonella_ and the species is _paratyphi_. There is also a strain 'B (strain ATCC BAA-1250 / SPB7). You can ignore this part. Using regular expressions, extract just the genus and species  and count the number of sequences present for that genus/species combination. List comprehensions make this kind of data processing quick to code, but you might want to start by going step by step in a for loop.

3. Make a new fasta file of all the sequences containing the species 'Salmonella paratyphi B'. Include the 'B' for this part of the exercise. Call this protein file s_paratyphi.prot.fa. You'll want to loop through all the sequence records, extract the description, find matches to 'Salmonella paratyphi B' and convert to fasta.

__For extra credit__
These questions will take some research and set up. Spend some time reading about how to run blast and ask for help as needed.
1. Blast this protein against the S. paratyphi B proteins. You can do this remotely or locally with a blast binary or with biopython.
2. Print the E-value and the score and the length of the alignment and the % similiarity (not % identity)

__Install NCBI Blast+__
1. [Download NCBI BLAST+](https://lmgtfy.com/?q=download+ncbi+blast&s=g&t=w)
2. Find the ftp link to the executables on the page you found in your google search [ BLAST+ executables](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download) 
3. `Installers and source code are available from ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ .`
4. Make sure you are a guest user, click continue
5. Since we are using Macs, click on the `ncbi-blast-2.6.0+.dmg`
6. continue, continue, agree, install
7. Now in a NEW terminal window, you will have the blast executables available. (blastn, blastx, tblastn, tblastx, blastp, makeblastdb, blastdbcmd)

__Run BLAST+__
1. First format you FASTA file so that BLAST+ can use it as a database
  `makeblastdb -in [FASTAFILE] -dbtype [nucl or prot] -parse_seqids`
      - `-in` is the switch for the FASTA formated sequence file that you want to use as your BLAST db
      - `-dbtype` needs to be `prot` or `nucl`. This has to correspond to the sequence type in your FASTA file
      - `parse_seqids` makes it possible for you to retrieve individual sequences by name using `blastdbcmd`
2. Run `blastp -help` for information about running the command and formatting output.
3. Run `blastp -query [Your Query FASTA File] -db [BLAST FORMATED DB FASTA FILE] -out [output file name] -evalue [evalue cutoff] -outfmt [5 for XML; 6 for TAB; etc]`
      - `-query`  A FASTA formated sequence file with one or more query sequences
      - `-db` The file name of the FASTA formated file you formated with `makeblastdb`
      - `-out` A name of your choice for your output file, otherwise, the output is printed to the screen
      - `-evalue` The Expectation value (E) threshold for returning hits. 1e-5 is a common cutoff (Bill will say 1e-2, but we will be a tad more conservative)
      - `-outfmt` Choose the output format of your BLAST report as XML(5) `-outfmt 5` .  TAB(6) is also common output but unparsable by BioPython.  
      
__Parse BLAST Output__

1. Use BioPython to parse your XML BLAST results. Print out all the hit sequence ID that are better than 1e-5 as well as their descriptions in tab separated columns.
  

