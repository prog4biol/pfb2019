#!/usr/bin/env python3

# Python 6 - IO - Problem Set
# ===================


# 6. You are going to generate a couple of gene list that are saved in files, add their contents to sets, and compare them. 

# __Generate Gene Lists:__


# _Get all genes:_

# 1. Go to [Ensembl Biomart](http://useast.ensembl.org/biomart/martview/4b8fb1941e75e7763e8c4ccf1ffcd9c5).
# 2. In dropdown box, select "Ensembl Genes 98"  (or most current version)
# 3. In dropdown box, select "Alpaca Genes" 
# 4. On the left, click Attributes
# 5. Expand GENE:
# 6. Deselect "transcript stable ID".
# 7. Click Results (top left)
# 8. Export all results to "File" "TSV" --> GO
# 9. Rename the file to "alpaca_all_genes.tsv"

# _In the same Ensembl window, follow the steps below to get genes that have been labeled with Gene Ontology term "stem cell proliferation". For extra information on stem cell proliferation, check out  [stem cell proliferation](http://purl.obolibrary.org/obo/GO_0072089)_

# 10. Click "Filters"
# 11. Under "Gene Ontology", check "Go term name" and enter "stem cell proliferation"
# 12. Click Results (top left)
# 13. Export all results to "File" "TSV" --> GO
# 14. Rename the file to "alpaca_stemcellproliferation_genes.tsv"

# _In the same Ensembl window, follow the steps below to get genes that have been labeled with Gene Ontology term "pigmentation". For extra information on pigmentation, check out [pigmentation](http://purl.obolibrary.org/obo/GO_0043473)_


# 15. Click "Filters"
# 16. Under "Gene Ontology", check "Go term name" and enter "pigmentation"
# 17. Click Results (top left)
# 18. Export all results to "File" "TSV" --> GO
# 19. Rename the file to "alpaca_pigmentation_genes.tsv"


# __Open each of the three files and add the geneIDs to a Set. One Set per file.__




alpaca_genes_f = open('alpaca_all_genes.tsv', 'r')

alpaca_genes = set()

header_line = 0
for line in alpaca_genes_f:
    if header_line == 0:
        header_line +=1
        pass
    else:
        gene = line.rstrip().split("\t")[0]
        alpaca_genes.add(gene)

alpaca_p_genes_f = open('alpaca_pigmentation_genes.tsv', 'r')

alpaca_p_genes = set()

header_line = 0
for line in alpaca_p_genes_f:
    if header_line == 0:
        header_line +=1
        pass
    else:
        gene = line.rstrip().split("\t")[0]
        alpaca_p_genes.add(gene)

alpaca_sc_genes_f = open('alpaca_stemcellproliferation_genes.tsv', 'r')
alpaca_sc_genes = set()

header_line = 0
for line in alpaca_sc_genes_f:
    if header_line == 0:
        header_line +=1
        pass
    else:
        gene = line.rstrip().split("\t")[0]
        alpaca_sc_genes.add(gene)


# A. Find all the genes that are not cell proliferation genes.

print(len(alpaca_genes - alpaca_sc_genes))


# B. Find all genes that are both stem cell proliferation genes and pigment genes.  
# *Note* Make sure to NOT add the header to your set.  
print('Genes that are both stem cell proliferation and pigmentation:')
print(alpaca_sc_genes & alpaca_p_genes)



# __Now, let do it again with transciption factors.__
 
# 1. Go back to your Ensembl Biomart window
# 2. Deselect the "GO Term Name"
# 3. Select "GO Term Accession"
# 4. Enter these two accessions IDs which in most organisms will be all the transcription factors
#    - GO:0006355 is "regulation of transcription, DNA-dependent”. 
#    - GO:0003677 is "DNA binding"
# 5.  Click Results (top left)
# 6. Export all results to "File" "TSV" --> GO
# 7. Rename the file to "alpaca_transcriptionFactors.tsv"

# __Open these two files: 1) the transcription factor gene list file and 2) the cell proliferation gene list file. Add each to a Set, One Set per file__


alpaca_tf_genes_f = open('alpaca_transcriptionFactors.tsv', 'r')
alpaca_tf_genes = set()

header_line = 0
for line in alpaca_tf_genes_f:
    if header_line == 0:
        header_line +=1
        pass
    else:
        gene = line.rstrip().split("\t")[0]
        alpaca_tf_genes.add(gene)

        

# A. Find all the genes that are transcription factors for cell proliferation

print('Genes that are transcription factors for cell proliferations:')
print(alpaca_sc_genes & alpaca_tf_genes)
print(len(alpaca_sc_genes & alpaca_tf_genes))

# __Now do the same on the command line with `comm` command. You might need to `sort` each file first.__

## firt pull out the first column of the file and sort it for both files
#cut -f 1 alpaca_stemcellproliferation_genes.tsv | sort >alpaca_stemcellproliferation_genes.sorted.tsv
#cut -f 1 alpaca_transcriptionFactors.tsv | sort >alpaca_transcriptionFactors.sorted.tsv

## take the common elements from each file
#comm -12 alpaca_transcriptionFactors.sorted.tsv alpaca_stemcellproliferation_genes.sorted.tsv
#comm -12 alpaca_transcriptionFactors.sorted.tsv alpaca_stemcellproliferation_genes.sorted.tsv | wc -l


