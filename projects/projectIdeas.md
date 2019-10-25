# 1. (CRISPRi/a) guide RNA design tool

 

**Goal:**

\-    CRISPR guide RNA design tool for CRISPRi (interference) or CRISPRa (activation) and/or normal Cas9 CRISPR. Given a gene (or list of genes) that you are interested in, what are the optimal guide RNAs (gRNAs) to use for gene repression or activation? 

\-    [Similar design tools](https://portals.broadinstitute.org/gpp/public/analysis-tools/sgrna-design) exist for generating CRISPR knockouts, but none are available for CRISPRa/i. Using CRISPRa/i requires gRNAs with different parameters – namely, close proximity to the transcription start site (TSS)

\-    Note that CRISPRi/a screening has been widely used in human cells and thus you could probably find the best guides for a given gene for human cells. However, the optimal CRISPRi/a guides may not have been identified in your organism of interest. In addition, your cell/tissue of interest may have specific/unique TSS sites, so it would be nice to be able to integrate TSS site data (for example, CAGE data for TSS mapping) to inform your guide RNA selection.

 

**Inputs into program:**

\-    gene (or list of genes of interest) that you want to target

\-    TSS site data

o  Option 1: Use just annotated TSSs in the genome

o  Option 2: Alternatively: choose TSSs based on analysis of existing [Cap Analysis of Gene Expression (CAGE)](http://fantom.gsc.riken.jp/protocols/basic.html) data for your cell/tissue type of interest.

o  Could be expanded to other sites with a bed file input.

\-    List of potential gRNA sites in the genome (genomic coordinates available)

o  For many organisms, genomic coordinates of sites are available as easily parse-able formats (bed or bigbed files)

o  We could incorporate a module where someone finds all the potential gRNA sites *de novo* for a less-annotated genome.

 

### TA Matt

1. 

2.

3.

4

5





# **2. DAta MaNagement Interface Tool (DAMNIT)**



The volume of sequencing data being produced continues to out-pace the ability to store and efficiently manage it. I propose a software development project to build a command-line application for managing and archiving data files with a Git-like interface. The software is envisioned to 1) traverse directories on a file system and archive only new or modified files, providing a non-redundant data store; 2) detect files with identical contents (but not necessarily identical names) to already-archived files via SHA checksums; 3) perform file comparison and only store differences (changes) in file contents using time-stamped tarballs; 4) store user-defined file/project metadata; 5) implement an interface to search for and list previously-archived files; and 6) retrieving all root files and apply changes while unarchiving.

 

**Programming concepts required by the project:**

1.   Use of common Python data structures, especially dictionary insertion and look-up

2.   Using modules (including os, sys, pickle, subprocess, hashlib)

3.   Interfacing with the operating system using built-in Python functions and the subprocess module

4.   Implementing depth-first and breadth-first recursive algorithms



### TA Jessen

1. 

2.

3.

4

5




# **3. Text-based Turn Game**

 

**Project description:**

A text-based turn game is a terminal-based interactive gaming style usually involving gameplay genres in the realms of escape rooms and strategy games. The user is typically thrust into a first-person scenario in which he/she is required to use his/her wits to survive and escape a risky scenario. For this project I propose writing a text-based turn game as an exercise in modular and collaborative code development. This project will leverage object-oriented programming to build the user’s character, monsters, and environments the user must navigate. The user will collect and store items and weapons, inspect their surroundings, and fight or flee from enemies in his/her attempt to escape their perilous plight. 

 

**Programming concepts required by the project:**

1.   Accept terminal input from the player to prompt actions

2.   Construct object classes with an abstract interface for people, monsters, etc. which will enable interaction between them (fight, converse).

3.   Modular programming. Each situation a user is presented with in the text-based game world is potentially a different module to be loaded in a main command script. Given a well-planned character object development, programmers will be able to construct scenarios (i.e., modules) that plug into the main program.

4.   Use the `random` module to introduce an element of chance into the gameplay.



### TA Shasta

1. 

2.

3.

4

5





# 6+4. Web Application for Querying existing (sc)RNA-seq Data and displaying plots etc 

Querying analyses generated from NGS data typically requires programming skills that are not formally taught to biologists. A typical bench researcher who generates such data can be wholly dependent on a collaborator proficient in writing code to extract meaningful patterns. Unfortunately, the number of datasets being generated far outweighs the number of individuals capable of analyzing the data. This phenomena has led to a bottleneck in NGS analysis. Indeed, there are some aspects of analysis that are time consuming and simply require programming literacy, however, there are other aspects can be very repetitive, particularly with tasks that are aimed towards generating figures for exploring data. These short repetitive tasks are a great candidate for a new type of web application written in high level programming languages such as Python and R. This allows an individual with basic programming skills to create an interactive app without any experience in web development. Here we propose a simple application for exploring single cell RNA seq data where the end user can create heatmaps and scatterplots based on their genes of interest. This application can not only reduce the workload for the bioinformatician, but also facilitates collaboration and data exploration. 



