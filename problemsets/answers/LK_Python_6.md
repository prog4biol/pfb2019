Python 6 - IO - Problem Set
===================

1. Write a script to do the following to [Python_06.txt](https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/Python_06.txt)
   - Open and read the contents.  
   - Uppercase each line
   - Print each line to the STDOUT

```python
with open('Python_06.txt', 'r') as song:
  for line in song:
    print(line.upper(), end='')
```
2. Modifiy the script in the previous problem to write the contents to a new file called "Python_06_uc.txt"

```python
song_uppercase=open('Python_06_uc.txt', 'w')
with open('Python_06.txt', 'r') as song:
  for line in song:
    print(line.upper(), end='', file=song_uppercase)
song_uppercase.close()
```
3. Open and print the reverse complement of each sequence in [Python_06.seq.txt](https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/Python_06.seq.txt). Each line is the following format:    `seqName\tsequence\n.` Make sure to print the output in fasta format including the sequence name and a note in the description that this is the reverse complement. Print to STDOUT and capture the output into a file with a command line redirect '>'.
   - **Remember is is always a good idea to start with a test set for which you know the correct output.**
```python
with open('Python_06.seq.txt', 'r') as sf:
  for line in sf:
    identifier, sequence = line.rstrip().split("\t")
    sequence_RC = sequence.replace('A', 't')
    sequence_RC = sequence.replace('T', 'a')
    sequence_RC = sequence.replace('C', 'g')
    sequence_RC = sequence.replace('G', 'c')
    sequence_RC=sequence_RC.upper()[::-1]
    print(">{}_reverse_complement\n{}".format(identifier,sequence))

```
4. Open the [FASTQ](https://en.wikipedia.org/wiki/FASTQ_format) file [Python_06.fastq](https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/Python_06.fastq) and go through each line of the file. Count the number of lines and the number of characters per line. Have your program report the:  
    - total number of lines  
    - total number of characters  
    - average line length   

```python
n_lines=0
n_chars=0

with open('Python_06.fastq', 'r') as fq:
  for line in fq:
    line=line.rstrip()
    n_lines+=1
    n_chars+=len(line)
print("There are {} lines and {} characters in the file.\nThe average line length is {}".format(n_lines, n_chars, n_chars/n_lines))

```

5. You are going to generate a couple of gene list that are saved in files, add their contents to sets, and compare them.

__Generate Gene Lists:__


_Get all genes:_

1. Go to [Ensembl Biomart](http://useast.ensembl.org/biomart/martview/4b8fb1941e75e7763e8c4ccf1ffcd9c5).
2. In dropdown box, select "Ensembl Genes 94"
3. In dropdown box, select "Alpaca Genes"
4. On the left, click Attributes
5. Expand GENE:
6. Deselect "transcript stable ID".
7. Click Results (top left)
8. Export all results to "File" "TSV" --> GO
9. Rename the file to "alpaca_all_genes.tsv"

_Get genes that have been labeled with Gene Ontology term [stem cell proliferation](http://purl.obolibrary.org/obo/GO_0072089)_

10. Click "Filters"
11. Under "Gene Ontology", check "Go term name" and enter "stem cell proliferation"
12. Click Results (top left)
13. Export all results to "File" "TSV" --> GO
14. Rename the file to "alpaca_stemcellproliferation_genes.tsv"

_Get genes that have been labeled with Gene Ontology term [pigmentation](http://purl.obolibrary.org/obo/GO_0043473)_


15. Click "Filters"
16. Under "Gene Ontology", check "Go term name" and enter "pigmentation"
17. Click Results (top left)
18. Export all results to "File" "TSV" --> GO
19. Rename the file to "alpaca_pigmentation_genes.tsv"


__Open each of the three files and add the geneIDs to a Set. One Set per file.__

A. Find all the genes that are not cell proliferation genes.  
B. Find all genes that are both stem cell proliferation genes and pigment genes.  
*Note* Make sure to NOT add the header to your set.  

```python
all_genes=set()
pigmentation_genes=set()
stemcell_proliferation=set()

#read in all genes
with open("alpaca_all_genes.tsv") as ag:
  firstline=True
  for line in ag:
    if firstline:
      firstline=False
      continue
    line=line.rstrip()
    all_genes.add(line)

#read in pigmentation genes
with open("alpaca_pigmentation_genes.tsv") as pg:
  firstline=True
  for line in pg:
    if firstline:
      firstline=False
      continue
    line=line.rstrip()
    pigmentation_genes.add(line)

#read in sc proliferation genes
with open("alpaca_stemcellproliferation_genes.tsv") as sg:
  firstline=True
  for line in sg:
    if firstline:
      firstline=False
      continue
    line=line.rstrip()
    stemcell_proliferation.add(line)

genes_not_cell_pro = all_genes-stemcell_proliferation
print("Non Stem-Cell Proliferation Genes:\n{}".format(genes_not_cell_pro))
scell_pigment=stemcell_proliferation & pigmentation_genes
print("Stemcell Proliferation & Pigmentation:\n{}".format(scell_pigment))

```



__Now, let do it again with transciption factors.__

1. Go back to your Ensembl Biomart window
2. Deselect the "GO Term Name"
3. Select "GO Term Accession"
4. Enter these two accessions IDs which in most organisms will be all the transcription factors
   - GO:0006355 is "regulation of transcription, DNA-dependent”.
   - GO:0003677 is "DNA binding"
5.  Click Results (top left)
6. Export all results to "File" "TSV" --> GO
7. Rename the file to "alpaca_transcriptionFactors.tsv"

__Open these two files: 1) the transcription factor gene list file and 2) the cell proliferation gene list file. Add each to a Set, One Set per file__

A. Find all the genes that are transcription factors for cell proliferation

```python
all_genes=set()
pigmentation_genes=set()
stemcell_proliferation=set()
transcription_factors=set()

with open("alpaca_stemcellproliferation_genes.tsv") as sg:
  firstline=True
  for line in sg:
    if firstline:
      firstline=False
      continue
    line=line.rstrip()
    stemcell_proliferation.add(line)

with open("alpaca_transcriptionFactors_genes.tsv") as tf:
  firstline=True
  for line in tf:
    if firstline:
      firstline=False
      continue
    line=line.rstrip()
    transcription_factors.add(line)

tf_for_cp=stemcell_proliferation & transcription_factors

print('Transcription Factors for Stemcell Proliferation:\n{}'.format(tf_for_cp))
```


## Extra: Expand on last problemset exercise on nucleotide composition
  - get the raw file [Python_06.seq.txt](https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/Python_06.seq.txt)
  - in a script, open this file
  - iterate over each line in this file (seqName\tsequence\n)
     - for each sequence:
         - calculate and store the count of each unique nucleotide character in a dictionary
         - report the name, total of each nucleotide count, and the GC content
```python

with open("Python_06.seq.txt") as s:
  for line in s:
    #create an empty dict. where we will store out nucleotide counts of each sequence
    nt_counts={}
    line=line.rstrip()
    name, sequence=line.split()
    #get the unique nucleotides in the sequences by converting it into a set
    uniq_nts=set(sequence)
    #count the number of occurences of the nt in the sequences:
    for nt in uniq_nts:
      nt_count=sequence.count(nt)
      nt_counts[nt]=nt_count
    #report count of nt, and gc contents
    seq_length=len(sequence)
    gc_cont=(nt_counts['G']+nt_counts['C'])/seq_length
    nt_comp=[(k,v) for k,v in nt_counts.items()]
    print("Name: {}\tGC:\t{}\tNT-Composition:{}".format(name, gc_cont, nt_comp))


```  
