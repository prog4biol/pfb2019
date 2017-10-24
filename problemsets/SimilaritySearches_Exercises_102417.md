
# Similarity Searching Workshop - Bill Pearson.  24 October 2017

## Morning Workshop
Exercises can be found <a href="http://fasta.bioch.virginia.edu/mol_evol" target="_blank">here</a>

http://fasta.bioch.virginia.edu/mol_evol


## Afternoon Workshop

This exercise can be found [here](http://fasta.bioch.virginia.edu/mol_evol/pfb_python_matrices.html):

http://fasta.bioch.virginia.edu/mol_evol/pfb_python_matrices.html

The goals of this exercise are to:

1. Do some simple parsing of BLAST tabular format output files to extract some information
2. Evaluate the accuracy of similarity statistics
3. Demonstrate to yourself that scoring matrices have different target identities and alignment lengths.

On the fasta.bioch.virginia.edu/mol_evol/dataare sets of results from either SSEARCH or BLASTP searching either 
a 200 or 800 amino acid random protein sequence against the QFO78 library of 78 Uniprot Reference Proteomes.

Your goal this afternoon will be to write a script that reads each of the sets of data from eitherthe SSEARCH or BLASTP outputs and produces a table with each of the scoring matrices as row, and the percent identity, alignment length, and E()-values for columns, for the top hit from each of the searches.

To do this, you will need to:

1. Download a set of SSEARCH of BLASTP results.

2. Write a program that will take take an argument from the command line, which you can use to specify either rand5-200or rand5-800, and concatenate it with a scoring matrix name (BL50, BP62, etc for SSEARCH, BLOSUM62, BLOSUM80for BLASTP, so that you can open and each result file and associate the results with a scoring matrix.

3. To parse the BLASTP tabular output file, you must:
  a. remove the newline character
  b. skip lines beginning with "#"
  c. use line.split('\t')to break each result line into its parts, which are:qseqid, sseqid, percid, alen, mismat, gaps, q_start, q_end, s_start, s_end, evalue, bits
  consider breaking the line up and saving the results to a dictionary with:
  this_data=dict(zip(field_names, line.split('\t')))
  d. As soon as you have a result line, save this_data, close the file, and move to the next result file.

4. Save the results in a dictionary using the matrix name as the key, and then print out the values you want ('percid', 'alen', and 'evalue').

5. Does the alignment length, percent identity, or evalue depend on the query sequence length?

6. Compare the SSEARCH results with the BLAST results. Which program gives a better range of alignment lengths and percent identities?
    Last modified: Mon Oct 23 2017 18:55:22 GMT-0400 (EDT)
