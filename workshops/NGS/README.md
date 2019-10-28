NGS Workshop Tutorial
=====================
To See answers to the below questions, go to Jessen's the answers branch of his [repo](https://github.com/bredeson/pfb2019/blob/answers/workshops/NGS/README.md).

**NOTE:** Unless otherwise specified, example command lines are available in this workshop's [lecture notes](https://github.com/bredeson/pfb2019/blob/master/workshops/NGS/bio_info_formats.pdf) 

1. First, install the `gnuplot` command line plotting software using HomeBrew:
   ```bash
   brew install gnuplot
   ```
   
2. Download the sofware required for this tutorial using `wget` from `https://www.dropbox.com/s/zn4m0oqbasg4gal/software.tar.gz`. Unarchive the files by typing `tar -xzvf software.tar.gz`. Finally, add the `software/bin` directory to your `$PATH` environment variable:
   ```bash
   export PATH=$PWD/software/bin:$PATH;
   ```
   **NOTE**: You need to replaced `$PWD` above with the full, expanded path the the `software/bin` dir if you put the `export` statement in your `.bash_profile` or `.bashrc`. 

3. Download the [genome](https://www.dropbox.com/s/goo2bt4br9mqxtt/Scerevisiae.fasta.gz) and [annotation](https://www.dropbox.com/s/uq8mfp125jlgknq/Scerevisiae.gff3.gz) files using `wget` and decompress them both with `gunzip`.

4. Index the genome as described in the lecture notes.

5. Download the reads with SRR number `SRR10178655` from the SRA and convert to FASTQ format:
   ```bash
   # Fetch the .sra container file from the SRA FTP:
   wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR101/SRR10178655/SRR10178655.sra
   # Use SRA Toolkit to extract the reads in FASTQ format:
   fastq-dump --gzip --split-files --defline-seq '@$sn/$ri' --defline-qual '+' SRR10178655.sra
   ```

6. Run FastQC on the FASTQ files and examine the report (see `fastqc --help` for a complete list of options).
   - How many read pairs are in included in the FASTQ file?
   - How long are the reads?
   - What quality encoding are the reads in? What is the quality offset?
   - For which metrics are there warnings?
   - Are there any over-represented sequences in the file? If so, what is it?

7. Next, run the Trimmomatic adapter trimmer on the FASTQ files in "PE" mode, using this [adapter file](https://www.dropbox.com/s/tpmhcz24jluq97s/adapters.fa). What fraction of the data were discarded? **NOTE**: Trimmomatic is in it's own subdirectory `sofware/Trimmomatic-0.39/trimmomatic-0.39.jar`.

8. Align the reads to the genome sequence using BWA-MEM. Convert the file to BAM format, sort the BAM file, and index it (see lecture notes for how).

9. Now, Run GATK's `MarkDuplicates` tool on the BAM file to identify optical and PCR duplicate reads.

10. Run `samtools stats` and `plot-bamstats` on the BAM file and examine the results.
    - What is the mode insert size of the sequencing library?
    - What is the estimated read base-call error rate?
    - What fraction of your reads are duplicates?
    - Within which base quality score range do the majority of mismatches occur? (*HINT*: see the "Mismatches per cycle" plot). Record the upper value of the range to use as the minimum base quality threshold for variant calling a later step.

11. Use `samtools view` to keep alignments with `PAIRED` and `PROPER_PAIR` flags *AND DO NOT* contain `UNMAP`, `MUNMAP`, `SECONDARY`, `QCFAIL`, `DUP`, or `SUPPLEMENTARY` flags; write the output as a BAM file. Index this new file with SAMtools (*HINT*: see `samtools flags` for help with flags). Be sure to index your filtered BAM file.

12. Using the base quality score determined in *Step 10* as the minimum base quality threshold, call SNPs using the GATK HaplotypeCaller.

13. Use the `samtools depth` command to calculate the per-site depth of reads in the genome (see `samtools depth --help` for more info). The output file contains three columns: the chromosome name, position (1-based), and depth. For example:
    ```
    chrI	1	15
    chrI	2	15
    chrI	3	14
    chrI	4	16
    chrI	5	16
    ```
    
14. Write a script that computes a text histogram of depth with output similar to the following:
    ```
     1 |                                        
     2 |]                                       
     3 |]]                                      
     4 |]]]]]                                   
     5 |]]]]]]]]                                
     6 |]]]]]]]]]]]]]                           
     7 |]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]  
     8 |]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
     9 |]]]]]]]]]]]]]]]]]]]]]]]]]]]             
    10 |]]]]]]]]]]]]]]]                         
    11 |]]]]]]]]]                               
    12 |]]]]]                                   
    13 |]                                       
    14 |]                                       
    15 |                                        
    ```

15. Filter SNPs and Indels for variant loci within the center 95% of the depth distribution (use your distribution from above; estimating by eye is fine). To filter loci, use VCFtools:
    ```bash
    vcftools --recode --recode-INFO-all --stdout --max-missing 1 --minDP <lower-threshold> --maxDP <upper-threshold> --vcf <your.vcf> >your.filtered.vcf

16. Finally, how many of these SNPs and Indels intersect CDS features? (*HINT*: extract CDS features into a new GFF3 file and use `bedtools intersect` to do this to extract unique SNP loci).

**BONUS:** Try loading the genome FASTA, annotation GFF3, and filtered SNPs into [IGV](https://software.broadinstitute.org/software/igv)
   - Open IGV
   - Navigate through `Genomes` => `Load Genomes from File...` and select the genome FASTA file.
   - Navigate `File` => `Load from File...` and load a VCF/GFF3/BED file.


