NGS Workshop Tutorial
=====================

**NOTE:** Unless otherwise specified, example command lines are available in this workshop's [lecture notes](https://github.com/prog4biol/pfb2019/blob/master/workshops/NGS/bio_info_formats.pdf) 

1. Download the [genome](https://github.com/prog4biol/pfb2019/blob/master/workshops/NGS/data/Scerevisiae.fasta.gz) and [annotation](https://github.com/prog4biol/pfb2019/blob/master/workshops/NGS/data/Scerevisiae.gff3.gz) files using `wget`, then decompress them with `gunzip`.

2. Index the genome as described in the lecture notes.

3. Download the reads with SRR number `SRR10178655` from the SRA and convert to FASTQ format:
   ```bash
   # Fetch the .sra container file from the SRA FTP:
   wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR101/SRR10178655/SRR10178655.sra
   # Use SRA Toolkit to extract the reads in FASTQ format:
   fastq-dump --gzip --split-files --defline-seq '@$sn/$ri' --defline-qual '+' SRR10178655.sra
   ```

4. Run FastQC on the FASTQ files and examine the report (see `fastqc --help` for a complete list of options).
   - How many read pairs are in included in the FASTQ file?
   - How long are the reads?
   - What quality encoding are the reads in? What is the quality offset?
   - For which metrics are there warnings?
   - Are there any over-represented sequences in the file? If so, what is it?

5. Next, run the Trimmomatic adapter trimmer on the FASTQ files in "PE" mode, using this [adapter file](https://github.com/prog4biol/pfb2019/blob/master/workshops/NGS/data/adapters.fa). What fraction of the data were discarded?

6. Align the reads to the genome sequence using BWA-MEM. Convert the file to BAM format, sort the BAM file, and index it (see lecture notes for how).

7. Now, Run GATK's `MarkDuplicates` tool on the BAM file to identify optical and PCR duplicate reads.

8. Run `samtools stats` and `plot-bamstats` on the BAM file and examine the results, in particular, the "Mismatches per cycle" plot. Below which base quality score do the majority of mismatches occur?

9. Use `samtools view` to keep alignments with `PAIRED` and `PROPER_PAIR` flags *AND DO NOT* contain `UNMAP`, `MUNMAP`, `SECONDARY`, `QCFAIL`, `DUP`, or `SUPPLEMENTARY` flags; write the output as a BAM file. Index this new file with SAMtools (*HINT*: see `samtools flags` for help with flags).

10. Using the base quality score determined in *Step 8*, call SNPs using the GATK HaplotypeCaller.

11. Use the `samtools depth` command to calculate the per-site depth of reads in the genome (see `samtools depth --help` for more info). The output file contains three columns: the chromosome name, position (1-based), and depth. For example:
    ```
    chrI	1	15
    chrI	2	15
    chrI	3	14
    chrI	4	16
    chrI	5	16
    ```
    
12. Write a script that computes a text histogram of depth with output similar to the following:
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

13. Filter SNPs and Indels for variant loci within the center 95% of the depth distribution (use your distribution from above; estimating by eye is fine). To filter loci, use VCFtools:
    ```bash
    vcftools --recode --stdout --max-missing 1 --minDP <lower-threshold> --maxDP <upper-threshold> --vcf <your.vcf> >your.filtered.vcf

14. Finally, how many of these SNPs and Indels intersect gene loci? (*HINT*: use `bedtools intersect` to do this to extract unique loci).

**BONUS:** Try loading the genome FASTA, annotation GFF3, and filtered SNPs into [IGV](https://software.broadinstitute.org/software/igv)
   - Open IGV
   - Navigate through `Genomes` => `Load Genomes from File...` and select the genome FASTA file.
   - Navigate `File` => `Load from File...` and load a VCF/GFF3/BED file.

