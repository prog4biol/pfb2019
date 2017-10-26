
# Problem Set 8 pfb2017

#### 1. Take a mulit-FASTA Python_08.fasta file from user input and calculate the nucleotide composition for each sequence. 
* Use a datastructure to keep count. 
* Print out each sequence name and its compostion in this format: seqName\tA_count\tT_count\tG_count\C_count

Here is a handy way to store the information:
```
seqs[geneName][nucleotide]=count

seqs['geneA']['A'] = 2
seqs['geneA']['T'] = 3
seqs['geneA']['G'] = 3
seqs['geneA']['C'] = 1


seqs['geneB']['A'] = 1
seqs['geneB']['T'] = 5
seqs['geneB']['G'] = 2
seqs['geneB']['C'] = 2
```


```python
### initialize variables 
dict = {}
seq = ""
### open file
fh = open("/Users/xdo/Shell/pfb2017/Python_08_test.fasta", "r")

### read in file and store into dictionary key=header : value=sequence
for line in fh:
    line = line.strip()
    if line.startswith(">"):
        header = line.replace(">","" ).split()[0] # just grabes gene
    
        if header not in dict:
            dict[header]=seq
        seq = ""
    else:
        seq += line
        dict[header] = seq

### calculate the nt compsition and store into another dictionary
### make dictionary of nt comp
nested = {}
for k, v in dict.items():
    count_A = v.count("A")
    count_T = v.count("T") 
    count_G = v.count("G") 
    count_C = v.count("C") 
    nt_comp = {"A" : count_A, "T" : count_T, "G" : count_G, "C" : count_T}

    if k not in nested:
        #nested[k] = {"nt_comp": nt_comp, "len":len(v)} # this will look exactly like the notes dictionary
        nested[k] = nt_comp
print(nested)
for key in nested:
    print(key, nested[key]["A"], nested[key]["T"], nested[key]["G"], 
        nested[key]["T"], sep = "\t") # you can put strings on different lines in your code 

```

    {'c0_g1_i1': {'A': 360, 'T': 370, 'G': 206, 'C': 370}, 'c1_g1_i1': {'A': 149, 'T': 165, 'G': 88, 'C': 165}}
    c0_g1_i1	360	370	206	370
    c1_g1_i1	149	165	88	165


I got lazy and didn't want to type in another key, so I only made a dictionary in a dictionary. If you want to make a dictionary in a dictionary in a dictionary like Sofia's example in the notes, do the commented out #nested line instead. 

#### 2. Write a script that takes a multi-FASTA file Python_08.fasta from user input and breaks each sequence into codons (every three nucleotides is a codon) in just the first reading frame. Your output should look like this:
* seq1-frame-1-codons
* CAT GCT TGA GTC


