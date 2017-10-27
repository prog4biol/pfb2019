Python 8 Problem Set
===================
**For this problem set I wrote a scrip that answers all of the questions using functions. I've put the entire script in the answers folder as MSC_Python_08_problemset.py. Each quesiton below has the relevant code with it.**

My script is devided into two sections "main" and "functions" main is where yo see the flow of data. The functions do all the work

I start in main with a call to a function that parses the file and builds a data structure that I can pass to other functions.

main
```python
seq_dict = make_data_structure(sys.argv[1])
```

Functions
```python
def make_data_structure(file):
  #this is the initial parsing of the file
  f_all = open(file,"r")
  seq_dict = {}
  def_line = ""
  #lopp through the file a line at a tie
  for line in f_all:
    #strip the line return from the line
    line = line.rstrip("\n")
    #check for the def line
    if line.startswith('>'):
      def_line = line
    #if it is not the def line it must be sequence
    else:
      #if the def line is in the dictionary we have already
      #a value to the key so we can append the next one to it
      if def_line in seq_dict:
        seq_dict[def_line] += line 
      #if we dont see it it is the first line of seuqence after
      #the def line and we need to asign it as the value of the key
      else:
        seq_dict[def_line] = line
  #close the file we were reading
  f_all.close()      
  #return the data structure
  return(seq_dict)
```

I can then pass seq_dict to make_trans_and_cds_data_structures to make two more datastructures that will help me get the data into a form that I can access more easily

Main
```python
trans_dict, codon_dict = make_trans_and_cds_data_structures(seq_dict)
```

Functions
```python
def make_trans_and_cds_data_structures(seq_dict):
  trans_dict = {}
  codon_dict = {}
  for seq_id in seq_dict:
#    print(seq_id)
  #calculate the nucleotide frequencies seqName\tA_count\tT_count\tG_count\C_count
    sub_codon_dict = {}
  #reverse comp the sequnce
    rc_seq = rev_comp(seq_dict[seq_id])
    #get the codons for the forward strand. First I'm grabbing the data 
    #that I need pass to the function
    f_seq = seq_dict[seq_id]
    seq_length = len(seq_dict[seq_id])
    
    #when I defined the function I used an infomative tag. This is helpful when
    #you are reading the code and are trying to figure out what a funciton does.
    #a bare number is not that informative but frame=number has some additional.
    #meaning
    sub_codon_dict['fs_f1'] = get_codons(dna=f_seq, frame=0, seq_len=seq_length)
    sub_codon_dict['fs_f2'] = get_codons(dna=f_seq, frame=1, seq_len=seq_length)
    sub_codon_dict['fs_f3'] = get_codons(dna=f_seq, frame=2, seq_len=seq_length)
    #get the codons for the reverse complement
    sub_codon_dict['rs_f1'] = get_codons(dna=rc_seq, frame=0, seq_len=seq_length)
    sub_codon_dict['rs_f2'] = get_codons(dna=rc_seq, frame=1, seq_len=seq_length)
    sub_codon_dict['rs_f3'] = get_codons(dna=rc_seq, frame=2, seq_len=seq_length)
    #add the codons in all 6 frames to the big codon dictionary
    codon_dict[seq_id] = sub_codon_dict    
    
    #get the translations for all of the reading frames identified above
    sub_trans_dict = {}
    for frame in codon_dict[seq_id]:
      sub_trans_dict[frame] = translate(codon_dict[seq_id][frame]) 

    #add the sub dictionary to the bigger dictionary  
    trans_dict[seq_id]=sub_trans_dict
  #retrn the two new data structures to main
  return(trans_dict, codon_dict)
```

This function called three more functions get_codons rev_comp and translate.

Functions
```python
#I defined this funtion with key value pairs. this way
#when we call it it we have informative tags to help us
#understand what is hapening in the function
def get_codons(dna = None, frame = None, seq_len = None):
  codons= []
  for i in range(frame, seq_len, 3):
    codon = dna[i:i+3]
    if not len(codon) % 3:
      codons.append(codon)
  return(codons)
```

```python
def rev_comp(seq_string):
  #this is the reverse compliment that we
  #wrote for a a previous problem
  complement = seq_string.replace('A','t')
  complement = complement.replace('T','a')
  complement = complement.replace('G','c')
  complement = complement.replace('C','g')
    #upper case it
  complement = complement.upper()
    #reverse it
  rev_comp = complement[::-1]
  return(rev_comp)
```

