# Ontology Problem set

In this exercise you will generate a gene list, get the GO annotations, and search through the genes for those that have been annotated with a GO term of interest. An issue you must address is that many GO terms have children terms, and the children may have children. Often you want all the genes annotated with the parent as well as it's child terms.

1. Install the necessary modules
   1. `pip install six` a required module
   2. `pip install pronto` an ontology parsing module
2. Look over the [documentation](https://github.com/althonos/pronto) for usage of the pronto module. It is linked [here](https://github.com/althonos/pronto)
3. Write a script that does the following:
   1. Creates an object of class type 'Ontology' with the gene ontology owl file. 
      - Download the go.owl with wget or curl at this address: <http://purl.obolibrary.org/obo/go.owl>
       -  Create your obj: `ont = pronto.Ontology('/Users/smr/Desktop/PFB2017/pfb2017/files/go.owl')` 
   2. Get the term name for a specific Gene ontology accession., i.e., GO:0006355 (regulation of transcription, DNA-templated)
       `term_obj = ont['REF:ACCESSION']`
       `term_name = term_obj.name`
   3. Use pronto `rchildren()` to retrieve all children terms of your term and to store the ID of each term in a dictionary with the term name as the value
     1. make sure to use the `id` method to retrieve the id of each term object that is returned by `rchildren()`
         ```
         all_children={}
         for child in ont['REF:ACCESSION'].rchildren():
            all_children[child.id] = child.name
         ```
         Add the parent term as well
         ```
         all_children['REF:ACCESSION'] = term_name
         ```
   4. Opens a file generated from biomart with these columns (or use <https://github.com/srobb1/pfb2017/raw/master/files/cow_genes_umd3.1_withGO.txt> )
        - Gene or transcript ID
        - GO TERM ID
        - GO TERM Name
   5. Checks to see if each gene's GO TERM is the provided parent GO TERM ID or one of its children.
   
   
   
   __extra credit__
   Have your script take a series of terms. For example, if you really want all transcription factor annotations you should really use GO:0006355 "regulation of transcription, DNA-templated" and GO:0003677 “DNA binding”.  
   
   
If you like, this is a start to your script   
   
```
#!/usr/bin/env python3

import sys
import pronto

GO_GENES = sys.argv[1] # this is your gene list (gene_id\tgo_id\tgo_name)
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

```
