# 1. CRISPR genome wide guide RNA generator

### TA Matt

1) Precompute activation, deletion, and interference CRISPR guide RNAs for any genome (uploaded FASTA) for all genes (uplodaed gff3). 

Note: interference CRISPR guide RNAs need TSS to be included in gff.

2) Compute activation, deletion, or interference CRISPER guide RNAs on a user targeted locus in a genome FASTA. 

3) Visualize genome wide guide RNAs in a genome browser.





































# 2. DAta MaNagement Interface Tool (DAMNIT)

### TA Jessen



The volume of sequencing data being produced continues to out-pace the ability to store and efficiently manage it. I propose a software development project to build a command-line application for managing and archiving data files with a Git-like interface. The software is envisioned to 1) traverse directories on a file system and archive only new or modified files, providing a non-redundant data store; 2) detect files with identical contents (but not necessarily identical names) to already-archived files via SHA checksums; 3) perform file comparison and only store differences (changes) in file contents using time-stamped tarballs; 4) store user-defined file/project metadata; 5) implement an interface to search for and list previously-archived files; and 6) retrieving all root files and apply changes while unarchiving.

 

**Programming concepts required by the project:**

1.   Use of common Python data structures, especially dictionary insertion and look-up

2.   Using modules (including os, sys, pickle, subprocess, hashlib)

3.   Interfacing with the operating system using built-in Python functions and the subprocess module

4.   Implementing depth-first and breadth-first recursive algorithms














































# 3. Text-based Turn Game

### TA Shasta
 

**Project description:**

A text-based turn game is a terminal-based interactive gaming style usually involving gameplay genres in the realms of escape rooms and strategy games. The user is typically thrust into a first-person scenario in which he/she is required to use his/her wits to survive and escape a risky scenario. For this project I propose writing a text-based turn game as an exercise in modular and collaborative code development. This project will leverage object-oriented programming to build the user’s character, monsters, and environments the user must navigate. The user will collect and store items and weapons, inspect their surroundings, and fight or flee from enemies in his/her attempt to escape their perilous plight. 

 

**Programming concepts required by the project:**

1.   Accept terminal input from the player to prompt actions

2.   Construct object classes with an abstract interface for people, monsters, etc. which will enable interaction between them (fight, converse).

3.   Modular programming. Each situation a user is presented with in the text-based game world is potentially a different module to be loaded in a main command script. Given a well-planned character object development, programmers will be able to construct scenarios (i.e., modules) that plug into the main program.

4.   Use the `random` module to introduce an element of chance into the gameplay.















































# 4. Web Application for Querying existing (sc)RNA-seq Data and displaying plots etc 

### TA Daniel

Create a web tool with a data dashboard for visualizing and exploring publicly available single cell RNAseq data. This could include gene lists, tsne clustering, searches by gene annotations (GO terms), cluster enrichment for GO terms, Gene searches.




















































## 5. DNA sequence analysis


### TA Joe

DNA sequence analysis: kmer words


DNA is not a random sequence of bases, rather it comprises kmers that are over-represented ('DNA words'). This project will analyze reference genome sequences to find all such DNA words, running statistical tests to determine which are over-represented, and subsequent analysis will investigate relationships between these words and known motifs and/or functions. Then, we will convert these motifs into English (based on word use abundance) and use Python's natural language toolkit to search for chance occurrences grammatical comprehensibility.  


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

# 6. Variant calling and mapping SNPs to proteins

### TA Kirsten

Somatic Variant calling (different from regular variant calling) Pipeline. Part of the project is to determine the differences. Include variant effect prediction (is there there a frame shift??). Are these SNPs found in public databases?
 
Visualize the variant in the protein sequence.








































# 7 RNASeq Analysis Pipeline with Mystery Unaligned Reads

### TA TBD

Build a Python Pipeline for RNAseq Analysis which includes trimming, aligning, quantifying, and testing for differential expression. Then take all unaligned reads and identify your contaminate/symbiote/organelle. 

To enrich your differential expression analysis incorporate transcript annotation/Gene Ontology/Pathways/Panther.

Is any of the differential expression between samples potentially caused by variants? Call SNPs and predict variant effect on transcripts.







 

