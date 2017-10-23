# Biopython problem set

### Preparation for problems

Preparation:

1.  Download uniprot_sprot using the Unix command 'wget':

```
wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
```

2. Unzip the file using the Unix command 'gunzip':

```
gunzip uniprot_sprot.fasta.gz
```
This will create a file `uniprot_sprot.fasta`

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
  

