Python 7 - Regular Expressions - Problem Set
===================

1. In the file [Python_07_nobody.txt](https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/Python_07_nobody.txt) find every occurrence of 'Nobody' and print out the position.


```python
import re
with open('Python_07_nobody.txt') as nobody:
	for line_number, line in enumerate(nobody):
		for found in re.finditer(r"Nobody", line):
			print("Found match in line {} pos {}".format(line_number, found.start()+1))
```
2. In the file [Python_07_nobody.txt](https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/Python_07_nobody.txt) substitute every occurrence of 'Nobody' with your favorite name and write an output file with that person's name (ex. Michael.txt).


```python
import re
m=open('Micheal.txt', 'w')
with open('Python_07_nobody.txt') as nobody:
	for line in nobody:
		line=line
		new_str = re.sub(r'Nobody', 'Michael', line)
		m.write(new_str)
m.close()
```

3. Using pattern matching, find all the header lines in [Python_07.fasta](https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/Python_07.fasta). Note that the format for a header in a fasta file is a line that starts with a greater than symbol and is followed by some text (e.g. `>seqName description` where seqName is the sequence name or identifier. The identifier cannot have spaces in it. The description that follows it can have spaces.)

```python
with open('Python_07.fasta') as fasta:
	for line in fasta:
		line=line.rstrip()
		header=re.search(r'\>.+', line)
		if header:
			print(header.group(0))
```

4. If a line matches the format of a FASTA header, extract the sequence name and description using sub patterns (groups).
	- Print lines something like this `id:"extracted seq name" desc:"extracted description"`

```python
with open('Python_07.fasta') as fasta:
	for line in fasta:
		line=line.rstrip()
		header=re.search(r'\>([^\s]+)\w*(.*)', line)
		if header:
			name=header.group(1)
			desc=header.group(2)
			print("id: {}\tdesc:{}".format(name, desc))
```

5. Create or modify your FASTA parser to use regular expressions. Also make sure your parser can deal with a sequence that is split over many lines.

```python
with open('Python_07.fasta') as fasta:
	sequences={}
	sequence=''
	for line in fasta:
		line=line.rstrip()
		#check if we are on a header line
		if re.search(r'\>([^\s]+)\w*(.*)', line) is not None:
			#if sequence is filled, let's put it into the dictionary:
			if sequence:
				sequences[header]=sequence
				sequence=''
			#store the header
			header=re.search(r'\>([^\s]+)\w*(.*)', line).group(1)
		#if we're not on a header line, it has to be a sequence line, so store it
		else:
			sequence+=line
		#store the last sequence:
		sequences[header]=sequence

for sequence in sequences:
	print("ID: {}\tSEQ: {}".format(sequence, sequences[sequence]))


```		

6. The enzyme ApoI has a restriction site: R^AATTY where R and Y are degenerate nucleotideides. See the IUPAC table to identify the nucleotide possibilities for the R and Y. Write a regular expression to find and print all occurrences of the site in the following sequence [Python_07_ApoI.fasta](https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/Python_07_ApoI.fasta).

```
>seq1
GAATTCAAGTTCTTGTGCGCACACAAATCCAATAAAAACTATTGTGCACACAGACGCGAC
TTCGCGGTCTCGCTTGTTCTTGTTGTATTCGTATTTTCATTTCTCGTTCTGTTTCTACTT
AACAATGTGGTGATAATATAAAAAATAAAGCAATTCAAAAGTGTATGACTTAATTAATGA
GCGATTTTTTTTTTGAAATCAAATTTTTGGAACATTTTTTTTAAATTCAAATTTTGGCGA
AAATTCAATATCGGTTCTACTATCCATAATATAATTCATCAGGAATACATCTTCAAAGGC
AAACGGTGACAACAAAATTCAGGCAATTCAGGCAAATACCGAATGACCAGCTTGGTTATC
AATTCTAGAATTTGTTTTTTGGTTTTTATTTATCATTGTAAATAAGACAAACATTTGTTC
CTAGTAAAGAATGTAACACCAGAAGTCACGTAAAATGGTGTCCCCATTGTTTAAACGGTT
GTTGGGACCAATGGAGTTCGTGGTAACAGTACATCTTTCCCCTTGAATTTGCCATTCAAA
ATTTGCGGTGGAATACCTAACAAATCCAGTGAATTTAAGAATTGCGATGGGTAATTGACA
TGAATTCCAAGGTCAAATGCTAAGAGATAGTTTAATTTATGTTTGAGACAATCAATTCCC
CAATTTTTCTAAGACTTCAATCAATCTCTTAGAATCCGCCTCTGGAGGTGCACTCAGCCG
CACGTCGGGCTCACCAAATATGTTGGGGTTGTCGGTGAACTCGAATAGAAATTATTGTCG
CCTCCATCTTCATGGCCGTGAAATCGGCTCGCTGACGGGCTTCTCGCGCTGGATTTTTTC
ACTATTTTTGAATACATCATTAACGCAATATATATATATATATATTTAT
```

