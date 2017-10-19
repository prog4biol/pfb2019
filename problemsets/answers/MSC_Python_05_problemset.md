Python 5 Problem Set
===================

1. **Write a script to do the following to [Python_05.txt](https://github.com/srobb1/pfb2017/blob/master/files/Python_05.txt)**
   - Open and read the contents.  
   - Uppercase each line
   - Print each line to the STDOUT

```python
#!/usr/bin/env python3

file_object = open("Python_05.fasta","r")
for line in file_object:
  line = line.rstrip("\n")
  print(line.upper())
```

2. **Modifiy the script in the previous problem to write the contents to a new file called "Python_05_uc.txt"**

```python
#!/usr/bin/env python3

file_object = open("Python_05.fasta","r")
fo = open("Python_05_uc.txt" , "w")
for line in file_object:
  line = line.rstrip("\n")
  fo.write(line.upper() + "\n")
fo.close()
```

3. **Open and print the reverse complement of each sequence in [Python_05.fasta](https://raw.githubusercontent.com/srobb1/pfb2017/master/files/Python_05.fasta). Make sure to print the output in fasta format including the sequence name and a note in the description that this is the reverse complement. Print to STDOUT and capture the output into a file with a command line redirect '>'.**

```python
#!/usr/bin/env python3

fi = open("Python_05.fasta","r")
fo = open("Python_05_rc.txt" , "w")
seqs={}
def_line = ""

for line in fi:
  line = line.rstrip("\n")
  if line.startswith('>'):
    def_line = line
    
  else:
    if def_line in seqs:
      seqs[def_line] += line 
    else:
      seqs[def_line] = line

for id in seqs:
    #compliment the sequence
  complement = seqs[id].replace('A','t')
  complement = complement.replace('T','a')
  complement = complement.replace('G','c')
  complement = complement.replace('C','g')
    #upper case it
  complement = complement.upper()
    #reverse it
  rev_comp = complement[::-1]
  fo.write(id + "rev_comp\n" + rev_comp + "\n")

fo.close()
fi.close()

```
4. Open the [FASTQ](https://en.wikipedia.org/wiki/FASTQ_format) file [Python_05.fastq](https://raw.githubusercontent.com/srobb1/pfb2017/master/files/Python_05.fastq) and go through each line of the file. Count the number of lines and the number of characters per line. Have your program report the:  
    - total number of lines  
    - total number of characters  
    - average line length   

```python
#!/usr/bin/env python3

fi = open("Python_05.fasta","r")

total_lines = 0
total_chars = 0

for line in fi:
  line = line.rstrip("\n")
  total_lines += 1
  total_chars += len(line)

fi.close()

ave_line_len = total_chars/total_lines

print("total lines: ", total_lines)
print("total chars: ", total_chars)
print("average line len: ", ave_line_len)
```

output
```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./file_io_3.py
total lines:  8
total chars:  687
average line len:  85.875
```

5. You are going to generate a couple of gene list that are saved in files, add their contents to sets, and compare them. 

__Generate Gene Lists:__


_Get all genes:_

1. Go to Ensembl Biomart.
2. In dropdown box, select "Ensembl Genes 90"
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
19. Rename the file to "alpaca_stemcellpigmentation_genes.tsv"


__Open each of the three files and add the geneIDs to a Set. One Set per file.__

A. Find all the genes that are not cell proliferation genes.  
B. Find all genes that are both stem cell proliferation genes and pigment genes.  
*Note* Make sure to NOT add the header to your set.  

```python
#!/usr/bin/env python3

f_all = open("alpaca_all_genes.tsv","r")
f_pro = open("alpaca_stemcellproliferation_genes.tsv","r")
f_pig = open("alpaca_stemcellpigmentation_genes.tsv","r")

s_all = set() 
s_pro = set()
s_pig = set()

for line in f_all:
  line = line.rstrip("\n")
  if line.startswith("Gene"):
    continue
  else:
    s_all.add(line)
    
for line in f_pro:
  line = line.rstrip("\n")
  if line.startswith("Gene"):
    continue
  else:
    s_pro.add(line)
    
for line in f_pig:
  line = line.rstrip("\n")
  if line.startswith("Gene"):
    continue
  else:
    s_pig.add(line)
    
all_but_pro = s_all - s_pro
in_both = s_pro & s_pig

for genes_in_both in in_both:
  print(genes_in_both)
  

f_all.close()
f_pig.close()
f_pro.close()
```

run it
```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./file_io_4.py
ENSVPAG00000006812
ENSVPAG00000000048
ENSVPAG00000006160
ENSVPAG00000003148
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
#!/usr/bin/env python3

f_all = open("alpaca_all_genes.tsv","r")
f_pro = open("alpaca_stemcellproliferation_genes.tsv","r")
f_pig = open("alpaca_stemcellpigmentation_genes.tsv","r")
f_tsf = open("alpaca_transcriptionFactors.tsv","r")

s_all = set() 
s_pro = set()
s_pig = set()
s_tsf = set()

for line in f_all:
  line = line.rstrip("\n")
  if line.startswith("Gene"):
    continue
  else:
    s_all.add(line)
    
for line in f_pro:
  line = line.rstrip("\n")
  if line.startswith("Gene"):
    continue
  else:
    s_pro.add(line)
    
for line in f_pig:
  line = line.rstrip("\n")
  if line.startswith("Gene"):
    continue
  else:
    s_pig.add(line)

for line in f_tsf:
  line = line.rstrip("\n")
  if line.startswith("Gene"):
    continue
  else:
    s_tsf.add(line)
    
all_but_pro = s_all - s_pro
in_both = s_pro & s_pig
pro_tsf = s_pro & s_tsf

for genes_in_both in pro_tsf:
  print(genes_in_both)
  

f_all.close()
f_pig.close()
f_pro.close()
f_tsv.close()
```

run it
```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./file_io_4.py
ENSVPAG00000004735
ENSVPAG00000002791
ENSVPAG00000005064
ENSVPAG00000009548
ENSVPAG00000000807
ENSVPAG00000003303
ENSVPAG00000007751
ENSVPAG00000003467
ENSVPAG00000002018
ENSVPAG00000012555
ENSVPAG00000011930
ENSVPAG00000004389
ENSVPAG00000000048
ENSVPAG00000002395
ENSVPAG00000005950
```
__Now do the same on the command line with `comm` command. You might need to `sort` each file first.__

start by getting rid of the headers and sorting the files 
```sh
mcampbel@jabberwocky.cshl.edu:answers$ grep -v 'Gene' alpaca_transcriptionFactors.tsv | sort > sorted_atf.txt
mcampbel@jabberwocky.cshl.edu:answers$ grep -v 'Gene' alpaca_ | sort > sorted_apr.txt
mcampbel@jabberwocky.cshl.edu:answers$ grep -v 'Gene' alpaca_stemcellproliferation_genes.tsv | sort > sorted_apr.txt
```

now we can run comm. by default comm prints three colums. The thrid colum is the one that contains the ids that are common to both files. The -1 and -2 flags supress the printing of colums 1 and 2, so only the colum of matches are printed.
```sh
mcampbel@jabberwocky.cshl.edu:answers$ comm -1 -2 sorted_apr.txt sorted_atf.txt 
ENSVPAG00000000048
ENSVPAG00000000807
ENSVPAG00000002018
ENSVPAG00000002395
ENSVPAG00000002791
ENSVPAG00000003303
ENSVPAG00000003467
ENSVPAG00000004389
ENSVPAG00000004735
ENSVPAG00000005064
ENSVPAG00000005950
ENSVPAG00000007751
ENSVPAG00000009548
ENSVPAG00000011930
ENSVPAG00000012555
```

if we run our python script again and sort the output it is easier to see that the lists are the same.

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./file_io_4.py | sort
ENSVPAG00000000048
ENSVPAG00000000807
ENSVPAG00000002018
ENSVPAG00000002395
ENSVPAG00000002791
ENSVPAG00000003303
ENSVPAG00000003467
ENSVPAG00000004389
ENSVPAG00000004735
ENSVPAG00000005064
ENSVPAG00000005950
ENSVPAG00000007751
ENSVPAG00000009548
ENSVPAG00000011930
ENSVPAG00000012555
```