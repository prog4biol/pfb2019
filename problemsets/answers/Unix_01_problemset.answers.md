# Answers Problemset 1

What is the full path to your home directory?
```sh
$ pwd
```
Go up one directory?
```sh
$ cd ..
```
How many files does it contain?
```sh
$ ls | wc -l
```
How many directories?
```sh
$ ls -d */ | wc -l
```
Make a directory called problemsets in your home directory.
```sh
$ cd
$ mkdir problemsets
```
Navigate into this new directory called problemsets. Verify that you are in the correct directory by using pwd.
```sh
$ cd problemsets
$ pwd
```
Use wget to copy https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/sequences.nt.fa from the web into your problemsets directory. If wget is not available on your system, use curl -O as an alternative.
```sh
$ wget  https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/sequences.nt.fa
```
Without using a text editor calculate or report these qualities for the file sequences.nt.fa. This file can be found here https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/sequences.nt.fa
How many lines does this file contain?
```sh
$ wc -l sequences.nt.fa
```
How many characters? (Hint: check out the options of wc)
```sh
$ wc -m sequences.nt.fa
```
What is the first line of this file? (Hint: read the man page of head)
```sh
$ head -1 sequences.nt.fa
```
What are the last 3 lines? (Hint: read the man page of tail)
```sh
$ tail -3 sequences.nt.fa
```
How many sequences are in the file? (Hint: use grep) (Note: The start of a sequence is indicated by a > character.)
```sh
$ grep ">" sequences.nt.fa
```
Rename sequences.nt.fa to cancer_genes.fasta. (Hint: read the man page for mv)
```sh
$ mv sequences.nt.fa cancer_genes.fasta
```
9. Copy this remote file: to your problemset directory.
Use wget to copy https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/cuffdiff.txt from the web into your problemsets directory. If wget is not available on your system, use curl -O as an alternative.
```sh
$ wget https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/cuffdiff.txt
```
Do the following to cuffdiff.txt. The descriptions of each column in the file are in the table below.
Look at the first few lines of the file
```sh
$ head cuffdiff.txt
```
Sort the file by log fold change 'log2(fold_change)', from highest to lowest, and save in a new file in your directory called sorted.cuffdiff.out
```sh
$ sort -k10gr cuffdiff.txt > sorted.cuffdiff.out
```
Sort the file (log fold change highest to lowest) then print out only the first 100 lines.
Save in a file called top100.sorted.cuffdiff.out.
```sh
$ sort -k10gr cuffdiff.txt | head -100 > top100.sorted.cuffdiff.out
```
Sort the file by log fold change, print out the top 100, print only first column. This will be a list of the genes with the largest change in expression. Make sure your list is sorted by gene name and is unique. Save this curated list in a file called differentially.expressed.genes.txt.
```sh
$ sort -k10gr cuffdiff.txt | head -100 | cut -f1 |sort | uniq > differentially.expressed.genes.txt
$ wc -l differentially.expressed.genes.txt
```
