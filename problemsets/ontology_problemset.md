# Ontology Problem set

In this exercise you will generate a gene list, get the GO annotations, and search though the genes for those that have been annotated with a GO term of interest. An issue you must address is that many GO terms have children terms, and the children may have children. Often you want all the genes annotoated with the parent as well as it's child terms.



1. Download [go.owl](http://purl.obolibrary.org/obo/go.owl). Or `git pull` from srobb1/pfb2017. go.owl will be in the files directory
2. `pip install six` a required module
3. `pip install pronto` an ontology parsing module
4. Look over the [documentation](https://github.com/althonos/pronto) for usage of the pronoto module. It is linked [here](https://github.com/althonos/pronto)
5. Write a script that
   1. Create an object of type 'Ontology' with the gene ontology owl file. You can download with wget or curl at this address: `http://purl.obolibrary.org/obo/go.owl` or you can `git pull` to update your course repositfrom the 
       `ont = pronto.Ontology('/Users/smr/Desktop/PFB2017/pfb2017/files/go.owl')`
   2
