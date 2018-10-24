# Estimating Gene Expression Levels

Write a python program that reads in the 'bowtie2.sam' file and generates a table containing the number of reads mapped to each gene.

For example:

    gene_read_counter.py bowtie2.sam

would return:

    CG14995 1654
    S-Lap3  1598
    Eno     1415
    sqd     866
    AdipoR  792
    Est-6   780
    Cnx99A  777
    eff     770
    CG31948 709
    eIF5B   671
    Aldh-III        634
    CG6424  604
    Calx    542
    ...





# About the data:

The alignments are stored in a 'bam' file - the binary equivalent of the 'sam' file format.  The format of the alignments are like so, showing the first few rows:

    25_1_17589_1126_120	83	AdipoR^FBtr0084283	536	1	101M	=	517	-120	GGCGCATTGGCACACAATGCCGCCGAGCAGGCGGAGGAGTTTGTGCGCAAGGTCTGGGAGGCTAGCTGGAAAGTGTGCCACTACAAAAATCTACCCAAGTG	EGJJHHIIHFFFFFHJJJIGIJJJJJJJIGFFFCIHB>@2DDEFFFF@DDBDBCC>@HHHHHHGHFFFFDDDDCDDDDDDFFHG@7FFBCCDDDB<FFD@B	AS:i:-5	XS:i:-5	XN:i:0	XM:i:1	XO:i:0	XG:i:0	NM:i:1	MD:Z:32A68	YS:i:-5	YT:Z:CP
    25_1_17589_1126_120	163	AdipoR^FBtr0084283	517	1	101M	=	536	120	CTCCGATGAAATTGATTTGGGCGCATTGGCACACAATGCCGCCGAGCAGGCAGAGGAGTTTGTGCGCAAGGTCTAGGAGGCTAGCTGGAAAGTGTGCCACT	CA?@@;@FFHHHIHIJJJIIHHHHJJJJJJJJJJJJJJJJC?6.(<92++9ABCHHIJIGIIJJIJJJJJJIIGGIJJJJJJJJJJJJJIJJIIIIJJJJJ	AS:i:-5	XS:i:-5	XN:i:0	XM:i:1	XO:i:0	XG:i:0	NM:i:1	MD:Z:74G26	YS:i:-5	YT:Z:CP
    25_1_17589_1126_120	339	AdipoR^FBtr0308848	649	1	101M	=	630	-120	GGCGCATTGGCACACAATGCCGCCGAGCAGGCGGAGGAGTTTGTGCGCAAGGTCTGGGAGGCTAGCTGGAAAGTGTGCCACTACAAAAATCTACCCAAGTG	EGJJHHIIHFFFFFHJJJIGIJJJJJJJIGFFFCIHB>@2DDEFFFF@DDBDBCC>@HHHHHHGHFFFFDDDDCDDDDDDFFHG@7FFBCCDDDB<FFD@B	AS:i:-5	XS:i:-5	XN:i:0	XM:i:1	XO:i:0	XG:i:0	NM:i:1	MD:Z:32A68	YS:i:-5	YT:Z:CP

The first field is the read name (ex. 25_1_17589_1126_120) and the second field is the name of the transcript sequence that read aligned to (ex. AdipoR^FBtr0084283).

For these data, the transcript identifiers include the gene identifier as a prefix.  So, the transcript AdipoR^FBtr0084283 corresponds to gene AdipoR.

>Note that a read that aligns to a region of shared sequence among multiple splicing isoforms for a gene will end up mapping to each of those isoforms (ie. multiply mapped).  If we are going to count reads mapping to genes, we'll want to count each read-to-gene mapping only once.


# Implementation options:

You'll need to uncompress the gzipped sam file in order to more easily read the data in your program. Youc an do this directly using gunzip:

    gunzip bowtie2.sam.gz

and then parse that tab-delimited text file.





