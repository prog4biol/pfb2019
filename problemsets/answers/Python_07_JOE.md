#!/usr/bin/env python3

import re

# Problem 1
In the file Python_07_nobody.txt find every occurrence of 'Nobody' and print out the position.
```
counter =1
with open("Python_07_nobody.txt") as nobody_FO:
    for line in nobody_FO:
        for match in re.finditer(r"Nobody",line):
            start = match.start() +1
            end = match.end()
            print("Line: {}\tstart:{}\tend:{}".format(counter,start,end))
            counter+=1
```
# Problem 2
In the file Python_07_nobody.txt substitute every occurrence of 'Nobody' with your favorite name and write an output file with that person's name (ex. Michael.txt).
```
with open("Python_07_nobody.txt") as nobody_FO:
    for line in nobody_FO:
        line = line.rstrip()
        line = re.sub(r"Nobody","Pinkerton", line)
        print(line)
```
# Problem 3
Using pattern matching, find all the header lines in Python_07.fasta. Note that the format for a header in a fasta file is a line that starts with a greater than symbol and is followed by some text (e.g. >seqName description where seqName is the sequence name or identifier. The identifier cannot have spaces in it. The description that follows it can have spaces.)


```
with open("Python_07.fasta") as FH:
    for line in FH:
        if re.search(r"^>",line):
            print(line.rstrip()) 
```

# Problem 4
If a line matches the format of a FASTA header, extract the sequence name and description using sub patterns (groups).
- Print lines something like this id:"extracted seq name" desc:"extracted description"
```
with open("Python_07.fasta") as FH:
    for line in FH:
        line = line.rstrip()
        if re.search(r"^>",line):
            for found in re.finditer(r"^>(\S*)? (.*)$", line):
                ID = found.group(1)
                Desc = found.group(2)
        print(ID,"\t",Desc) 
```

#Problem 5

Create a FASTA parser, or modify your FASTA parser from the previous problem set, to use regular expressions. Also make sure your parser can deal with a sequence that is split over many lines.

```
seqdict = {}

with open("Python_07.fasta") as FH:
    seq = ''
    for line in FH:
        line = line.rstrip()
        if re.search(r"^>", line):
            header = line
            seq = ''
        else:
            seq += line
            seqdict[header] = seq
seqdict[header] = seq
print (seqdict)
```

# Problem 6

The enzyme ApoI has a restriction site: R^AATTY where R and Y are degenerate nucleotideides. See the IUPAC table to identify the nucleotide possibilities for the R and Y. Write a regular expression to find and print all occurrences of the site in the following sequence Python_07_ApoI.fasta.

```
seq = ''

with open("Python_07_ApoI.fasta") as FH:
    for line in FH:
        seq += line

for match in re.finditer(r"[A|G]AATT[C|T]",seq):
    print (match)
```

# Problem 7 

## seq1
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

Determine the site(s) of the physical cut(s) by ApoI in the above sequence. Print out the sequence with "^" at the cut site.

Hints:

- Use sub()
- Use subpatterns (parentheses and group() ) to find the cut site within the pattern.
- Example: if the pattern is GACGT^CT the following sequence
AAAAAAAAGACGTCTTTTTTTAAAAAAAAGACGTCTTTTTTT
we want to display the cut site like this:

> AAAAAAAAGACGT\^CTTTTTTTAAAAAAAAGACGT\^CTTTTTTT


```
seq = ''

with open("Python_07_ApoI.fasta") as FH:
    for line in FH:
        seq += line

newseq = re.sub(r"([A|G])(AATT[C|T])",r"\1^\2",seq)
print (newseq)

```

# Problem 8

Now that you've done your restriction digest, determine the lengths of your fragments and sort them by length (in the same order they would separate on an electrophoresis gel).
Hint: Convert this string:

> AAAAAAAAGACGT\^CTTTTTTTAAAAAAAAGACGT\^CTTTTTTT
Into this list:

> ["AAAAAAAAGACGT","CTTTTTTTAAAAAAAAGACGT","CTTTTTTT"]

```
seq = ''

with open("Python_07_ApoI.fasta") as FH:
    for line in FH:
        seq += line

newseq = re.sub(r"([A|G])(AATT[C|T])",r"\1^\2",seq)

fragList = []
for match in re.findall(r"\^(\w+)[\^\n]", newseq):
    fragList.append(match)
fragList = sorted(fragList, key=len, reverse=True)

for frag in fragList:
    fragLen = len(frag)
    print("Length: {}\tFragment: {}".format(fragLen, frag))
```
# Problem 9 

Download this file: ftp://ftp.neb.com/pub/rebase/bionet.txt of enzymes and their cut sites to fill a dictionary of enzymes paired with their recognition patterns. Skip the top 10 header lines and be aware of how the columns are delimited. You'll modify this script in the next question.

```
enzymeDict = {}

with open("bionet.txt", 'r') as FH:
    for n in range(1,10):
        next(FH)
    for line in FH:
            line = line.rstrip()
            if re.match(r"^\w",line):
                cleanline = re.sub(r" {2,}", r"\t",line)
                splitline = cleanline.split('\t')
                enzymeDict[splitline[0]]=splitline[1]

print(enzymeDict)
```

