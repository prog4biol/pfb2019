# Counting k-mers

Write a python program 'kmer_counter.py' that takes command-line parameters:

* kmer_length
* filename.fastq
* num_top_kmers

The program should do the following:

* read in the fastq file 'filename.fastq'
* count kmers of size 'kmer_length'
* output a table of the 'num_top_kmers' kmers sorted by abundance, descendingly.


# example:

Using a kmer size of 8 and reporting the top 10 kmers and their counts:

    kmer_counter.py 8 reads.fq 10

.

    TTTTTTTT	1743
    AAAAAAAA	1204
    CCAGCCTT	666
    GAAGCTGG	627
    CAGGCAGG	549
    TTTGCTGT	536
    GCCTGCTG	533
    CTTGGTCT	525
    AAGCTGGA	518
    TTTTATTT	504



