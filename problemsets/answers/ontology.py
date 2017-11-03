#!/usr/bin/env python3

import sys
import pronto

GO_GENES = sys.argv[1] # this is a file with your gene list with this format: gene_id\tgo_id\tgo_name
MY_GO_ID = sys.argv[2] # this is the GO term you want to search for in your gene list

# create an object of class Ontology with the GO ontology
ont = pronto.Ontology('your/path2/pfb2017/files/go.owl')

# get the term name of the provided GO ID
term_obj = ont[MY_GO_ID]
term_name = term_obj.name
print("These genes have all been annotated with" , MY_GO_ID + ', "' + term_name + '" or any of its child terms' )


# add the parent GO ID to dictionary of IDs to search for
all_children={}
all_children[MY_GO_ID] = term_name

# add all children of the parent term to dictionary
for child in ont[MY_GO_ID].rchildren():
  all_children[child.id] = child.name

# open genes file 
# look at each line
# if the go term is present in your parent/child dictionary
# add gene name and their annotated GO term ID to a dictionary
# print out all the genes their GO TERM ID and the GO TERM name for all matching genes

##### YOU DO THIS PART 
    
# save any gene that has a go term that is in the all_children dictionary
genes = {}

file = open(GO_GENES , "r")
for line in file:
  line = line.rstrip()
  #print(line)
  columns = line.split("\t")
  # not all the genes have go terms, so there could be blank columns, lets check for those by counting columns
  if len(columns) == 3:
    (gene_id , go_id, go_name) = columns
    #print(line)
    if go_id in all_children:
      genes[gene_id] = go_id  
  
     
# print out all the genes that are of the type you provided as well as any of its children
for gene in genes:
   go_id = genes[gene]
   go_id_obj = ont[go_id]
   go_name = go_id_obj.name
   print(gene, go_id, go_name, sep="\t")