```python
with open('Python_07_ApoI.fasta') as fasta:
	sequences={}
	sequence=''
	for line in fasta:
		line=line.rstrip()
		#check if we are on a header line
		if re.search(r'\>([^\s]+)\w*(.*)', line) is not None:
			#if sequence is filled, let's put it into the dictionary:
			if sequence:
				sequences[header]=sequence
				sequence=''
			#store the header
			header=re.search(r'\>([^\s]+)\w*(.*)', line).group(1)
		#if we're not on a header line, it has to be a sequence line, so store it
		else:
			sequence+=line
		#store the last sequence:
		sequences[header]=sequence

#look for the restriction site:
my_sequence='seq1'
sequence=sequences[my_sequence]

for motif in re.findall(r"[AG]AATT[CT]",sequence):
	print(motif)
```		

7. Determine the site(s) of the physical cut(s) by ApoI in the above sequence. Print out the sequence with "^" at the cut site.

  Hints:  
   - Use `sub()`  
   - Use subpatterns (parentheses and `group()` ) to find the cut site within the pattern.
   - Example: if the pattern is GACGT^CT the following sequence

```
AAAAAAAAGACGTCTTTTTTTAAAAAAAAGACGTCTTTTTTT
```
we want to display the cut site like this:

```
AAAAAAAAGACGT^CTTTTTTTAAAAAAAAGACGT^CTTTTTTT
```

```python
with open('Python_07_ApoI.fasta') as fasta:
	sequences={}
	sequence=''
	for line in fasta:
		line=line.rstrip()
		#check if we are on a header line
		if re.search(r'\>([^\s]+)\w*(.*)', line) is not None:
			#if sequence is filled, let's put it into the dictionary:
			if sequence:
				sequences[header]=sequence
				sequence=''
			#store the header
			header=re.search(r'\>([^\s]+)\w*(.*)', line).group(1)
		#if we're not on a header line, it has to be a sequence line, so store it
		else:
			sequence+=line
		#store the last sequence:
		sequences[header]=sequence

#look for the restriction site:
my_sequence='seq1'
sequence=sequences[my_sequence]

cut_sequence=sequence
for motif in re.finditer(r"([AG])(AATT[CT])",sequence):
	cut_sequence=re.sub(motif.group(0), "^".join([motif.group(1), motif.group(2)]), cut_sequence)
print(cut_sequence)
```		

8. Now that you've done your restriction digest, determine the lengths of your fragments and sort them by length (in the same order they would separate on an electrophoresis gel).

Hint: Convert this string:

```
AAAAAAAAGACGT^CTTTTTTTAAAAAAAAGACGT^CTTTTTTT
```

Into this list:

```
["AAAAAAAAGACGT","CTTTTTTTAAAAAAAAGACGT","CTTTTTTT"]
```
```python
with open('Python_07_ApoI.fasta') as fasta:
	sequences={}
	sequence=''
	for line in fasta:
		line=line.rstrip()
		#check if we are on a header line
		if re.search(r'\>([^\s]+)\w*(.*)', line) is not None:
			#if sequence is filled, let's put it into the dictionary:
			if sequence:
				sequences[header]=sequence
				sequence=''
			#store the header
			header=re.search(r'\>([^\s]+)\w*(.*)', line).group(1)
		#if we're not on a header line, it has to be a sequence line, so store it
		else:
			sequence+=line
		#store the last sequence:
		sequences[header]=sequence

#look for the restriction site:
my_sequence='seq1'
sequence=sequences[my_sequence]

cut_sequence=sequence

for motif in re.finditer(r"([AG])(AATT[CT])",sequence):
	cut_sequence=re.sub(motif.group(0), "^".join([motif.group(1), motif.group(2)]), cut_sequence)

fragments=cut_sequence.split('^')
fragments=sorted(fragments, key=len)
for fragment in fragments:
	print(fragment)
```
9. Download this [file](ftp://ftp.neb.com/pub/rebase/bionet.txt) of enzymes and their cut sites to fill a dictionary of enzymes paired with their recognition patterns. Be aware of the header lines, and be aware of how the columns are delimited. You'll modify this script in the next question.

```python
import re
with open('bionet.txt') as enz:
	rest_enz={}
	for line in enz:
		f=re.search(r'^(.*?)\s{4,}(.*[A-Z^])$', line)
		if f:
			rest_enz[f.group(1)]=f.group(2)

rest_enz
```

10. Write a script which takes two command line arguments: the name of an enzyme and a fasta file with a sequence to be cut. Load a dictionary of enzyme names and cut sites from the code you developed in question 9.
   If the enzyme is present in the dictionary, and can cut the sequence, print out:
     - the sequence, annotated with cut sites
     - the number of fragments
     - the fragments in their natural order (unsorted)
     - the fragments in sorted order (largest to smallest)
