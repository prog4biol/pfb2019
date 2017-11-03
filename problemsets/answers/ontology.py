#!/usr/bin/env python3

import sys
import pronto

GO_GENES = sys.argv[1]
MY_GO_TERM = sys.argv[2]

ont = pronto.Ontology('/Users/smr/Desktop/PFB2017/pfb2017/files/go.owl')

term = ont[MY_GO_TERM]

print("Searching for children of" , term)

all_children={}
all_children[MY_GO_TERM] = term
for child in ont[MY_GO_TERM].rchildren():
  all_children[child.id] = child.name


genes = {}

file = open(GO_GENES , "r")
for line in file:
  line = line.rstrip()
  #print(line)
  columns = line.split("\t")
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
