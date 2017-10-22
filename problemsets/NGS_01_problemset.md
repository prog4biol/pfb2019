NGS 1 Problem Set
=================

1. Write a script to count the number of sequences in a [FASTQ](../files/pfb.fastq) file.
	- Output the mean and standard deviation of sequence lengths
   	- Calculate the mean and standard deviation of base quality scores.
2. Write a script to trim each sequence in a FASTQ file starting from the first base in each sequence lower than Q=20 to the end of the sequence. (don't forget to trim the quality scores as well)
3. Write a script to parse a [GFF3](../files/cab_sav_contig.gff) file.
	- Print the average gene length
	- Print the average exon length
	- Print the average number of exons per mRNA
	- Print the number of exons in each mRNA (use the "Parent=" tag in column 9 of the exon lines to tie the exons to the mRNAs) 
4. Make your script read the [FASTA](../files/cab_sav_contig.fasta) file that goes with the GFF3 file.
   	- Calculate the GC content of the sequence in the FASTA file
	- Calculate the GC content of the gene features
	- Calculate the GC content of the exon features
	- Calculate the GC contents of the introns (bonus: this feature is implied and not explicit in most GFF3 files)
	
