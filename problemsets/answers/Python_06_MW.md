Python 6 - IO - Problem Set
===================

1. Write a script to do the following to [Python_06.txt](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_06.txt)
   - Open and read the contents.  
   - Uppercase each line
   - Print each line to the STDOUT

```python
#!/usr/bin/env python3

file = open('Python_06.txt')

for line in file:
  line = line.upper()
  print(line)

file.close()
```

2. Modifiy the script in the previous problem to write the contents to a new file called "Python_06_uc.txt"

```python

#!/usr/bin/env python3

file = open('Python_06.txt','r')
wFile= open('Python_06_uc.txt','w')

for line in file:
  line = line.upper()
  wFile.write(line)

file.close()
wFile.close()

```



3. Open and print the reverse complement of each sequence in [Python_06.seq.txt](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_06.seq.txt). Each line is the following format:    `seqName\tsequence\n.` Make sure to print the output in fasta format including the sequence name and a note in the description that this is the reverse complement. Print to STDOUT and capture the output into a file with a command line redirect '>'. 
   - **Remember is is always a good idea to start with a test set for which you know the correct output.**

```python
#!/usr/bin/env python3

file = open('Python_06.seq.txt','r')

geneSet = {}				## initializes an empty dictionary to populate from the file

for line in file:			## iterates through the file object
  line = line.rstrip()			## cleans the line
  id,seq = line.split()			## splits the line into id and sequence
  geneSet[id] = seq			## saves the info to a dictionary

geneSetRC = {}				## initializes an empty dictionary for reverse complement of sequence

for gene in geneSet:			## iterate through dictionary using a for loop
  dna = geneSet[gene]			## reads the sequence from the previously generated dictionary
  tDNA = dna.replace('T','a')		## substitute the nt's out
  aDNA = tDNA.replace('A','t')
  cDNA = aDNA.replace('C','g')
  gDNA = cDNA.replace('G','c')

  compDNA = gDNA.upper()		## capitalize and reverse the sequence
  rCdna = compDNA[::-1]
  
  geneSetRC[gene] = rCdna		## saves the reverse complement into a new dict using the same gene ID as the dictionary that we are iterating through

for gene in geneSetRC:
  print('>'+ gene , geneSetRC[gene] , sep = '\n') ## prints in fasta format


file.close()

```

