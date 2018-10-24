# CSHL Sequence Homology and Alignment Workshop
 
## Understanding Scoring Matrices
 
- Examine the PAM matrices at different levels:
- Compare PAM matrices [30](https://www.ncbi.nlm.nih.gov/IEB/ToolBox/C_DOC/lxr/source/data/PAM30),[70](https://www.ncbi.nlm.nih.gov/IEB/ToolBox/C_DOC/lxr/source/data/PAM70) and [250](https://www.ncbi.nlm.nih.gov/IEB/ToolBox/C_DOC/lxr/source/data/PAM250)

---
Questions:

1.	What is the highest score?
2.	What is the score for a W-W match?
3.	What is the score for a W-G mismatch?

## Identifying homologs and non-homologs; effects of scoring matrices and algorithms 

### Try Sequence Similarity Searching with FASTA 


- Go to the [FASTA SERVER](http://fasta.bioch.virginia.edu)
- Search the protein sequence Drosophila glutathione transferase (P20432) against the PIR1 Annotated protein sequence database: 
    - type the accession in the search box
    - choose accession on the drop drown for “Query Sequence”
- Take a look at the output. 

--- 

### Questions

1. How long is the query sequence? 
2. How many sequences are in the PIR1 database? 
3. What scoring matrix was used? 
4. What were the gap penalties? 
5. What are each of the numbers after the description of the library sequence? Which one is best for inferring homology? 
6. Looking at an alignment, where are the boundaries of the alignment (the best local region)? 
7. What is the highest scoring non-homolog? (The non-homolog with the highest alignment score, or the lowest E()-value.) How would you confirm that your candidate non-homolog was truly unrelated? 
8. Note that this drosophila glutathione transferase shares significant similarity with both sequences from bacteria (SSPA_EOC57) and mammals. How might you test whether the stringent starvation protein is homologous to glutathione transferases? (Hint - compare your candidate non-homolog with SwissProt for a more reliable test.) 
9. Compare the expectation (E()) value for the distant relationship between GSTT1_DROME and GSTM2_RAT (class-mu). How would you demonstrate that GSTT1_DROME is homologous to GSTM2_RAT? 
10. Examine how the expectation value changes with different scoring matrices (BLOSUM62, BlastP62, PAM250) and different gap penalties. (The default scoring matrix for the FASTA programs is BLOSUM50, with gap penalties of -10 to open a gap and -2 for each residue in the gap - e.g. -12 for a one residue gap). 
11. What happens to the E()-value for the 100% identical sequence with the different matrices and different gap penalties? 
12. What happens to the E()-value for distant homologs, like GSTA1_RAT with the different matrices and different gap penalties? 
13. What happens to the E()-value for the highest scoring unrelated sequence with the different matrices? 
14. Try the search ssearch (Smith-Waterman). Again, look at the E()-values for distant homologs and the highest scoring unrelated sequence. 

--- 

### Try Sequence Similarity Searching with BLAST
- Go to the [BLAST Server](http://blast.ncbi.nlm.nih.gov)
- Search the protein sequence Drosophila glutathione transferase (P20432) against the SwissProt protein sequence database.
- Take a look at the output (there is a link to other reports: Search Summary for some questions). 

--- 

### Questions

1.	How long is the query sequence? 
2.	How many sequences are in the Swissprot database? 
3.	What scoring matrix was used? 
4.	What were the gap penalties? 
5.	Looking at an alignment, where are the boundaries of the alignment (the best local region)? 
6.	What is the highest scoring non-homolog? 
7.	How do the blastp E(), alignment length and score compare with the FASTA SSPA_ECO57?

## Comparison of Protein:Protein, translated DNA:protein to DNA:DNA searches - more sensitive DNA searches
 
- Using [BLAST](http://blast.ncbi.nlm.nih.gov/): in the next three exercises, we will try to find gstt1_drome (P20432) homologs in the Arabidopsis genome using:
  - protein:protein (BLASTP)
  - DNA:protein (BLASTX)
  - protein:DNA (TBLASTN)
  - DNA:DNA (BLASTN) searches. 

*Hint exclude taxa by Arabidopisis*

--- 

### Questions

1. What are the E()-values for Arabidopsis THETA1, phi 12, zeta- class 1 and lambda 1 for:
    - Protein:Protein BLASTP with gstt1_drome (P20432) using the protein database RefSeq
    -  DNA:Protein BLASTX with GSTT1_DROME cDNA (gi 8033) using the protein database RefSeq
    - Protein:DNA TBLASTN: with GSTT1_DROME cDNA (gi 8033) using the Reference mRNA sequences refseq_rna
    - DNA:DNA BLASTN using (gi 8033) to the Reference mRNA sequences (refseq_rna)
2. Are there detectable Arabidopsis homologues? 
    -	What are the BLAST DNA match/mismatch penalties used for the BLASTN search? 