```python
import sys
#to get file from user input
fh = open(sys.argv[1])

codon_dict ={}
outfh = open("Python_08.codons-frame-1.nt", "w")

for k, v in dict.items():
    #make a more descriptive id
    header = k+"frame-1-codons"
    
    #break into codons and add to codon_dict key=header, val=[codons]
    codon_dict[header] = [v[i:i+3] for i in range(0, len(v), 3)]
    
    #write to file
    outfh.write(header + "\n")
    outfh.write("\t".join(codon_dict[header]))
    outfh.write("\n")
    
    # print out to stdout
    print(header)
    print("\t".join(codon_dict[header]))
    
#close file
outfh.close()
```

    c0_g1_i1frame-1-codons
    GAA	CTC	CAA	AAA	TGA	AAA	CAT	AGT	AGC	AAT	CAA	AGC	ATC	CCA	CTA	TTT	TTT	GTC	TCT	CGT	TTC	ATT	AGC	GTT	GTA	AAT	TAC	TGA	TAC	CCT	ACT	ATA	CCT	CTA	CAA	GGC	CTT	TGT	CAT	CTT	TTT	ACT	CAA	GTG	TGA	AAT	CAT	CAC	TTA	TTG	TAT	GAA	GGA	TGA	GCT	TTC	CGT	TCG	CTA	GTT	TGC	TGA	AAA	GGC	CTT	CTG	CAA	TAA	GCT	CTC	TAT	TAT	CTT	TAA	AAA	AAC	CTG	GTT	CCT	GGT	CTT	CCA	TTC	TGC	TAA	AAG	CTG	TAG	GGG	TTT	TAT	CAC	GAG	ATT	CCC	GTT	GGC	ATT	CTG	ACT	TAT	TAA	AAA	TGC	TTA	CAG	AAG	AAA	TGG	ATT	CTT	TAA	ATG	GTC	AAA	TTA	ATA	CGT	GGA	CAG	ATA	ATA	ATC	CTT	TAT	TAG	ATG	AAA	TTA	CGA	AGC	CAT	ACA	GAA	AAT	CTT	CAA	CTC	GTT	TTT	TTC	ATC	CGC	TTC	TTG	TAC	TTC	TAA	TGT	CTA	GAG	CAT	CAG	TAA	ATG	GGG	ATC	CAC	CGA	GTC	AGC	AAC	TAT	TTC	AAA	GGT	ACA	AAC	AAC	TTG	CCC	GTG	TAA	CAG	AAT	TGA	TTC	ATG	CTG	CCA	ATA	TAA	TTC	ATA	TTA	ATA	TTG	GAG	AAG	AAC	AAA	GCA	ACG	AAC	AGA	TTA	AAC	TTG	CAA	CGT	TGG	TTG	GAG	ATT	ATT	TAC	TCG	GAA	AGG	CGT	CTG	TTG	ATT	TAG	CAC	ATT	TAG	AAA	ACA	ACG	CTA	TTA	CAG	AAA	TTA	TGG	CTT	CTG	TTA	TTG	CAA	ACT	TAG	TTG	AAG	GGC	ACT	TCG	GAA	GCC	GAC	AAA	ATG	GCT	CTG	TTG	GTT	TGT	CAA	ACG	AAC	GAA	CCA	TCC	TTC	TGC	AAT	CAG	CCT	TTA	TGC	CAG	CAA	AGG	CAT	GTT	TAT	GCG	CAA	GCA	TAT	TGA	ATA	ACT	CAT	CAC	AAT	ACA	TTA	ATG	ATG	CGT	GTT	TCA	ATT	ATG	GAA	AAT	TTC	TAG	GCT	TAT	CGC	TGC	AAC	TGG	CCC	ATA	AGC	CTG	TAT	CTC	CTG	ACG	CCC	AAG	TTT	TGC	AAA	AGA	ATA	ATG	ACA	TTT	TGA	AAA	CAT	ATG	TTG	AGA	ATG	CCA	AGA	GCT	CAT	TGT	CTG	TTT	TCC	CCG	ATA	TAG	AGG	CTA	AGC	AAG	CTC	TCA	TGG	AAA	TCG	CTA	ATA	GTG	TTT	CGA	AGT	AAT	CGA	CAG	GTA	TTG	TAT	CCT	GGA	TTA	ATA	TTA	GGG	TGG	CTC	ATG	CAT	GCT	CGT	GCA	ATC	GTA	ACA	AAT	ATG	TCT	TTC	TTT	TAC	GAA	TTT	TAA	CGC	TTC	AAT	ATA	AAT	CAT	ATT	TTT	CCT	CA
    c1_g1_i1frame-1-codons
    ACG	AAA	CGT	TGA	ATT	GAT	TTT	ATA	TCA	ATA	ATA	TCG	ATC	ATT	TTT	ATT	CTA	TTA	TTT	GTT	TGT	TTG	CTT	GGC	TTT	CAT	CTA	TTT	CTA	CAG	ACT	ATC	TTT	CCC	TAA	TGT	CTA	TTG	CAA	AAG	GAA	AAA	ATG	CAT	TGC	TTG	TTG	CCA	GCA	GTT	ATT	ATG	GCC	CAT	TTT	ATC	CAG	ATG	GTA	AAA	ACA	CTG	GAG	TCC	ATT	TTT	CAG	AGC	TTT	TAA	TCC	CTT	ACA	ATG	TTT	TCA	AAA	AAG	CAG	GTT	TTA	ACG	TGC	AAT	TCG	TTT	CAG	AAA	ATG	GCT	CTT	ACA	AAT	TTG	ACG	ATC	ATT	CCA	TTG	AGG	AGT	CAA	AAT	TAG	GGG	ACT	TTG	AAA	GAA	AAG	TAT	TTA	ATG	ATA	AAA	ACG	ACG	ATT	TTT	GGA	CTA	ATC	TTA	ACA	ATA	TGA	AAA	AGG	CTT	CGG	ACA	TAG	TTG	GAA	AAG	ACT	ATC	AGC	TTT	TAT	TTG	TGG	CAG	GTG	GGC	ATG	CTG	CGA	TGT	TTG	ACT	TAC	CCA	AAG	CCA	CGA	ATT	TAC	AGG	CGG