4. Open the [FASTQ](https://en.wikipedia.org/wiki/FASTQ_format) file [Python_06.fastq](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_06.fastq) and go through each line of the file. Count the number of lines and the number of characters per line. Have your program report the:  
    - total number of lines  
    - total number of characters  
    - average line length   

```python
#!/usr/bin/env python3

file = open('Python_06.fastq.txt','r')
lineCount = 0					## initialize the line counter
charCount = 0					## initialize the character counter

for line in file:				## iterate through file object using for loop
   lineCount += 1				## increment line count by 1
   charCount += len(line.rstrip())		## increment character count by length

print('lines:',lineCount)			## print total num of lines
print('chars:',charCount)			## print total num of characters
print('ave line len:',charCount/lineCount)	## print the average length of line

file.close()
```

5. Write your first FASTA parser. This is a script that reads in a FASTA file and stores each FASTA record separately for easy access for future analysis.

Things to keep in mind:
   - open your file
   - read each line
   - is your line a header line? is it a sequence line?
   - does a single FASTA record have one line of sequence or multiple lines of sequence?
   
   HINTS: use file I/O, if statements and dictionaries to write your first FASTA parser. Some other useful functions and methods are find, split, string concatenation.
   
   At the end, your script should return the following:
   
   fastaDict = {
      'seq1' : 'AAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGCCACCAATTATGGTGTATGAGTGAATCTCTGGTCCGAGATTCACTGAGTAACTGCTGTACACAGTAGTAACACGTGGAGATCCCATAAGCTTCACGTGTGGTCCAATAAAACACTCCGTTGGTCAAC' ,
      'seq2' : 'GCCACAGAGCCTAGGACCCCAACCTAACCTAACCTAACCTAACCTACAGTTTGATCTTAACCATGAGGCTGAGAAGCGATGTCCTGACCGGCCTGTCCTAACCGCCCTGACCTAACCGGCTTGACCTAACCGCCCTGACCTAACCAGGCTAACCTAACCAAACCGTGAAAAAAGGAATCT' ,
      'seq3' : 'ATGAAAGTTACATAAAGACTATTCGATGCATAAATAGTTCAGTTTTGAAAACTTACATTTTGTTAAAGTCAGGTACTTGTGTATAATATCAACTAAAT' ,
      'seq4' : 'ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAAACAACATGCCAAATAGAAACGATCAATTCGGCGATGGAAATCAGAACAACGATCAGTTTGGAAATCAAAATAGAAATAACGGGAACGATCAGTTTAATAACATGATGCAGAATAAAGGGAATAATCAATTTAATCCAGGTAATCAGAACAGAGGT' }

```python

#!/usr/bin/env python3

import sys

fasta_filename = sys.argv[1]			## read in file name from command line

fasta_fileobj = open(fasta_filename, 'r')	## create a file obj from the specified file

sequence_name = ''				## initialize strings to populate from file object info
sequence_desc = ''
sequence_string = ''
sequnce_dict = {}

for line in fasta_fileobj:  			## iterate through file object with for loop
    line = line.rstrip()			## strip white space on the right side (like a new line character!) 

    if line.startswith('>'):
	line = line.lstrip('>')  		## remove leading `>` char
	sequence_info = line.split(maxsplit=1)  	## split on only first space


	if len(sequence_info) > 1:
		sequence_desc = sequence_info[1]

	else:					## sequence has no description, set to empty
		sequence_desc = ''
	
	if len(sequence_string) > 0:
		sequence_dict[sequence_name] = sequence_string	
		sequence_string = ''  		## reset for the new sequence
		
           
	sequence_name = sequence_info[0]
        
	if len(sequence_info) > 1:
            sequence_desc = sequence_info[1]
        else:
            # sequence has no description, set to empty
            sequence_desc = ''
             
    else:
        sequence_string += line  # incrementally elongate seq

# When we reach the end of the FASTA file, we drop out of the
# 'for' loop. However, we still have the last sequence record
# stored in memory, which we haven't processed yet, because we
# haven't observed a '>' symbol, so we must copy and paste any
# code that we used to process sequences above to the code block
# below. Check if sequence_string has a non-zero length to
# determine whether to execute the sequence processing code:

if len(sequence_string) > 0:
	sequence_dict[sequence_name] = sequence_string

```

6. You are going to generate a couple of gene list that are saved in files, add their contents to sets, and compare them. 

__Generate Gene Lists:__


_Get all genes:_

1. Go to [Ensembl Biomart](http://useast.ensembl.org/biomart/martview/4b8fb1941e75e7763e8c4ccf1ffcd9c5).
2. In dropdown box, select "Ensembl Genes 98"  (or most current version)
3. In dropdown box, select "Alpaca Genes" 
4. On the left, click Attributes
5. Expand GENE:
6. Deselect "transcript stable ID".
7. Click Results (top left)
8. Export all results to "File" "TSV" --> GO
9. Rename the file to "alpaca_all_genes.tsv"

_In the same Ensembl window, follow the steps below to get genes that have been labeled with Gene Ontology term "stem cell proliferation". For extra information on stem cell proliferation, check out  [stem cell proliferation](http://purl.obolibrary.org/obo/GO_0072089)_

10. Click "Filters"
11. Under "Gene Ontology", check "Go term name" and enter "stem cell proliferation"
12. Click Results (top left)
13. Export all results to "File" "TSV" --> GO
14. Rename the file to "alpaca_stemcellproliferation_genes.tsv"

_In the same Ensembl window, follow the steps below to get genes that have been labeled with Gene Ontology term "stem cell proliferation". For extra information on pigmentation, check out [pigmentation](http://purl.obolibrary.org/obo/GO_0043473)_


15. Click "Filters"
16. Under "Gene Ontology", check "Go term name" and enter "pigmentation"
17. Click Results (top left)
18. Export all results to "File" "TSV" --> GO
19. Rename the file to "alpaca_pigmentation_genes.tsv"


__Open each of the three files and add the geneIDs to a Set. One Set per file.__

A. Find all the genes that are not cell proliferation genes.  
B. Find all genes that are both stem cell proliferation genes and pigment genes.  
*Note* Make sure to NOT add the header to your set.  

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


__Now do the same on the command line with `comm` command. You might need to `sort` each file first.__


```python
  
#!/usr/bin/env python3

with open('alpaca_all_genes.tsv','r') as file:			## open file object in with block
  lineCount = 0							## line counter (to dodge the header file)
  allGenes=set()						## initializes an empty set

  for line in file:						## iterate through file object and recoreds all but the first line into the set
    if lineCount == 0:
      lineCount += 1
      continue
    allGenes.add(line)
    lineCount += 1

with open('alpaca_pigmentation_genes.tsv','r') as file:
  lineCount = 0
  pigGenes=set()

  for line in file:
    if lineCount == 0:
      lineCount += 1
      continue
    pigGenes.add(line)
    lineCount += 1

with open('alpaca_stemcellproliferation_genes.tsv','r') as file:
  lineCount = 0
  proGenes=set()

  for line in file:
    if lineCount == 0:
      lineCount += 1
      continue
    proGenes.add(line)
    lineCount += 1

with open('alpaca_transcriptionFactors.tsv','r') as file:
  lineCount = 0
  tfGenes=set()

  for line in file:
    if lineCount == 0:
      lineCount += 1
      continue
    tfGenes.add(line)
    lineCount += 1    

print(len(allGenes))						## prints lengths
print(len(proGenes))
print(len(pigGenes))
print(len(tfGenes))

notInscp = allGenes - proGenes					## use set algebra to report exclusive genes
print(len(notInscp))

proNpig = proGenes & pigGenes					## find and report the union
print(len(proNpig))

proTF = proGenes & tfGenes					## find and report the union
print(len(proTF))

```

## Extra: Expand on an exercise from ProblemSet 5 on nucleotide composition
  - get the raw file [Python_06.seq.txt](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_06.seq.txt)
  - in a script, open this file
  - iterate over each line in this file (seqName\tsequence\n)
     - for each sequence:
         - calculate and store the count of each unique nucleotide character in a dictionary
         - report the name, total of each nucleotide count, and the GC content
```python 
#!/usr/bin/env python3

seq_dict = {}						## initializes the sequence dictionary to populate from the file

with open('Python_06.seq.txt', 'r') as file_obj:	## opens the file as a file obj

	for line in file_obj:				## iterates through the file obj
		line = line.rstrip()			## strip the new line character
		ID , seq = line.split()			## splits the line into an ID and a sequence
		
		nt_count = {}				## resets the nt dict
		nt_tot = 0				## resets the total nt count

		for nt in set(seq):			## iterates through all the unique nt in each sequence
			nt_count[nt] = seq.count(nt)	## adds nt count to a dict
			nt_tot += seq.count(nt)		## keeps track of the total number of nt
			gc_cont = ( nt_count['G'] + nt_count['C'] ) / nt_tot	## calcs GC cont
			
		seq_dict[ID] = { 'ID' : ID , 'seq' : seq , 'nt_counts' : nt_count ,'nt_tot'  : nt_tot ,'gc_cont' :gc_cont }	## creates a dictionary of dictionaries

	for ID in seq_dict:				## iterates through the sequence dictionary
		to_print = ''				## (re)initialize a sequence to print

		for item in ['ID', 'nt_tot', 'gc_cont']:## iterates through the information to print
			to_print += item + ': ' + str(seq_dict[ID][item]) + '\t'		## fills the to_print string with the desired infor from the dict dict

		print(to_print)				## prints the desired info
```
