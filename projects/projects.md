# 1. CRISPR genome wide guide RNA generator

TA: Matt  
TeamName: litterbox  
GitHub Repo:  https://github.com/mrwaas/funny_CRISPR_pun  
Participants:  
 - Zach
 - Becky
 - Doug
 - Hunter
 - John
 - Mina
 
Project Desc:  

Cat Piss: CRISPR Anotation Tool for Parsing In Silico Sequences

1) Precompute activation, deletion, and interference CRISPR guide RNAs for any genome (uploaded FASTA) for all genes (uplodaed gff3). 

Note: interference CRISPR guide RNAs need TSS to be included in gff.

2) Compute activation, deletion, or interference CRISPER guide RNAs on a user targeted locus in a genome FASTA. 

3) Visualize genome wide guide RNAs in a genome browser.



# 2. DAta MaNagement Interface Tool (DAMNIT)

TA: Jessen    
TeamName: DAMNIT (**DA**ta **M**a**N**agement **I**nterface **T**ool)  
GitHub Repo: https://github.com/katiemharding/ProjectDAMNIT    
Participants:   
 - Omer  
 - Katie  

Project Desc:  

The volume of sequencing data being produced continues to out-pace the ability to store and efficiently manage it. This software development project endeavors to build a command-line application for managing and archiving data files with a Git-like interface. The software was envisioned to 1) traverse directories on a file system and archive only new or modified files, providing a non-redundant data store; 2) detect files with identical contents (but not necessarily identical names) to already-archived files via SHA checksums; 3) perform file comparison and only store differences (changes) in file contents using time-stamped tarballs; 4) store user-defined file/project metadata; 5) implement an interface to search for and list previously-archived files; and 6) retrieving all root files and apply changes while unarchiving.

**Programming concepts exercised by the project:**

1.   Use of common Python data structures, especially dictionary insertion and look-up

2.   Using modules (including os, sys, json, subprocess)

3.   Interfacing with the operating system using built-in Python functions and the subprocess module (especially with `diff`, `patch`, and `md5`)

4.   Implementing depth-first and breadth-first recursive algorithms



# 3. Command Line Adventure Game

TA: Shasta  
TeamName: VI (visiually impaired)  
GitHub Repo:  https://github.com/webbshasta/pfb2019_VisuallyImpaired  
Participants:    
 - Renee  
 - Cody
 - Mareike
 - Carla
 - Kelsey

Project Desc:  


The main goal of this project was to create a command line adventure game. In this game, a user first fills out a personality quiz, which generates a character for them. Each character comes pre-set with certain attributes which can change throughout the game. This game creates an object class called "user" which creates a user object with a series of attributes and methods. This object is then used in a game script that calls multiple modules individually written by team members. The user object is adjusted based on encounters in the game.

This game incorporates the following programming concepts:

1.   Accept terminal input from the player to prompt actions

2.   Construct object classes with an abstract interface for characters.

3.   Modular programming. Each situation a user is presented with in the text-based game world is a different module to be loaded in a main command script. Given a well-planned character object development, programmers will be able to construct scenarios (i.e., modules) that plug into the main program.

4.   Use the `random` module to introduce an element of chance into the gameplay.

5. Create modules that can be called for formatting output. 



# 4. Web Application for Querying existing (sc)RNA-seq Data and displaying plots etc 

TA: Daniel  
TeamName: FISH n' SEQ: Facilitative Illustration by/for Stupid Humans  
GitHub Repo:  https://github.com/JulianKimura/FISHn-SEQ  

Participants:  
 - Luca 
 - Agusto
 - Nicole
 - Julien
 - Manny

Project Desc:  

Create a web tool with a data dashboard for visualizing and exploring publicly available single cell RNAseq data. This could include gene lists, tsne clustering, searches by gene annotations (GO terms), cluster enrichment for GO terms, Gene searches.






## 5. DNA sequence analysis


TA: Joe  
TeamName: MERKat  
GitHub Repo:  https://github.com/nomascus/MERKat  
Participants:  
 - Alissa
 - Diyendo

Project Desc:  

DNA sequence analysis: kmer words


DNA is not a random sequence of bases, rather it comprises kmers that are over-represented ('DNA words'). This project will analyze reference genome sequences to find all such DNA words, running statistical tests to determine which are over-represented, and subsequent analysis will investigate relationships between these words and known motifs and/or functions. Then, we will convert these motifs into English (based on word use abundance) and use Python's natural language toolkit to search for chance occurrences grammatical comprehensibility.  






# 6 RNASeq Analysis Pipeline with Mystery Unaligned Reads

TA: Kirsten  

TeamName: RNA1   

GitHub Repo: https://github.com/kirstengott/pfb2019_rna1  

Participants:  
 - Marina
 - Cynthia
 - Brooke
 - Marya

Project Desc:  

Build a Python Pipeline for RNAseq Analysis which includes trimming, aligning, quantifying, and testing for differential expression. Then take all unaligned reads and identify your contaminate/symbiote/organelle. 

To enrich your differential expression analysis incorporate transcript annotation/Gene Ontology/Pathways/Panther.

Is any of the differential expression between samples potentially caused by variants? Call SNPs and predict variant effect on transcripts.







 