```python
def translate(codon_list):
  #I stole this codon table from the internet
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
  #initialize a string to add the amino acids to once they
  #are translated
  translation = ""
  #loop through the codons
  for codon in codon_list:
    #look up the codon in the dictionary and append the 
    #amino acids to the string
    translation += codontable[codon]
    #return the translation
  return(translation)

```



__Don't forget to use a small test data set when you are testing your code. Make sure you know what the correct answer should be__

1. **Take a mulit-FASTA [Python_08.fasta](https://raw.githubusercontent.com/srobb1/pfb2017/master/files/Python_08.fasta) file from user input and calculate the nucleotide composition for each sequence. Use a datastructure to keep count. Print out each sequence name and its compostion in this format `seqName\tA_count\tT_count\tG_count\C_count`**


Here is a structure of a handy datastructure to store this information
```
seqs[geneName][nucleotide]=count

seqs['geneA']['A'] = 2
seqs['geneA']['T'] = 3
seqs['geneA']['G'] = 3
seqs['geneA']['C'] = 1

for question #2 we can send the seq_dict to a function and do the nucleotide counting there. I called the function output_gc_content

Main
```python
output_gc_content(seq_dict)
```

Functions
```python
def output_gc_content(seq_dict):
  #print a header for our output
  print("gene_id\tA\tT\tG\tC")
  #start a dictionary 
  nucl_dict = {}
  #loop through the keys in the sequence dictionary
  for id in seq_dict:
    #get the DNA sequence out of the dictionary
    sequence = seq_dict[id]
    #split the DNA string into a list
    sequence_list = list(sequence)
    #initialize the inner dictionary
    nucl_counts = {}
    #loop through all of the nucleotides
    for nucl in sequence_list:
      #if the nucleotide is already in the dictionary add one
      if nucl in nucl_counts:
        nucl_counts[nucl] += 1
      #if the nucleotide isn't in the dictionary add the key and set it equal to 1
      else:
        nucl_counts[nucl] = 1
        #make the outer key in the dictionary
    nucl_dict[id] = {}
    #Assign the inner dictionary to the key we just initialized
    nucl_dict[id] = nucl_counts
  #lopp through the genes in the dictionary and print out the nucleotide counts
  for gene in nucl_dict:
    print(gene, "\t", nucl_dict[gene]['A'],"\t", nucl_dict[gene]['T'],"\t", nucl_dict[gene]['G'],"\t", nucl_dict[gene]['C'])
```

seqs['geneB']['A'] = 1
seqs['geneB']['T'] = 5
seqs['geneB']['G'] = 2
seqs['geneB']['C'] = 2
``` 

2. **Write a script that takes a multi-FASTA file [Python_08.fasta](https://raw.githubusercontent.com/srobb1/pfb2017/master/files/Python_08.fasta) from user input and breaks each sequence into codons (every three nucleotides is a codon) in just the first reading frame. Your output should look like this** 
```
seq1-frame-1-codons
CAT GCT TGA GTC
``` 
**Write the output to a file called 'Python_08.codons-frame-1.nt'.**

The print_nuc_frames uses the codon_dict data structure to print the file that you need for problems #2, #4, #5, and #6

Main
```python
print_nuc_frames(codon_dict)
```

Functions
```python
def print_nuc_frames(codon_dict): #5 and #6
  #open files to write to for questions #5 and #6
  f_nuc_frames_out = open("Python_08.codons-6frames.nt","w")
  f_trans_out = open("Python_08.translated.aa","w")
  #loop through the ids in the dictionary
  for id in codon_dict:
    #loop through the frames
    for frame in codon_dict[id]:
      #write to one out file
      f_nuc_frames_out.write(id + "_" + frame + "\n")
      #join on a space to print the codons seperately. you can join 
      #on no space ''.join to print them all together
      f_nuc_frames_out.write(' '.join(codon_dict[id][frame]) + "\n")
      #now print the output for question #6. I called the translation 
      #function within the print statemnet.
      f_trans_out.write(id + "_" + frame + "\n")
      f_trans_out.write(translate(codon_dict[id][frame]) + "\n")
  f_nuc_frames_out.close()
  f_trans_out.close()
```

3. **Add in exception handling. Throw and handle (try/except) the exception**
   - if no input is provided  
   - if the file cannot be opened
   - if the file does not end in '.fasta' or '.fa' or '.nt'
   - if a non ATGCN charcter is found in the sequence

Still need to add this

4. **Now produce codons in the first three reading frames for each sequence and print out ids and sequence records for each frame and print to a file called 'Python_08.codons-3frames.nt'**

See question 2

For example
```
seq1-frame-1-codons
ATG TTG
seq-frame-2-codons
TGT TGA
``` 

5. **Now reverse complement each sequence and print out all six reading frames to a file called 'Python_08.codons-6frames.nt'**

See question 2

6. **Translate each of the six reading frames into amino acids. Create one file for which you print the six reading frames (Python_08.codons-6frames.nt) and one file for which you print the translation of the six reading frames (Python_08.translated.aa).**

See question 2

7. **Find the longest peptide sequence (M-->Stop) of all the six translated reading frames for a single sequence. Do this for all the sequence records. For each sequence, print out in FASTA format the six frames of codons to one file (Python_08.codons-6frames.nt), the translations to a second file (Python_08.translated.aa), and the single longest translated peptide to a third file (Python_08.translated-longest.aa).**

The find_longest_translation function takes the trans dictionary and prints the outpur for question 7 and returns a data structure that will help us get the lonest CDS

Main
```python
longest_trans = find_longest_translation(trans_dict)
```
Functions
```python
def find_longest_translation(protein_dict): #7
  f_aa_longest_out = open("Python_08.translated-longest.aa","w")
  #start the longest transcript to lenght zero to start. And make a dictionary 
  #to keep our data in for later use
  last_longest = 0 
  longest_tran = {}
  #loop through the sequence ids in the dictionary
  for id in protein_dict:
    last_longest = 0 #reset this for the new id 
    longest_tran[id]={} #I had this thing in the down one loop and it kept getting reset
    #loop through the frames
    for frame in protein_dict[id]:
      #split on the stops "_" in the translation
      orfs = protein_dict[id][frame].split("_")
      orfs.sort(key = len, reverse=True) #sort it to get the longest one first
      #loop through all of the orfs
      for orf in orfs:
          m_pos = orf.find("M") #this returns -1 if it doesn't find anything 
          if m_pos == -1: #make sure there is a methionene
            continue #skip it if there isn't a methionene
          else:
            longest = len(orf) - m_pos # this is the longest orf in the frame

            #here is where we are finding the longest open reading frame out of all the 
            #potential translations. I could add another function to print out the the 
            #files that are requested in question #7. I took an aproach that reduces
            #the data structure I passed in to this function to a single longest peptide/
            #open reading frame instead
            
            #check to see if the current open reading frame is the longest one
            if longest > last_longest:
              #make a new dictionary
              sub_longest_tran = {}
              #load it up
              sub_longest_tran['len'] = longest
              sub_longest_tran['frame'] = frame
              sub_longest_tran['seq'] = orf[m_pos:]
              #put it in the bigger dictionary. If there is no methionene the id key points 
              #to an empty dictionary. We neeed to remember this for later
              longest_tran[id] = sub_longest_tran
              #update the last_longest variable to reflect the new information
              last_longest = longest

  #loop through dictionary to print to the file
  for lt_id in longest_tran:
    #check to see if there was a Met. An empty dicitonary returns false
    if longest_tran[lt_id]: 
      #I wrapped the argument to the write method below so it wasn't too long
      f_aa_longest_out.write(lt_id + "_" + 
                             longest_tran[lt_id]['frame'] + "\n" + 
                             longest_tran[lt_id]['seq'] + "\n")
    else:
      continue #move on if there is no methionene. I could have printed a dummy entry 
  f_aa_longest_out.close()
  return(longest_tran)
```

8. **Finally determine which subset of codons produced the longest peptide for each sequence record. Print this to a fourth file in FASTA format (Python_08.orf-longest.nt).**

This one takes the last three data structures I made and combines the information in each one to get the longest CDS and print the file for problem #8. It returns a structure that can be used later, but we don't need it for any more problems.

Main
```python
longest_cds = match_longest_cds(longest_trans, codon_dict, trans_dict)
```

Functions
```python
def match_longest_cds(longest_trans, codon_dict, trans_dict): #8
  # this is where I need to match up the longest protein with the codons
  # the basic structure of these dictionaries lends them to getting stuff out 
  # of each other
  f_nuc_longest_orf = open("Python_08.orf-longest.nt","w")
  cds_dict_to_return = {}

  #lo0p through all of the longest transcripts
  for id in longest_trans:
    #if there wasn't an open reading frame that started with a Met
    #print out a dummy entry. In practice you would not print this
    #you would use a continue to skip it. As I have it here it will 
    #contaminate the FASTA file. 
    if not longest_trans[id]:
      f_nuc_longest_orf.write(id + "\nNO COMPLETE OPEN READING FRAME\n")
      continue #this gets past genes without a complete open reading frame 
    else:
      #if you are in here the transcipt must have a Met start.
      #get the frame and amino acid translation.
      frame = longest_trans[id]['frame']
      long_tran = longest_trans[id]['seq']
      #use the frame to get the codons from that reading frame
      longest_codons_with_stops = codon_dict[id][frame]
      #get the translation of the entire sequence with the stops. It will 
      #have the same order as the codons in longest_codons_with_stops
      trans_with_stops = trans_dict[id][frame]
      #use a regular expression search to identify the coordinates of the longest
      #translation in the big string. the span() function returns a tuple of the 
      #begining and ending of the match
      starting_in, ending_in = re.search(long_tran, trans_with_stops).span()
      #use the coordinates to slice the array
      longest_cds_in_codons = longest_codons_with_stops[starting_in:ending_in]
      #put the codons together into a single string and put it into the dictionary
      cds = "".join(longest_cds_in_codons)
      cds_dict_to_return[id + "_" + frame] = cds
      #write out the file that you need for problem 8
      f_nuc_longest_orf.write(id + "_" + frame + "\n" + cds +"\n")
  #close the file handle and return the dictionary.
  f_nuc_longest_orf.close()
  return(cds_dict_to_return)
```

This is what the entire script looks like together

```python
#!/usr/bin/env python3

#import the modules that we are goin to need.
#we need re to do patern matching and sys to 
#access the command line arguments
import re
import sys

#these are the functions. Reading from here will just be 
#confusing. The flow of the script is defined in "main,"
#so it will be best to start there.
#------------------------------------------
#------------------functions---------------
#------------------------------------------
#I defined this funtion with key value pairs. this way
#when we call it it we have informative tags to help us
#understand what is hapening in the function
def get_codons(dna = None, frame = None, seq_len = None):
  codons= []
  for i in range(frame, seq_len, 3):
    codon = dna[i:i+3]
    if not len(codon) % 3:
      codons.append(codon)
  return(codons)    
#------------------------------------------
def make_data_structure(file):
  #this is the initial parsing of the file
  f_all = open(file,"r")
  seq_dict = {}
  def_line = ""
  #lopp through the file a line at a tie
  for line in f_all:
    #strip the line return from the line
    line = line.rstrip("\n")
    #check for the def line
    if line.startswith('>'):
      def_line = line
    #if it is not the def line it must be sequence
    else:
      #if the def line is in the dictionary we have already
      #a value to the key so we can append the next one to it
      if def_line in seq_dict:
        seq_dict[def_line] += line 
      #if we dont see it it is the first line of seuqence after
      #the def line and we need to asign it as the value of the key
      else:
        seq_dict[def_line] = line
  #close the file we were reading
  f_all.close()      
  #return the data structure
  return(seq_dict)

#------------------------------------------
def rev_comp(seq_string):
  #this is the reverse compliment that we
  #wrote for a a previous problem
  complement = seq_string.replace('A','t')
  complement = complement.replace('T','a')
  complement = complement.replace('G','c')
  complement = complement.replace('C','g')
    #upper case it
  complement = complement.upper()
    #reverse it
  rev_comp = complement[::-1]
  return(rev_comp)

#------------------------------------------
def translate(codon_list):
  #I stole this codon table from the internet
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
  #initialize a string to add the amino acids to once they
  #are translated
  translation = ""
  #loop through the codons
  for codon in codon_list:
    #look up the codon in the dictionary and append the 
    #amino acids to the string
    translation += codontable[codon]
    #return the translation
  return(translation)

#------------------------------------------
def print_nuc_frames(codon_dict): #5 and #6
  #open files to write to for questions #5 and #6
  f_nuc_frames_out = open("Python_08.codons-6frames.nt","w")
  f_trans_out = open("Python_08.translated.aa","w")
  #loop through the ids in the dictionary
  for id in codon_dict:
    #loop through the frames
    for frame in codon_dict[id]:
      #write to one out file
      f_nuc_frames_out.write(id + "_" + frame + "\n")
      #join on a space to print the codons seperately. you can join 
      #on no space ''.join to print them all together
      f_nuc_frames_out.write(' '.join(codon_dict[id][frame]) + "\n")
      #now print the output for question #5. I called the translation 
      #function within the print statemnet.
      f_trans_out.write(id + "_" + frame + "\n")
      f_trans_out.write(translate(codon_dict[id][frame]) + "\n")
  f_nuc_frames_out.close()
  f_trans_out.close()
#------------------------------------------
def find_longest_translation(protein_dict): #7
  f_aa_longest_out = open("Python_08.translated-longest.aa","w")
  #start the longest transcript to lenght zero to start. And make a dictionary 
  #to keep our data in for later use
  last_longest = 0 
  longest_tran = {}
  #loop through the sequence ids in the dictionary
  for id in protein_dict:
    last_longest = 0 #reset this for the new id 
    longest_tran[id]={} #I had this thing in the down one loop and it kept getting reset
    #loop through the frames
    for frame in protein_dict[id]:
      #split on the stops "_" in the translation
      orfs = protein_dict[id][frame].split("_")
      orfs.sort(key = len, reverse=True) #sort it to get the longest one first
      #loop through all of the orfs
      for orf in orfs:
          m_pos = orf.find("M") #this returns -1 if it doesn't find anything 
          if m_pos == -1: #make sure there is a methionene
            continue #skip it if there isn't a methionene
          else:
            longest = len(orf) - m_pos # this is the longest orf in the frame

            #here is where we are finding the longest open reading frame out of all the 
            #potential translations. I could add another function to print out the the 
            #files that are requested in question #7. I took an aproach that reduces
            #the data structure I passed in to this function to a single longest peptide/
            #open reading frame instead
            
            #check to see if the current open reading frame is the longest one
            if longest > last_longest:
              #make a new dictionary
              sub_longest_tran = {}
              #load it up
              sub_longest_tran['len'] = longest
              sub_longest_tran['frame'] = frame
              sub_longest_tran['seq'] = orf[m_pos:]
              #put it in the bigger dictionary. If there is no methionene the id key points 
              #to an empty dictionary. We neeed to remember this for later
              longest_tran[id] = sub_longest_tran
              #update the last_longest variable to reflect the new information
              last_longest = longest

  #loop through dictionary to print to the file
  for lt_id in longest_tran:
    #check to see if there was a Met. An empty dicitonary returns false
    if longest_tran[lt_id]: 
      #I wrapped the argument to the write method below so it wasn't too long
      f_aa_longest_out.write(lt_id + "_" + 
                             longest_tran[lt_id]['frame'] + "\n" + 
                             longest_tran[lt_id]['seq'] + "\n")
    else:
      continue #move on if there is no methionene. I could have printed a dummy entry 
  f_aa_longest_out.close()
  return(longest_tran)

#------------------------------------------
def match_longest_cds(longest_trans, codon_dict, trans_dict): #8
  # this is where I need to match up the longest protein with the codons
  # the basic structure of these dictionaries lends them to getting stuff out 
  # of each other
  f_nuc_longest_orf = open("Python_08.orf-longest.nt","w")
  cds_dict_to_return = {}

  #lo0p through all of the longest transcripts
  for id in longest_trans:
    #if there wasn't an open reading frame that started with a Met
    #print out a dummy entry. In practice you would not print this
    #you would use a continue to skip it. As I have it here it will 
    #contaminate the FASTA file. 
    if not longest_trans[id]:
      f_nuc_longest_orf.write(id + "\nNO COMPLETE OPEN READING FRAME\n")
      continue #this gets past genes without a complete open reading frame 
    else:
      #if you are in here the transcipt must have a Met start.
      #get the frame and amino acid translation.
      frame = longest_trans[id]['frame']
      long_tran = longest_trans[id]['seq']
      #use the frame to get the codons from that reading frame
      longest_codons_with_stops = codon_dict[id][frame]
      #get the translation of the entire sequence with the stops. It will 
      #have the same order as the codons in longest_codons_with_stops
      trans_with_stops = trans_dict[id][frame]
      #use a regular expression search to identify the coordinates of the longest
      #translation in the big string. the span() function returns a tuple of the 
      #begining and ending of the match
      starting_in, ending_in = re.search(long_tran, trans_with_stops).span()
      #use the coordinates to slice the array
      longest_cds_in_codons = longest_codons_with_stops[starting_in:ending_in]
      #put the codons together into a single string and put it into the dictionary
      cds = "".join(longest_cds_in_codons)
      cds_dict_to_return[id + "_" + frame] = cds
      #write out the file that you need for problem 8
      f_nuc_longest_orf.write(id + "_" + frame + "\n" + cds +"\n")
  #close the file handle and return the dictionary.
  f_nuc_longest_orf.close()
  return(cds_dict_to_return)
#------------------------------------------
def make_trans_and_cds_data_structures(seq_dict):
  trans_dict = {}
  codon_dict = {}
  for seq_id in seq_dict:
#    print(seq_id)
  #calculate the nucleotide frequencies seqName\tA_count\tT_count\tG_count\C_count
    sub_codon_dict = {}
  #reverse comp the sequnce
    rc_seq = rev_comp(seq_dict[seq_id])
    #get the codons for the forward strand. First I'm grabbing the data 
    #that I need pass to the function
    f_seq = seq_dict[seq_id]
    seq_length = len(seq_dict[seq_id])
    
    #when I defined the function I used an infomative tag. This is helpful when
    #you are reading the code and are trying to figure out what a funciton does.
    #a bare number is not that informative but frame=number has some additional.
    #meaning
    sub_codon_dict['fs_f1'] = get_codons(dna=f_seq, frame=0, seq_len=seq_length)
    sub_codon_dict['fs_f2'] = get_codons(dna=f_seq, frame=1, seq_len=seq_length)
    sub_codon_dict['fs_f3'] = get_codons(dna=f_seq, frame=2, seq_len=seq_length)
    #get the codons for the reverse complement
    sub_codon_dict['rs_f1'] = get_codons(dna=rc_seq, frame=0, seq_len=seq_length)
    sub_codon_dict['rs_f2'] = get_codons(dna=rc_seq, frame=1, seq_len=seq_length)
    sub_codon_dict['rs_f3'] = get_codons(dna=rc_seq, frame=2, seq_len=seq_length)
    #add the codons in all 6 frames to the big codon dictionary
    codon_dict[seq_id] = sub_codon_dict    
    
    #get the translations for all of the reading frames identified above
    sub_trans_dict = {}
    for frame in codon_dict[seq_id]:
      sub_trans_dict[frame] = translate(codon_dict[seq_id][frame]) 

    #add the sub dictionary to the bigger dictionary  
    trans_dict[seq_id]=sub_trans_dict
  #retrn the two new data structures to main
  return(trans_dict, codon_dict)
#------------------------------------------
#--------------------main------------------
#------------------------------------------

#This is where you find the real flow of data through the script,
#but all of the work is done in the funtions

#I started by calling the function make_data_structure and passing it
#the FASTA file off of the command line. it returns a data structure
seq_dict = make_data_structure(sys.argv[1])

#I can then pass seq_dict to make_trans_and_cds_data_structures to 
#make two more data structures that will help me get the data into 
#a form that I can access more easily
trans_dict, codon_dict = make_trans_and_cds_data_structures(seq_dict)

#The print_nuc_frames uses the codon_dict data structure to print the
#file that you need for problem #5 and #6
print_nuc_frames(codon_dict)

#the find_longest_translation function takes the trans dictionary and 
#prints the outpur for question 7 and returns a data structure that will
#help us get the lonest CDS
longest_trans = find_longest_translation(trans_dict)

#This one takes the last three data structures I made and combines the 
#information in each one to get the longest CDS and print the file for
#problem #8. It returns a structure that can be used later, but we don't
#need it for any more problems
longest_cds = match_longest_cds(longest_trans, codon_dict, trans_dict)
```