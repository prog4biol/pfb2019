# FASTA ([human_cds.fasta](../input_files/human_cds.fasta))
1. Parse the FASTA file in to a dictionary.
2. What is the frequency of each nucleotide in the file?
3. What percentage of each sequence is G or C? make a table with the seqid in the first column and the percent G/C in the second.
4. Stretch goal: (maybe when you get home and are looking for something to do) calculate the entropy in the whole file. 

# FASTQ ([four_reads.fastq](../input_files/four_reads.fastq))
1. trim the first 5 bases off of each read. (remember to trim the quality scores as well)
2. What fraction of the nucleotides in the file have a quality score greater than 30?
3. Stretch goal: trim off any bases from the beginning and end of each read that have a quality of less than 30. 

# SAM ([little_sam.sam](../input_files/little_sam.sam))
1. Read the SAM file into a python script.
2. Use the MI tags to calculate the number of reads per molecule.
3. Stretch goal: Use the MI tags and the alignment position to estimate the average molecule length

# GFF3 ([protein_coding_genes.gff](../input_files/protien_coding_genes.gff))
1. Calculate the number of genes in the file.
2. What is the average gene length?
3. Use the exon feature types and the parent information in column 9 to calculate the average number of exons per transcript. 
4. Stretch goal: Use the GFF3 file to reconstruct the CDS of a gene and translate it into amino acids.
