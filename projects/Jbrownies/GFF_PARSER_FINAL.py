#!/usr/bin/env python3

#############
# JBrownies
# script name: NG_gffparser_lengths_per_exon.py
# goal: parse gff3 file, retrieve feature information 
# input files and extensions: Aspergillus nidulans .gff3 file
# status: finished!
#############

import sys
import re

### Part1 - Data structure 
## strategy: dict - mrna - gff_type - feature id
# this will allow us to retrieve detailed info per gene

gff_file = open(sys.argv[1], 'r')

dict_mrna_exon_ids = {}

for line in gff_file:
        if line.startswith('#'):
                continue
        else:
                columns = line.rstrip().split('\t')
                #print(columns)
                if columns[2] == 'exon' or columns[2] == 'five_prime_UTR' or columns[2] == 'three_prime_UTR':
                        match = re.search(r"ID=(\w+);.*?Parent=(\w+)", columns[8])
                        featureid = match.group(1)
                        mrnaid = match.group(2)
                        gff_type = columns[2]
                        #print(exonid)
                        #print(mrnaid)
                        if not mrnaid in dict_mrna_exon_ids:
                                dict_mrna_exon_ids[mrnaid]={} # creating dict for mrna 
                                if not gff_type in dict_mrna_exon_ids[mrnaid]: # asking if our targets in mrna {}
                                        dict_mrna_exon_ids[mrnaid][gff_type]=[]      # if not seen it, create [] to hold them
                                        dict_mrna_exon_ids[mrnaid][gff_type].append(featureid) # put target on []
                                else:
                                        dict_mrna_exon_ids[mrnaid][gff_type].append(featureid) # if seen targets before in {}, add to []
                        elif gff_type in dict_mrna_exon_ids[mrnaid]: # if mrna in {} and gfftype in {}
                                dict_mrna_exon_ids[mrnaid][gff_type].append(featureid) # add the featureid (= matches) to []
                        else: 
                                dict_mrna_exon_ids[mrnaid][gff_type]=[]
                                dict_mrna_exon_ids[mrnaid][gff_type].append(featureid)


### Part2 - Report of features per gene

total_numb_exon = 0
total_numb_genes = 0
numb_genes_5utr = 0
numb_genes_3utr =0

#print("Features per gene")
for k in dict_mrna_exon_ids:
        #print(k)
        total_numb_exon += len(dict_mrna_exon_ids[k]['exon'])
        total_numb_genes += 1        
        for key2 in dict_mrna_exon_ids[k]:
                #print('  ',key2,'\t',len(dict_mrna_exon_ids[k][key2]))
                #print(key2)
                if key2 == 'five_prime_UTR':
                        numb_genes_5utr +=1       
                if key2 == 'three_prime_UTR':
                        numb_genes_3utr +=1

                        
### Part3 - Length of exons

gff_file = open(sys.argv[1], 'r')

length_exons = 0

for line in gff_file:
        if line.startswith('#'):
                continue
        else:
                columns = line.rstrip().split('\t')
                #print(columns)
                if columns[2] == 'exon':
                        begin_frame = int(columns[3])
                        end_frame = int(columns[4])
                        length_exons += ((end_frame+1) - begin_frame)                        
#print(length_exons)
#print(length_exons/total_numb_genes)


### Part4 - Totals 

gff_file = open(sys.argv[1], 'r')

gene_dict = {}
other_dict = {}

for line in gff_file:
        if line.startswith('#'):
                continue
        else:
                columns = line.rstrip().split('\t')
                if not columns[2] in other_dict:
                        other_dict[columns[2]] =1
                else:
                        other_dict[columns[2]] +=1
                if columns[2] == 'gene':
                        if not "total_genes" in gene_dict:
                                gene_dict["total_genes"] =1
                        else:
                                gene_dict["total_genes"] +=1
                                
                elif columns[2] == 'exon':
                        if not "total_exons" in gene_dict:
                                gene_dict["total_exons"] =1
                        else:
                                gene_dict["total_exons"] +=1
                                
                elif columns[2] == 'mRNA':
                        if not "total_mRNA" in gene_dict:
                                gene_dict["total_mRNA"] =1
                        else:
                                gene_dict["total_mRNA"] +=1


### Part5 - Gene features per chromosome

gff_file = open(sys.argv[1], 'r')

chromo_dict = {}

for line in gff_file:
        if line.startswith('#'):
                continue
        else:
                columns = line.rstrip().split('\t')
                match = re.search(r"Chr[A-Z]+", columns[0])
                #print(match.group(0))
                chrm_name = match.group(0)
                #print(chrm_name)
                if not chrm_name in chromo_dict:
                        gcounter =1
                        mcounter =0
                        exoncounter =0
                        threeprimeutr =0
                        fiveprimeutr =0
                        my_counts = [gcounter,mcounter,exoncounter,threeprimeutr,fiveprimeutr]
                        chromo_dict[chrm_name] = my_counts
                else:
                        #print('else')
                        if columns[2] == 'gene':
                                gcounter += 1
                        if columns[2] == 'mRNA':
                                mcounter += 1
                        if columns[2] == 'exon':
                                exoncounter += 1
                        if columns[2] == 'three_prime_UTR':
                                threeprimeutr +=1
                        if columns[2] == 'five_prime_UTR':
                                fiveprimeutr +=1
                        chromo_dict[chrm_name] = [gcounter,mcounter,exoncounter,threeprimeutr,fiveprimeutr]
                        #print(chrm_name)


