Problem Set Answers from Mike
=============================

1. **Log into your machine.** 
This is easy on a mac. For a remote server you would have to use ssh. On a mac you open a terminal window and you are ready to go
     ```sh
     jabberwocky:scratch mcampbel$
     ```

2. **What is the full path to your home directory?**
Use pwd for this
	```sh
	jabberwocky:scratch mcampbel$ pwd
	/Users/mcampbel/foo/scratch
	```
3. **Go up one directory and How many directories?**
 * **Go up one directory?**
       	  Use cd and ls for this
	```sh
	jabberwocky:scratch mcampbel$ cd ..
	jabberwocky:foo mcampbel$
	```
 * **How many directories?**
   
	```sh
	jabberwocky:foo mcampbel$ ls -1 -F
	all_betas_no_missing_data.txt
	cns_p_ctg_uc.fasta.gz
	get_10000_exons.py*
	gff3_stuff.py*
	head_hexamer_counts.txt
	internal-exons.fasta
	multiple_trans_example.gff
	pn_chr.fa.gz
	quickmerge/
	repeat_notes_from_george.txt
	scratch/
	smaller_genes_only.gff
	subset_fasta.py*
	tail_hexamer_counts.txt
	tids.txt
	tig00000022.gff
	v4_pc_genes_longest_cds.gff
	```
looks like I have 2 directories and 15 files

4. **Make a directory called problemsets.**
Use mkdir for this one
	```sh
	jabberwocky:foo mcampbel$ mkdir problemsets
	```
5. **Navigate into this new directory called problemsets. Verify that you are in the correct directory by using pwd.** 
	```sh
	jabberwocky:foo mcampbel$ cd problemsets
	jabberwocky:problemsets mcampbel$ pwd
	/Users/mcampbel/foo/problemsets
	```
6. **Use wget to copy https://raw.githubusercontent.com/srobb1/pfb2017/master/files/sequences.nt.fa from the web into your problemsets directory. If wget is not available on your system, use curl -O as an alternative.**
we didn't have wget on the macs in class so we had to use curl
	```sh
	jabberwocky:problemsets mcampbel$ curl -O https://raw.githubusercontent.com/srobb1/pfb2017/master/files/sequences.nt.fa
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
	100 10267  100 10267    0     0  21711      0 --:--:-- --:--:-- --:--:--  113k
	```
but wget would work too
	```sh
	wget https://raw.githubusercontent.com/srobb1/pfb2017/master/files/sequences.nt.fa
	--2017-10-16 19:30:36--  https://raw.githubusercontent.com/srobb1/pfb2017/master/files/sequences.nt.fa
	Resolving raw.githubusercontent.com... 151.101.20.133
	Connecting to raw.githubusercontent.com|151.101.20.133|:443... connected.
	HTTP request sent, awaiting response... 200 OK
	Length: 10267 (10K) [text/plain]
	Saving to: 'sequences.nt.fa.1'
	
	sequences.nt.fa.1     100%[==========================>]  10.03K  --.-KB/s   in 0s     
	
	2017-10-16 19:30:37 (59.0 MB/s) - 'sequences.nt.fa.1' saved [10267/10267]
	```
7. **This is a 5 part question** 
 * **How many lines does this file contain?**
	```sh
	jabberwocky:problemsets mcampbel$ wc -l sequences.nt.fa 
	     148 sequences.nt.fa
	```
 * **How many characters? (Hint: check out the options of wc)**
	```sh
	jabberwocky:problemsets mcampbel$ wc -c sequences.nt.fa 
	   10267 sequences.nt.fa
	```

 * **What is the first line of this file? (Hint: read the man page of head)**
	```sh
	jabberwocky:problemsets mcampbel$ head -n 1 sequences.nt.fa 
	>NM_001126114.2 Homo sapiens tumor protein p53 (TP53), transcript variant 3, mRNA
	```
 * **What are the last 3 lines? (Hint: read the man page of tail)***
	```sh
	jabberwocky:problemsets mcampbel$ tail -n 3 sequences.nt.fa 
	TTTATAGCTGTTGGAAGGACTAGGTCTTCCCTAGCCCCCCCAGTGTGCAAGGGCAGTGAAGACTTGATTG
	TACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAA
	AAAAAAAAAAAAAA
	```

 * **How many sequences are in the file? (Hint: use grep) (Note: The start of a sequence is indicated by a > character.)**
	```sh
	jabberwocky:problemsets mcampbel$ grep '>' sequences.nt.fa | wc -l
	       2
	```
