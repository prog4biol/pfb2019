Python 6 - IO - Problem Set
===================

1. Write a script to do the following to [Python_06.txt](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_06.txt)
   - Open and read the contents.  
   - Uppercase each line
   - Print each line to the STDOUT


2. Modifiy the script in the previous problem to write the contents to a new file called "Python_06_uc.txt"


3. Open and print the reverse complement of each sequence in [Python_06.seq.txt](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_06.seq.txt). Each line is the following format:    `seqName\tsequence\n.` Make sure to print the output in fasta format including the sequence name and a note in the description that this is the reverse complement. Print to STDOUT and capture the output into a file with a command line redirect '>'. 
   - **Remember is is always a good idea to start with a test set for which you know the correct output.**

4. Open the [FASTQ](https://en.wikipedia.org/wiki/FASTQ_format) file [Python_06.fastq](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_06.fastq) and go through each line of the file. Count the number of lines and the number of characters per line. Have your program report the:  
    - total number of lines  
    - total number of characters  
    - average line length   

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

_In the same Ensembl window, follow the steps below to get genes that have been labeled with Gene Ontology term "pigmentation". For extra information on pigmentation, check out [pigmentation](http://purl.obolibrary.org/obo/GO_0043473)_


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


## Extra: Expand on an exercise from ProblemSet 5 on nucleotide composition
  - get the raw file [Python_06.seq.txt](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_06.seq.txt)
  - in a script, open this file
  - iterate over each line in this file (seqName\tsequence\n)
     - for each sequence:
         - calculate and store the count of each unique nucleotide character in a dictionary
         - report the name, total of each nucleotide count, and the GC content 