### Part6 - Average gene length

gff_file = open(sys.argv[1], 'r')

length_genes = 0

for line in gff_file:
        if line.startswith('#'):
                continue
        else:
                columns = line.rstrip().split('\t')
                #print(columns)
                if columns[2] == 'gene':
                        begin_frame = int(columns[3])
                        end_frame = int(columns[4])
                        length_genes += (end_frame+1)-begin_frame
#print(length_exons)
#print(length_exons/total_numb_genes) 


### Part7 - Average length of introns


gff_file = open(sys.argv[1], 'r')

dict_exon_lengths = {}

for line in gff_file:
        if line.startswith('#'):
                continue
        else:
                columns = line.rstrip().split('\t')
                #print(columns)
                if columns[2] == 'exon':
                        match = re.search(r"ID=(\w+);.*?Parent=(\w+)", columns[8])
                        mrnaid = match.group(2)
                        gff_type = columns[2]
                        start_exon = int(columns[3])
                        end_exon = int(columns[4])
                        #print(mrnaid)
                        #print(gff_type)
                        #print(start_exon)
                        #print(end_exon)
                        if not mrnaid in dict_exon_lengths:
                                dict_exon_lengths[mrnaid]={} # creating dict for mrna
                                if not gff_type in dict_exon_lengths[mrnaid]: # asking if our targets in mrna {}
                                        dict_exon_lengths[mrnaid][gff_type]=[]      # if not seen it, create [] to hold them
                                        dict_exon_lengths[mrnaid][gff_type].append(start_exon) # put target on []
                                        dict_exon_lengths[mrnaid][gff_type].append(end_exon)
                                else:
                                        dict_exon_lengths[mrnaid][gff_type].append(start_exon) # if seen targets before in {}, add to []
                                        dict_exon_lengths[mrnaid][gff_type].append(end_exon)
                        elif gff_type in dict_exon_lengths[mrnaid]: # if mrna in {} and gfftype in {}
                                dict_exon_lengths[mrnaid][gff_type].append(start_exon) # add the featureid (= matches) to []
                                dict_exon_lengths[mrnaid][gff_type].append(end_exon)
                        else:
                                dict_exon_lengths[mrnaid][gff_type]=[]
                                dict_exon_lengths[mrnaid][gff_type].append(start_exon)
                                dict_exon_lengths[mrnaid][gff_type].append(end_exon)

#print(dict_exon_lengths)

numb_introns =0
length_introns =0

for key in dict_exon_lengths:
        #print(key)
        for key2 in dict_exon_lengths[key]:
                #print(key,'\n',key2,'\t')
                exon_coordinates = dict_exon_lengths[key][key2]
                #print(exon_coordinates)
                intron_coordinates = exon_coordinates[1:-1]
                intron_coordinates = sorted(intron_coordinates, key=None, reverse=False)
                #print(intron_coordinates)
                for index in range(0,len(intron_coordinates),2):
                        b,e = intron_coordinates[index:index+2]                        
                        length_introns += e-b -1 #why -1? Bc of the coordinates of the introns just outside the exons
                        numb_introns +=1
#print(length_introns)
#print(numb_introns)

                
######### PRINTING REPORT OF GFF FILE FEATURES

# genes:
print("Total genes:",gene_dict['total_genes'])

# mRNA
print("Total mRNA:", gene_dict['total_mRNA'])

# genes/chromosome:
print("Chromosome metrics:")
for k in chromo_dict:
        print("  ",k)
        print('     ',"Total number of genes:",chromo_dict[k][0])
        print('     ',"Total number of mRNA:",chromo_dict[k][1])
        print('     ',"Total number of exons:",chromo_dict[k][2])
        print('     ',"Total number of 3' UTR:",chromo_dict[k][3])
        print('     ',"Total number of 4' UTR:",chromo_dict[k][4])
        
# avg gene_length:
gene_length_total = length_genes/total_numb_genes
print("Average length of genes:","{:.1f}".format(gene_length_total)," bp")

# exons/gene:
average_exons_gene = total_numb_exon/total_numb_genes
print("Average number of exons per gene:","{:.1f}".format(average_exons_gene))

# avg spliced transcript length:
exon_length_total = length_exons/total_numb_genes
print("Average length of spliced transcripts:","{:.1f}".format(exon_length_total)," bp")

# avg exon_length:
avg_exon_length = length_exons/total_numb_exon
print("Average length of exons:","{:.1f}".format(avg_exon_length)," bp")

# avg intro_length
print("Average length of introns:","{:.1f}".format(length_introns/numb_introns)," bp")

# % genes with 5' and 3' UTRs:
#print("Number of genes with 5' UTR:",numb_genes_5utr)
#print("Number of genes with 3' UTR:",numb_genes_3utr)
print("Percent of genes with 5' UTR:","{:.1%}".format(numb_genes_5utr/total_numb_genes))
print("Percent of genes with 3' UTR:","{:.1%}".format(numb_genes_5utr/total_numb_genes))