I iterated through the dictionary from Q1 using dictionary.iter() so I could set the value to v instead of having to type out dictionary[key] to get the value. 

#### 4. Now produce codons in the first three reading frames for each sequence and print out ids and sequence records for each frame and print to a file called 'Python_08.codons-3frames.nt'

For example:
```
seq1-frame-1-codons
ATG TTG
seq-frame-2-codons
TGT TGA
```


```python
codon_dict ={}
outfh = open("Python_08.codons-frame-3.nt", "w")

for k, v in dict.items():
    header1 = k+"-frame-1-codons"
    header2 = k+"-frame-2-codons"
    header3 = k+"-frame-3-codons"
    
    #get codons and make sure its 3 nt
    codon_dict[header1] = [v[i:i+3] for i in range(0, len(v), 3) if (len(v)- i) >= 3]
    codon_dict[header2] = [v[i:i+3] for i in range(1, len(v), 3) if (len(v)- i) >= 3]
    codon_dict[header3] = [v[i:i+3] for i in range(2, len(v), 3) if (len(v)- i) >= 3]

    #write to file
    outfh.write(header1 + "\n")
    outfh.write("\t".join(codon_dict[header1]))
    outfh.write("\n" + header2 + "\n")
    outfh.write("\t".join(codon_dict[header2]))
    outfh.write("\n" + header3 + "\n")
    outfh.write("\t".join(codon_dict[header3]))
    outfh.write("\n")
    
    #print to stdout
    print(header1)
    print("\t".join(codon_dict[header1]))
    print(header2)
    print("\t".join(codon_dict[header2]))
    print(header3)
    print("\t".join(codon_dict[header3]))
outfh.close()
```

    c0_g1_i1-frame-1-codons
    GAA	CTC	CAA	AAA	TGA	AAA	CAT	AGT	AGC	AAT	CAA	AGC	ATC	CCA	CTA	TTT	TTT	GTC	TCT	CGT	TTC	ATT	AGC	GTT	GTA	AAT	TAC	TGA	TAC	CCT	ACT	ATA	CCT	CTA	CAA	GGC	CTT	TGT	CAT	CTT	TTT	ACT	CAA	GTG	TGA	AAT	CAT	CAC	TTA	TTG	TAT	GAA	GGA	TGA	GCT	TTC	CGT	TCG	CTA	GTT	TGC	TGA	AAA	GGC	CTT	CTG	CAA	TAA	GCT	CTC	TAT	TAT	CTT	TAA	AAA	AAC	CTG	GTT	CCT	GGT	CTT	CCA	TTC	TGC	TAA	AAG	CTG	TAG	GGG	TTT	TAT	CAC	GAG	ATT	CCC	GTT	GGC	ATT	CTG	ACT	TAT	TAA	AAA	TGC	TTA	CAG	AAG	AAA	TGG	ATT	CTT	TAA	ATG	GTC	AAA	TTA	ATA	CGT	GGA	CAG	ATA	ATA	ATC	CTT	TAT	TAG	ATG	AAA	TTA	CGA	AGC	CAT	ACA	GAA	AAT	CTT	CAA	CTC	GTT	TTT	TTC	ATC	CGC	TTC	TTG	TAC	TTC	TAA	TGT	CTA	GAG	CAT	CAG	TAA	ATG	GGG	ATC	CAC	CGA	GTC	AGC	AAC	TAT	TTC	AAA	GGT	ACA	AAC	AAC	TTG	CCC	GTG	TAA	CAG	AAT	TGA	TTC	ATG	CTG	CCA	ATA	TAA	TTC	ATA	TTA	ATA	TTG	GAG	AAG	AAC	AAA	GCA	ACG	AAC	AGA	TTA	AAC	TTG	CAA	CGT	TGG	TTG	GAG	ATT	ATT	TAC	TCG	GAA	AGG	CGT	CTG	TTG	ATT	TAG	CAC	ATT	TAG	AAA	ACA	ACG	CTA	TTA	CAG	AAA	TTA	TGG	CTT	CTG	TTA	TTG	CAA	ACT	TAG	TTG	AAG	GGC	ACT	TCG	GAA	GCC	GAC	AAA	ATG	GCT	CTG	TTG	GTT	TGT	CAA	ACG	AAC	GAA	CCA	TCC	TTC	TGC	AAT	CAG	CCT	TTA	TGC	CAG	CAA	AGG	CAT	GTT	TAT	GCG	CAA	GCA	TAT	TGA	ATA	ACT	CAT	CAC	AAT	ACA	TTA	ATG	ATG	CGT	GTT	TCA	ATT	ATG	GAA	AAT	TTC	TAG	GCT	TAT	CGC	TGC	AAC	TGG	CCC	ATA	AGC	CTG	TAT	CTC	CTG	ACG	CCC	AAG	TTT	TGC	AAA	AGA	ATA	ATG	ACA	TTT	TGA	AAA	CAT	ATG	TTG	AGA	ATG	CCA	AGA	GCT	CAT	TGT	CTG	TTT	TCC	CCG	ATA	TAG	AGG	CTA	AGC	AAG	CTC	TCA	TGG	AAA	TCG	CTA	ATA	GTG	TTT	CGA	AGT	AAT	CGA	CAG	GTA	TTG	TAT	CCT	GGA	TTA	ATA	TTA	GGG	TGG	CTC	ATG	CAT	GCT	CGT	GCA	ATC	GTA	ACA	AAT	ATG	TCT	TTC	TTT	TAC	GAA	TTT	TAA	CGC	TTC	AAT	ATA	AAT	CAT	ATT	TTT	CCT
    c0_g1_i1-frame-2-codons
    AAC	TCC	AAA	AAT	GAA	AAC	ATA	GTA	GCA	ATC	AAA	GCA	TCC	CAC	TAT	TTT	TTG	TCT	CTC	GTT	TCA	TTA	GCG	TTG	TAA	ATT	ACT	GAT	ACC	CTA	CTA	TAC	CTC	TAC	AAG	GCC	TTT	GTC	ATC	TTT	TTA	CTC	AAG	TGT	GAA	ATC	ATC	ACT	TAT	TGT	ATG	AAG	GAT	GAG	CTT	TCC	GTT	CGC	TAG	TTT	GCT	GAA	AAG	GCC	TTC	TGC	AAT	AAG	CTC	TCT	ATT	ATC	TTT	AAA	AAA	ACC	TGG	TTC	CTG	GTC	TTC	CAT	TCT	GCT	AAA	AGC	TGT	AGG	GGT	TTT	ATC	ACG	AGA	TTC	CCG	TTG	GCA	TTC	TGA	CTT	ATT	AAA	AAT	GCT	TAC	AGA	AGA	AAT	GGA	TTC	TTT	AAA	TGG	TCA	AAT	TAA	TAC	GTG	GAC	AGA	TAA	TAA	TCC	TTT	ATT	AGA	TGA	AAT	TAC	GAA	GCC	ATA	CAG	AAA	ATC	TTC	AAC	TCG	TTT	TTT	TCA	TCC	GCT	TCT	TGT	ACT	TCT	AAT	GTC	TAG	AGC	ATC	AGT	AAA	TGG	GGA	TCC	ACC	GAG	TCA	GCA	ACT	ATT	TCA	AAG	GTA	CAA	ACA	ACT	TGC	CCG	TGT	AAC	AGA	ATT	GAT	TCA	TGC	TGC	CAA	TAT	AAT	TCA	TAT	TAA	TAT	TGG	AGA	AGA	ACA	AAG	CAA	CGA	ACA	GAT	TAA	ACT	TGC	AAC	GTT	GGT	TGG	AGA	TTA	TTT	ACT	CGG	AAA	GGC	GTC	TGT	TGA	TTT	AGC	ACA	TTT	AGA	AAA	CAA	CGC	TAT	TAC	AGA	AAT	TAT	GGC	TTC	TGT	TAT	TGC	AAA	CTT	AGT	TGA	AGG	GCA	CTT	CGG	AAG	CCG	ACA	AAA	TGG	CTC	TGT	TGG	TTT	GTC	AAA	CGA	ACG	AAC	CAT	CCT	TCT	GCA	ATC	AGC	CTT	TAT	GCC	AGC	AAA	GGC	ATG	TTT	ATG	CGC	AAG	CAT	ATT	GAA	TAA	CTC	ATC	ACA	ATA	CAT	TAA	TGA	TGC	GTG	TTT	CAA	TTA	TGG	AAA	ATT	TCT	AGG	CTT	ATC	GCT	GCA	ACT	GGC	CCA	TAA	GCC	TGT	ATC	TCC	TGA	CGC	CCA	AGT	TTT	GCA	AAA	GAA	TAA	TGA	CAT	TTT	GAA	AAC	ATA	TGT	TGA	GAA	TGC	CAA	GAG	CTC	ATT	GTC	TGT	TTT	CCC	CGA	TAT	AGA	GGC	TAA	GCA	AGC	TCT	CAT	GGA	AAT	CGC	TAA	TAG	TGT	TTC	GAA	GTA	ATC	GAC	AGG	TAT	TGT	ATC	CTG	GAT	TAA	TAT	TAG	GGT	GGC	TCA	TGC	ATG	CTC	GTG	CAA	TCG	TAA	CAA	ATA	TGT	CTT	TCT	TTT	ACG	AAT	TTT	AAC	GCT	TCA	ATA	TAA	ATC	ATA	TTT	TTC	CTC
    c0_g1_i1-frame-3-codons
    ACT	CCA	AAA	ATG	AAA	ACA	TAG	TAG	CAA	TCA	AAG	CAT	CCC	ACT	ATT	TTT	TGT	CTC	TCG	TTT	CAT	TAG	CGT	TGT	AAA	TTA	CTG	ATA	CCC	TAC	TAT	ACC	TCT	ACA	AGG	CCT	TTG	TCA	TCT	TTT	TAC	TCA	AGT	GTG	AAA	TCA	TCA	CTT	ATT	GTA	TGA	AGG	ATG	AGC	TTT	CCG	TTC	GCT	AGT	TTG	CTG	AAA	AGG	CCT	TCT	GCA	ATA	AGC	TCT	CTA	TTA	TCT	TTA	AAA	AAA	CCT	GGT	TCC	TGG	TCT	TCC	ATT	CTG	CTA	AAA	GCT	GTA	GGG	GTT	TTA	TCA	CGA	GAT	TCC	CGT	TGG	CAT	TCT	GAC	TTA	TTA	AAA	ATG	CTT	ACA	GAA	GAA	ATG	GAT	TCT	TTA	AAT	GGT	CAA	ATT	AAT	ACG	TGG	ACA	GAT	AAT	AAT	CCT	TTA	TTA	GAT	GAA	ATT	ACG	AAG	CCA	TAC	AGA	AAA	TCT	TCA	ACT	CGT	TTT	TTT	CAT	CCG	CTT	CTT	GTA	CTT	CTA	ATG	TCT	AGA	GCA	TCA	GTA	AAT	GGG	GAT	CCA	CCG	AGT	CAG	CAA	CTA	TTT	CAA	AGG	TAC	AAA	CAA	CTT	GCC	CGT	GTA	ACA	GAA	TTG	ATT	CAT	GCT	GCC	AAT	ATA	ATT	CAT	ATT	AAT	ATT	GGA	GAA	GAA	CAA	AGC	AAC	GAA	CAG	ATT	AAA	CTT	GCA	ACG	TTG	GTT	GGA	GAT	TAT	TTA	CTC	GGA	AAG	GCG	TCT	GTT	GAT	TTA	GCA	CAT	TTA	GAA	AAC	AAC	GCT	ATT	ACA	GAA	ATT	ATG	GCT	TCT	GTT	ATT	GCA	AAC	TTA	GTT	GAA	GGG	CAC	TTC	GGA	AGC	CGA	CAA	AAT	GGC	TCT	GTT	GGT	TTG	TCA	AAC	GAA	CGA	ACC	ATC	CTT	CTG	CAA	TCA	GCC	TTT	ATG	CCA	GCA	AAG	GCA	TGT	TTA	TGC	GCA	AGC	ATA	TTG	AAT	AAC	TCA	TCA	CAA	TAC	ATT	AAT	GAT	GCG	TGT	TTC	AAT	TAT	GGA	AAA	TTT	CTA	GGC	TTA	TCG	CTG	CAA	CTG	GCC	CAT	AAG	CCT	GTA	TCT	CCT	GAC	GCC	CAA	GTT	TTG	CAA	AAG	AAT	AAT	GAC	ATT	TTG	AAA	ACA	TAT	GTT	GAG	AAT	GCC	AAG	AGC	TCA	TTG	TCT	GTT	TTC	CCC	GAT	ATA	GAG	GCT	AAG	CAA	GCT	CTC	ATG	GAA	ATC	GCT	AAT	AGT	GTT	TCG	AAG	TAA	TCG	ACA	GGT	ATT	GTA	TCC	TGG	ATT	AAT	ATT	AGG	GTG	GCT	CAT	GCA	TGC	TCG	TGC	AAT	CGT	AAC	AAA	TAT	GTC	TTT	CTT	TTA	CGA	ATT	TTA	ACG	CTT	CAA	TAT	AAA	TCA	TAT	TTT	TCC	TCA
    c1_g1_i1-frame-1-codons
    ACG	AAA	CGT	TGA	ATT	GAT	TTT	ATA	TCA	ATA	ATA	TCG	ATC	ATT	TTT	ATT	CTA	TTA	TTT	GTT	TGT	TTG	CTT	GGC	TTT	CAT	CTA	TTT	CTA	CAG	ACT	ATC	TTT	CCC	TAA	TGT	CTA	TTG	CAA	AAG	GAA	AAA	ATG	CAT	TGC	TTG	TTG	CCA	GCA	GTT	ATT	ATG	GCC	CAT	TTT	ATC	CAG	ATG	GTA	AAA	ACA	CTG	GAG	TCC	ATT	TTT	CAG	AGC	TTT	TAA	TCC	CTT	ACA	ATG	TTT	TCA	AAA	AAG	CAG	GTT	TTA	ACG	TGC	AAT	TCG	TTT	CAG	AAA	ATG	GCT	CTT	ACA	AAT	TTG	ACG	ATC	ATT	CCA	TTG	AGG	AGT	CAA	AAT	TAG	GGG	ACT	TTG	AAA	GAA	AAG	TAT	TTA	ATG	ATA	AAA	ACG	ACG	ATT	TTT	GGA	CTA	ATC	TTA	ACA	ATA	TGA	AAA	AGG	CTT	CGG	ACA	TAG	TTG	GAA	AAG	ACT	ATC	AGC	TTT	TAT	TTG	TGG	CAG	GTG	GGC	ATG	CTG	CGA	TGT	TTG	ACT	TAC	CCA	AAG	CCA	CGA	ATT	TAC	AGG	CGG
    c1_g1_i1-frame-2-codons
    CGA	AAC	GTT	GAA	TTG	ATT	TTA	TAT	CAA	TAA	TAT	CGA	TCA	TTT	TTA	TTC	TAT	TAT	TTG	TTT	GTT	TGC	TTG	GCT	TTC	ATC	TAT	TTC	TAC	AGA	CTA	TCT	TTC	CCT	AAT	GTC	TAT	TGC	AAA	AGG	AAA	AAA	TGC	ATT	GCT	TGT	TGC	CAG	CAG	TTA	TTA	TGG	CCC	ATT	TTA	TCC	AGA	TGG	TAA	AAA	CAC	TGG	AGT	CCA	TTT	TTC	AGA	GCT	TTT	AAT	CCC	TTA	CAA	TGT	TTT	CAA	AAA	AGC	AGG	TTT	TAA	CGT	GCA	ATT	CGT	TTC	AGA	AAA	TGG	CTC	TTA	CAA	ATT	TGA	CGA	TCA	TTC	CAT	TGA	GGA	GTC	AAA	ATT	AGG	GGA	CTT	TGA	AAG	AAA	AGT	ATT	TAA	TGA	TAA	AAA	CGA	CGA	TTT	TTG	GAC	TAA	TCT	TAA	CAA	TAT	GAA	AAA	GGC	TTC	GGA	CAT	AGT	TGG	AAA	AGA	CTA	TCA	GCT	TTT	ATT	TGT	GGC	AGG	TGG	GCA	TGC	TGC	GAT	GTT	TGA	CTT	ACC	CAA	AGC	CAC	GAA	TTT	ACA	GGC
    c1_g1_i1-frame-3-codons
    GAA	ACG	TTG	AAT	TGA	TTT	TAT	ATC	AAT	AAT	ATC	GAT	CAT	TTT	TAT	TCT	ATT	ATT	TGT	TTG	TTT	GCT	TGG	CTT	TCA	TCT	ATT	TCT	ACA	GAC	TAT	CTT	TCC	CTA	ATG	TCT	ATT	GCA	AAA	GGA	AAA	AAT	GCA	TTG	CTT	GTT	GCC	AGC	AGT	TAT	TAT	GGC	CCA	TTT	TAT	CCA	GAT	GGT	AAA	AAC	ACT	GGA	GTC	CAT	TTT	TCA	GAG	CTT	TTA	ATC	CCT	TAC	AAT	GTT	TTC	AAA	AAA	GCA	GGT	TTT	AAC	GTG	CAA	TTC	GTT	TCA	GAA	AAT	GGC	TCT	TAC	AAA	TTT	GAC	GAT	CAT	TCC	ATT	GAG	GAG	TCA	AAA	TTA	GGG	GAC	TTT	GAA	AGA	AAA	GTA	TTT	AAT	GAT	AAA	AAC	GAC	GAT	TTT	TGG	ACT	AAT	CTT	AAC	AAT	ATG	AAA	AAG	GCT	TCG	GAC	ATA	GTT	GGA	AAA	GAC	TAT	CAG	CTT	TTA	TTT	GTG	GCA	GGT	GGG	CAT	GCT	GCG	ATG	TTT	GAC	TTA	CCC	AAA	GCC	ACG	AAT	TTA	CAG	GCG


