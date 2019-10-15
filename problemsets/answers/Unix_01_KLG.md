# Unix Basics Quick Review and Problem Set

useful commands
=========================

| command         | description                              |
| --------------- | ---------------------------------------- |
| `ls`            | list directory contents                  |
| `cd`            | change directory                         |
| `mkdir`         | make a directory                         |
| `rm`            | remove, or delete files and directories. Use caution, it is easy to delete more that you want. |
| `head`          | prints the top few lines to the terminal window |
| `tail`          | prints the last few lines to the terminal window |
| `sort`          | sorts the lines                          |
| `uniq`          | prints the unique lines                  |
| `grep`          | filnds the lines that contain a pattern  |
| `wc`            | counts the number of lines, characters and words |
| `mv`            | move files                               |
| `cp`            | copy files                               |
| `date`          | returns the current date and time        |
| `pwd`           | return working directory name            |
| `ssh`           | remote login                             |
| `scp`           | remote secure copy                       |
| `~`             | shortcut for your home directory         |
| `man <command>` | manual page for the command e.g. `man ls` to get the man page for `ls` |





### Try these examples

**The files you need later in this review are in our [github repository](https://github.com/prog4biol/pfb2019). There will be direction on how to retrieve them**

Let's go to a directory with a lot of files in it and list those files

```bash
cd /bin/
ls
```

__What's the difference between these two commands?__

```bash
bash-3.2$ cd /bin/
bash-3.2$ ls
[		dd		ksh		pax		stty
bash		df		launchctl	ps		sync
cat		echo		link		pwd		tcsh
chmod		ed		ln		rm		test
cp		expr		ls		rmdir		unlink
csh		hostname	mkdir		sh		wait4path
date		kill		mv		sleep		zsh
bash-3.2$ 
```
One command __changes directory_ into /bin/, the other command __lists__ what is in the directory.

Try them both!!
```
ls -l
ls -lt
```

The -l option gives information about each file, the -t options will sort the files by time modified. 

__Pipes__ 

You can string more than one command together with a pipe `|` , such that the standard output of the first command is 'piped' into the standard input of the second command.

Try it!!
```
ls -lt | head
```

```bash
kirstens-mbp-4:~ Kirsten$ ls -lt | head
total 71020856
drwxr-xr-x  19 Kirsten  staff          608 Oct 15 09:12 pfb2018
drwxr-xr-x  18 Kirsten  staff          576 Oct 15 09:11 pfb2019
drwxr-xr-x   6 Kirsten  staff          192 Oct 14 14:53 Analysis
drwx------+ 44 Kirsten  staff         1408 Oct 13 21:56 Downloads
drwx------@ 23 Kirsten  staff          736 Oct 11 21:05 OneDrive - UW-Madison
drwxr-xr-x@ 19 Kirsten  staff          608 Oct  9 23:28 KirstenGoogleDrive
drwxr-xr-x  17 Kirsten  staff          544 Oct  6 20:23 miniconda3
drwxr-xr-x  40 Kirsten  staff         1280 Oct  6 20:23 scripts
drwx------@  6 Kirsten  staff          192 Oct  6 19:41 Desktop
```


__Semicolons__

You can string more than one command together by putting a semi-colon `;` after the each command. Here, the commands will be run sequentially, but any output does not get passed from one command to the next.

Try it!!
```
date ; sleep 2 ; date
```

```bash

kirstens-mbp-4:~ Kirsten$ date ; sleep 2 ; date
Tue Oct 15 09:35:28 EDT 2019
Tue Oct 15 09:35:30 EDT 2019

```

> If you want to know more about `sleep` type `man sleep`


__Download a file__
You can use `wget` or `curl` to download files. On some systems only one of these may be available
```
curl -O https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/cuffdiff.txt
```

__Redirect STDOUT__  
You can redirect the output of a command into a file. 
```
cd ~
grep Chr7 cuffdiff.txt > fav_chr_cuffdiff.txt
```



__Append STDOUT to the end of a file that already exists__

You can append the output of a command to a file

```
grep Chr9 cuffdiff.txt >> fav_chr_cuffdiff.txt
```



__Redirect STDERR__  

You can redirect STDERR to a file.

Let's review what STDERR actually is.
```
cat blablabla.txt
```
> file blablabla.txt does not exist so we get `cat: blablabla.txt: No such file or directory` printed to the terminal. This message is labeled by the operating system as an error message or STDERR. 

STDERR is a labeled type of output we can redirect

```
cat blablabla.txt 2> errors.txt
```
> We can redirect the error messages, A.K.A. STDERR, to a new file called anything we want


What happens when you try to redirect STDOUT?
```
cat blablabla.txt > errors.txt
```
> `cat: blablabla.txt: No such file or directory` still gets printed to the screen because we only redirect STDOUT to our file. There is no STDOUT in this case and our file will be empty. How would you verify this?


```bash
## look at the top of the file
head errors.txt
```

__Redirect STDOUT and STDERR__

You can redirect both STDOUT and STDERR to **two separate** files in one command.

```
# just print it to the terminal first
cat fav_chr_cuffdiff.txt blablabla.file

# redirect to two files, STDOUT to out.txt, STDERR to err.txt 
cat fav_chr_cuffdiff.txt blablabla.file 1> out.txt 2> err.txt

# this does the same, do you see the difference?
cat fav_chr_cuffdiff.txt blablabla.file > out.txt 2> err.txt

```
> Examine the contents of `out.txt` and `err.txt`

You can also redirect both STDOUT and STDERR to **the same** file.
```
cat fav_chr_cuffdiff.txt blablabla.file &> all_out_err.txt 
```


Problem Set
===========

1. Log into your machine. 

2. What is the full path to your home directory?

```bash
kirstens-mbp-4:~ Kirsten$ pwd
/Users/Kirsten
```

3. Go up one directory?
    - How many files does it contain?

```bash
kirstens-mbp-4:~ Kirsten$ ls | wc -l
      39
```

    - How many directories?

```bash

kirstens-mbp-4:~ Kirsten$ ls -F | grep "/" | wc -l
      34
 ```


4. Make a directory called `problemsets` in your home directory.

```bash

mkdir problemsets

```

5. Navigate into this new directory called problemsets. Verify that you are in the correct directory by using `pwd`.

```bash
bash-3.2$ pwd
/Users/Kirsten/problemsets
```

6. Use `wget` to copy <https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/sequences.nt.fa> from the web into your problemsets directory. If `wget` is not available on your system, use `curl -O` as an alternative.

```bash
wget https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/sequences.nt.fa
```

7. Without using a text editor calculate or report these qualities for the file `sequences.nt.fa`.
  This file can be found here <https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/sequences.nt.fa>
      - How many lines does this file contain?   
      - How many characters?    (Hint: check out the options of wc)
      - What is the first line of this file?    (Hint: read the man page of head)
      - What are the last 3 lines?    (Hint: read the man page of tail)
      - How many sequences are in the file?    (Hint: use grep) (Note: The start of a sequence is indicated by a `>` character.)    

```bash
# - How many lines does this file contain?
bash-3.2$ wc -l sequences.nt.fa 
     148 sequences.nt.fa


# - How many characters?    (Hint: check out the options of wc)
bash-3.2$ wc -c sequences.nt.fa 
   10267 sequences.nt.fa

# - What is the first line of this file?    (Hint: read the man page of head)
bash-3.2$ head -n 1 sequences.nt.fa 
>NM_001126114.2 Homo sapiens tumor protein p53 (TP53), transcript variant 3, mRNA

# - What are the last 3 lines?    (Hint: read the man page of tail)

bash-3.2$ tail -n 3 sequences.nt.fa 
TTTATAGCTGTTGGAAGGACTAGGTCTTCCCTAGCCCCCCCAGTGTGCAAGGGCAGTGAAGACTTGATTG
TACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAA
AAAAAAAAAAAAAA

# - How many sequences are in the file?    (Hint: use grep) (Note: The start of a sequence is indicated by a `>` character.)

bash-3.2$ grep ">" sequences.nt.fa  | wc -l
       2

```


8. Rename `sequences.nt.fa` to `cancer_genes.fasta`. (Hint: read the man page for mv)

```bash
bash-3.2$ mv sequences.nt.fa cancer_genes.fasta
```

<div id="get-cuffdiff"></a> 9. Copy this remote file: <https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/cuffdiff.txt> to your problemset directory. 

Use `wget` to copy <https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/cuffdiff.txt> from the web into your problemsets directory. If `wget` is not available on your system, use `curl -O` as an alternative.




10. Do the following to `cuffdiff.txt`. The descriptions of each column in the file are in the table below.
    - Look at the first few lines of the file
    - Sort the file by log fold change 'log2(fold_change)', from highest to lowest, and save in a new file in your directory called sorted.cuffdiff.out
    - Sort the file (log fold change highest to lowest) then print out only the first 100 lines. Save in a file called `top100.sorted.cuffdiff.out`.
    - Sort the file by log fold change, print out the top 100, print only first column. This will be a list of the genes with the largest change in expression. Make sure your list is sorted by gene name and is unique. Save this curated list in a file called `differentially.expressed.genes.txt`.

```bash
# - Look at the first few lines of the file
head -n 3 cuffdiff.txt 
# - Sort the file by log fold change 'log2(fold_change)', from highest to lowest, and save in a new file in your directory called sorted.cuffdiff.out

sort -k 10 -g -r cuffdiff.txt >sorted.cuffdiff.out

# - Sort the file (log fold change highest to lowest) then print out only the first 100 lines. Save in a file called `top100.sorted.cuffdiff.out`.

sort -k 10 -g -r cuffdiff.txt | head -n 100 >top100.sorted.cuffdiff.out

# - Sort the file by log fold change, print out the top 100, print only first column. This will be a list of the genes with the largest change in expression. Make sure your list is sorted by gene name and is unique. Save this curated list in a file called `differentially.expressed.genes.txt`.

sort -k 10 -g -r cuffdiff.txt | head -n 100 | cut -f 1 | sort | uniq  >differentially.expressed.genes.up.txt

```

__Cuffdiff file format__

| Column number | Column name       | Example              | Description                              |
| ------------- | ----------------- | -------------------- | ---------------------------------------- |
| 1             | Tested id         | XLOC_000001          | A unique identifier describing the transcipt, gene, primary transcript, or CDS being tested |
| 2             | Tested id         | XLOC_000001          | A unique identifier describing the transcipt, gene, primary transcript, or CDS being tested |
| 3             | gene              | Lypla1               | The gene_name(s) or gene_id(s) being tested |
| 4             | locus             | chr1:4797771-4835363 | Genomic coordinates for easy browsing to the genes or transcripts being tested. |
| 5             | sample 1          | Liver                | Label (or number if no labels provided) of the first sample being tested |
| 6             | sample 2          | Brain                | Label (or number if no labels provided) of the second sample being tested |
| 7             | Test status       | NOTEST               | Can be one of OK (test successful), NOTEST (not enough alignments for testing), LOWDATA (too complex or shallowly sequenced), HIDATA (too many fragments in locus), or FAIL,  when an ill-conditioned covariance matrix or other numerical exception prevents testing. |
| 8             | FPKMx             | 8.01089              | FPKM of the gene in sample x             |
| 9             | FPKMy             | 8.551545             | FPKM of the gene in sample y             |
| 10            | log2(FPKMy/FPKMx) | 0.06531              | The (base 2) log of the fold change y/x  |
| 11            | test stat         | 0.860902             | The value of the test statistic used to compute significance of the observed change in FPKM |
| 12            | p value           | 0.389292             | The uncorrected p-value of the test statistic |
| 13            | q value           | 0.985216             | The FDR-adjusted p-value of the test statistic |
| 14            | significant       | no                   | Can be either "yes" or "no", depending on whether p is greater then the FDR after Benjamini-Hochberg correction for multiple-testing |