#### (  Continuation of previous project RNAseq data cleanup, analysis and visualization for data sets such as unidentified metagenomics RNAseq reads)

Input style: curated bacterial RNA or RNA-seq analyses from well annotated repository of diverse bacteria



When dealing with RNAseq from organisms containing obligate, facultative, opportunistic and pathogenic symbionts, read alignments are never 100%. Usually, a large proportion of total reads will align to the host organism, while the rest remain unmapped, and unknown. What to do with these reads? There are currently a fair number of metatranscriptomic microbiome pipelines. To expand this repertoire, we will develop two tools. The first pipeline will input orphaned reads and blast them to attempt a taxonomy assignment. The second pipeline will verify taxonomy for one gene of interest by identifying homologs present in distant organisms through blast. The full report will give thorough discussions on the statistics used including the probability that our proteins are found in the database and the probability that our results would occur by chance. The goal would be to show the reproducibility by using standard statistics and well described methods.

The data generated from various RNA-seq pipelines seem to follow a trend and often consist of: gene name, unique reads mapped, total reads mapped, expression values and some comparison value relative to wildtype. However, tools for processing the output are not as readily available and are often tailored to each experiment. The goal of this pipeline is to provide such a tool for generic data handling between a WT and mutant/condition. We have a lot of ideas and are trying to make a story out of our selfish desires so bear with us its almost over. To do so, a script will be written that parses RNA-seq data, trimms the data based on stringent parameters, and produces a tabular output of the RNA-seq expression data that has been deemed reliable. A second script will assign scores to ontology classes (obtained and parsed from KEGG) and generate a figure depicting general trends in the bacteria’s transcriptome. Finally, if time permits, a script will be written to generate a “gene translator.” All coding sequences of one bacterial strain will be blasted against another strain and vice versa. If the same hit is returned with an acceptable E-value, then these genes will be considered the same and appended to the “translator” output file. Genes that do not return a match will also be saved to the translator file, but as a new line (without a match.)

 



#### (continuation of last project idea: Statistical exploration of multiple datasets of transcripts



Data: 

5 datasets of estimation of expression levels of plants in interaction with fungi between 24 to 48 hpi.



Format:

Datasets are in tsv format files (tab spaced), and are normalized in TPM.

g.e:

Name		Lng		TPM		#ReadsMapped

Trinity_c0_i2	352		222		80



Issues to handle:

There is a wide variation of unique transcripts among datasets, this variation can range from 45% to 90% of unique transcripts is each data set.

 

Strategy: basic pipeline to parse the transcripts in order to explore the distribution of the datasets without isoforms (just unique transcripts):