#### 5.Now reverse complement each sequence and print out all six reading frames to a file called 'Python_08.codons-6frames.nt'


```python
#initialize new dictionary that will be nested
fw_rev_dict = {}
for k, v in dict.items():
    reverse = v[::-1]
    fw_rev_dict[k] = {k+"_fw": v, k+"_rev":reverse}

fw_rev_codons= {}
outfh = open("Python_08.codons-frame-6.nt", "w")
for k, v in fw_rev_dict.items():

    fw1 = k+"_fw-frame-1-codons"
    fw2 = k+"_fw-frame-2-codons"
    fw3 = k+"_fw-frame-3-codons"

    fw_rev_codons[fw1] = [v[k+"_fw"][i:i+3] for i in range(0, len(v[k+"_fw"]), 3) if (len(v[k+"_fw"])- i) >= 3]
    fw_rev_codons[fw2] = [v[k+"_fw"][i:i+3] for i in range(1, len(v[k+"_fw"]), 3) if (len(v[k+"_fw"])- i) >= 3]
    fw_rev_codons[fw3] = [v[k+"_fw"][i:i+3] for i in range(2, len(v[k+"_fw"]), 3) if (len(v[k+"_fw"])- i) >= 3]

    rev1 = k+"_rev-frame-1-codons"
    rev2 = k+"_rev-frame-2-codons"
    rev3 = k+"_rev-frame-3-codons"

    fw_rev_codons[rev1] = [v[k+"_rev"][i:i+3] for i in range(0, len(v[k+"_fw"]), 3) if (len(v[k+"_fw"])- i) >= 3]
    fw_rev_codons[rev2] = [v[k+"_rev"][i:i+3] for i in range(1, len(v[k+"_fw"]), 3) if (len(v[k+"_fw"])- i) >= 3]
    fw_rev_codons[rev3] = [v[k+"_rev"][i:i+3] for i in range(2, len(v[k+"_fw"]), 3) if (len(v[k+"_fw"])- i) >= 3]
    outfh.write(fw1 + "\n")
    outfh.write("\t".join(fw_rev_codons[fw1]))
    outfh.write("\n" + fw2 + "\n")
    outfh.write("\t".join(fw_rev_codons[fw2]))
    outfh.write("\n" + fw3 + "\n")
    outfh.write("\t".join(fw_rev_codons[fw3]))
    outfh.write("\n" + rev1 + "\n")
    outfh.write("\t".join(fw_rev_codons[rev1]))
    outfh.write("\n" + rev2 + "\n")
    outfh.write("\t".join(fw_rev_codons[rev2]))
    outfh.write("\n" + rev3 + "\n")
    outfh.write("\t".join(fw_rev_codons[rev3]))
    outfh.write("\n")
outfh.close()
```