Note: you can also do the counting with the grep option -c
	```sh
	jabberwocky:problemsets mcampbel$ grep -c '>' sequences.nt.fa 
	2
	```

8. **Rename sequences.nt.fa to cancer_genes.fasta. (Hint: read the man page for mv)** 
	```sh
	jabberwocky:problemsets mcampbel$ mv sequences.nt.fa cancer_genes.fasta
	```
9. **Copy this remote file: https://raw.githubusercontent.com/srobb1/pfb2017/master/files/cuffdiff.txt to your problemset directory.**

Use wget again
	```sh
	jabberwocky:problemsets mcampbel$ wget https://raw.githubusercontent.com/srobb1/pfb2017/master/files/cuffdiff.txt
	--2017-10-16 19:37:44--  https://raw.githubusercontent.com/srobb1/pfb2017/master/files/cuffdiff.txt
	Resolving raw.githubusercontent.com... 151.101.20.133
	Connecting to raw.githubusercontent.com|151.101.20.133|:443... connected.
	HTTP request sent, awaiting response... 200 OK
	Length: 1113672 (1.1M) [text/plain]
	Saving to: 'cuffdiff.txt'
	
	cuffdiff.txt          100%[==========================>]   1.06M  --.-KB/s   in 0.08s  
	
	2017-10-16 19:37:45 (12.9 MB/s) - 'cuffdiff.txt' saved [1113672/1113672]
	```

10. **This one is five parts** 
  * **Look at the first few lines of the file**
	```sh
	jabberwocky:problemsets mcampbel$ head -n 2 cuffdiff.txt 
	AC148152.3_FG006	AC148152.3_FG006  AC148152.3_FG006	Chr2:231237971-231241387	B73.s	Mo17.s	NOTEST	0.0125804 0 -1.79769e+308 -1.79769e+308 0.32736 1 no
	AC148152.3_FG008	AC148152.3_FG008  AC148152.3_FG008	Chr2:231209190-231213723	B73.s	Mo17.s	OK	5.83386	  0.0236324	  -5.50882	4.61463.93829e-06 0.000124139 yes
	```
   * **Sort the file by log fold change 'log2(fold_change)', from highest to lowest, and save in a new file in your directory called sorted.cuffdiff.out**
	```sh
	jabberwocky:problemsets mcampbel$ sort -k 10 -g -r cuffdiff.txt > sorted.cuffdiff.out
	```
   * **Sort the file (log fold change highest to lowest) then print out only the first 100 lines. Save in a file called top100.sorted.cuffdiff.out.**
	```sh
	jabberwocky:problemsets mcampbel$ head -n 100 sorted.cuffdiff.out > top100.sorted.cuffdiff.out
	```
   * **Sort the file, print only first column. Get a unique list of the genes, then print only the top 100. Save in a file called differentially.expressed.genes.txt.**
we need cut and uniq for this
	```sh
	jabberwocky:problemsets mcampbel$ cut -f 1 sorted.cuffdiff.out | sort | uniq | head -n 100 > differentially.expressed.genes.txt
	```

This does what the questions asks but it the second sorting will mess up the first sort. The result of this is an asci sorted list of gene names.  

To get the top 100 most diferentialy expressed genes I would start by checking for duplicate ids.
	```sh
	jabberwocky:problemsets mcampbel$ cut -f 1 sorted.cuffdiff.out | sort | wc -l
	    8256
	jabberwocky:problemsets mcampbel$ cut -f 1 sorted.cuffdiff.out | sort -u | wc -l
	    8256
	```

Looks like there are no duplicated gene ids so I don't have to worry about getting rid of duplicates.
	```sh
	jabberwocky:problemsets mcampbel$ cut -f 1 sorted.cuffdiff.out | head -n 100 > differentially.expressed.genes.txt
	```

Now this file will have what you are hoping for.