1. Send to a new file the unique transcripts (Unique.txt)
2. Average the repeated isoforms by transcript and get a unique value to represent each transcript.
3. Normalize the data by TPMs.
4. Get the standard deviation of each dataset and send the transcripts inside 3+- [std.dev](http://std.dev/) to Unique.txt (keeping the 95% of the transcripts).
5. Plot the Unique.txt and try to infer what is there based on the new representation of the data.

 





### TA Daniel

1. 

2.

3.

4.

5.



## DNA sequence analysis

DNA is not a random sequence of bases, rather it comprises kmers that are over-represented ('DNA words'). This project will analyse the human genome sequence to find all such DNA words, running statistical tests to determine which are over-represented and subsequent analysis will investigate relationships between these words and known motifs and/or functions (e.g. codons).

### TA Joe

1

2

3

4

5









 

# 5. Variant calling and mapping SNPs to proteins

 

Somatic variant callers have been directed at detection of non-reference alleles (NRAs) present in tumor DNA from surgically acquired tissue. Currently, the common practice is to limit variant detection to allele frequency >5% because artifacts associated with NGS (e.g. PCR errors, sequencing errors) have restricted the use of lower VAF thresholds. Thus, commonly used variant callers (e.g., Strelka2, Mutect2, LoFreq) for “low” frequency variant detection do not interrogate NRAs with a variant allele frequency (VAF) < 1-3%. The development of a variant caller pipeline to adjudicate all NRAs regardless of VAF based on pathogenicity of the variant rather than VAF has applications in understanding tumor phylogeny. Moreover, improved characterization of the overall mutational landscape in solid tumor DNA has the potential to improve the molecular staging of cancer. 

 

Here, we propose to develop a pipeline using a python wrap around each module to handle the input/output between modules. The project will use mpileup files produced from sequencing data of solid tumor DNA representing very early and malignant pancreatic lesions. Each NRA regardless of VAF will be evaluated for variant effect (e.g., nonsense, missense, etc.), predictive protein damage, and cross-referenced against reported pancreatic variants present in the COSMIC database. A subset of patient samples will be used to train the algorithm to distinguish the various stages of pancreatic cancer based on a combined output of variant effect, protein damage, and previous report in COSMIC. Once optimized, the pipeline for variant adjudication will be tested against a new set of patient samples. The analysis will be restricted to exonic SNVs.

 

Resources available:

\1.   ~~Mpileup~~ bam files from tumor DNA capture-panel (118 genes) enriched NGS of pancreatic cancer representing intra-ductal papillary mucinous neoplasm (stage I), stage II-III pancreatic cancer, and stage IV pancreatic cancer.

\2.   The Ensembl Variant Effect Predictor will be used for variant classification including output from SIFT and Polyphen – predictive algorithms that determine if a DNA variant alters/disrupts protein function.

\3.   A database of reported variants associated with human pancreatic lesions has been downloaded from COSMIC.

 

#### (Continuation of last project idea: To create a tool that will map SNPs to a protein sequence )

 

Input:

\1.   Output file from Ensembl with SNP info (see example attached)

\2.   Protein sequence  

Steps: 

\1.   Output data file with SNP information:

a.   The Ensembl genome browser allows you to filter by some parameters and outputs an excel file. I would only export SNPs that are: 

​                        i.     Located in exons

​                       ii.     Missense 

​                      iii.     Alter protein sequence

\2.   Parse and sort the output file:

​                        i.     Extract columns for nucleotide change, amino acid change, amino acid coordinate, SIFT score, and PolyPhen score

\3.   Map affected amino acids to protein sequence 

a.   Only include those with scores that predict that the amino acid change is probably deleterious (SIFT score < 0.05 AND PolyPhen score >0.85)  

 

Additional ideas for features if time permits:

·   Color-code SNPs based on SIFT or PolyPhen scores

·   Add functional domains 

·   Create a graphic 

·   Instead of using amino acid in output file, you could map the chromosomal location to the transcript and then translate the protein sequence



| Variant ID   | vf       | Location  | Chr: bp   | vf_allele | Alleles | gmaf_allele | gmaf_freq | Global MAF | Class | Source | Evidence                                 | Clin. Sig.       | Conseq. Type | AA   | AA coord | AA coord | sift_sort                  | sift_class | SIFT | polyphen_sort | polyphen_class | PolyPhen | cadd_sort     | cadd_class | CADD | revel_sort    | revel_class | REVEL | meta_lr_sort | meta_lr_class | MetaLR | mutation_assessor_sort | mutation_assessor_class | Mutation Assessor | Transcript |
| ------------ | -------- | --------- | --------- | --------- | ------- | ----------- | --------- | ---------- | ----- | ------ | ---------------------------------------- | ---------------- | ------------ | ---- | -------- | -------- | -------------------------- | ---------- | ---- | ------------- | -------------- | -------- | ------------- | ---------- | ---- | ------------- | ----------- | ----- | ------------ | ------------- | ------ | ---------------------- | ----------------------- | ----------------- | ---------- |
| rs1213480778 | 66494864 | 3:6861396 | 3:6861396 | G         | A/G     |             |           | -          | SNP   | dbSNP  | Frequency~gnomAD                         | missense variant | Q/R          | 3    | 3        | 681      | tolerated - low confidence | 0.68       | 1    | benign        | 0              | 16001    | likely benign | 16         | 196  | likely benign | 0.195       | 365   | tolerated    | 0.364         | 171    | neutral                | 0.17                    | ENST00000357716.9 |            |
| rs577556367  | 21937588 | 3:6861397 | 3:6861397 | C         | G/C     | C           | 0.0002    | < 0.001    | SNP   | dbSNP  | Frequency~1000Genomes~ExAC~TOPMed~gnomAD | missense variant | Q/H          | 3    | 3        | 131      | tolerated - low confidence | 0.13       | 1    | benign        | 0              | 15001    | likely benign | 15         | 178  | likely benign | 0.177       | 332   | tolerated    | 0.331         | 264    | low                    | 0.263                   | ENST00000357716.9 |            |





### TA Kirsten

1. 

2.

3.

4

5









 