#### 6. Translate each of the six reading frames into amino acids. Create one file for which you print the six reading frames (Python_08.codons-6frames.nt) and one file for which you print the translation of the six reading frames (Python_08.translated.aa).


```python
def translate_dna_to_aa(sequence): #sequence = list of codons

    codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    proteinsequence = ""
    for codon in sequence:
        if codon in codontable:
            proteinsequence += codontable[codon]
    sequence = ""
    return proteinsequence

#make outfile
outfh = open("Python_08.translated.aa", "w")

#loop through dictionary
for k in fw_rev_codons:
    outfh.write(k+"\n")
    sequence = fw_rev_codons[k]
    prot_seq = translate_dna_to_aa(sequence) #calls translate function
    outfh.write(prot_seq)
    outfh.write("\n")

#close outfile
outfh.close()

```

#### 7. Find the longest peptide sequence (M-->Stop) of all the six translated reading frames for a single sequence. Do this for all the sequence records. For each sequence, print out in FASTA format the six frames of codons to one file (Python_08.codons-6frames.nt), the translations to a second file (Python_08.translated.aa), and the single longest translated peptide to a third file (Python_08.translated-longest.aa).


```python
import re

outfh = open("Python_08.translated.aa", "w")
outfh2 = open("Python_08.translated-longest.aa", "w")

for k in fw_rev_codons:
    outfh.write(k+"\n")
    sequence = fw_rev_codons[k]
    prot_seq = translate_dna_to_aa(sequence) #calls translate function
    outfh.write(prot_seq)
    outfh.write("\n")

    # get the longest match
    longest_match = ""
    outfh2.write(k+"\n")
    for match in re.finditer(r"M.*?_", prot_seq):
        stop = int(match.end())
        start = int(match.start())
        if (stop - start) > len(longest_match): #check length
            longest_match = match.group() #if longer, rewrite
outfh2.write(longest_match+"\n") #watch out for indentation! this has to be outside the previous loop

outfh.close()
outfh2.close()

```

#### 8. Finally determine which subset of codons produced the longest peptide for each sequence record. Print this to a fourth file in FASTA format (Python_08.orf-longest.nt).


```python
import re

outfh = open("Python_08.translated.aa", "w")
outfh2 = open("Python_08.translated-longest.aa", "w")
outfh3 = open("Python_08.orf-longest.nt", "w")

for k in fw_rev_codons:
    outfh.write(k+"\n")
    sequence = fw_rev_codons[k]
    prot_seq = translate_dna_to_aa(sequence)
    outfh.write(prot_seq)
    outfh.write("\n")

    longest_match = ""
    outfh2.write(k+"\n")
    for match in re.finditer(r"M.*?_", prot_seq):
        stop = int(match.end())
        start = int(match.start())
        if (stop - start) > len(longest_match):
            longest_match = match.group()
            stop = int(match.end()) #get the NEW end
            start = int(match.start()) #get updated start
            
            joined = "".join(sequence) #gets codons in a string, not list
            
            outfh3.write(k + "\n") #write key
            outfh3.write(joined[start*3:(stop*3)]) #write orf
            outfh3.write("\n")

        outfh2.write(longest_match+"\n")
 

outfh.close()
outfh2.close()
outfh3.close()
```
