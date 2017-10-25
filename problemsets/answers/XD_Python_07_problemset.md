
# Problem Set 7 pfb2017

#### 1.Create a function to format a string of DNA so that each line is no more than 60 nt long.
* INPUT: a string of DNA without newlines
* RETURNS: a string of DNA with lines no more than 60 nucleoties long


```python
dna="GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT"
n=60
def print_lines(string):
    list_60dna = [string[i:i+n] for i in range(0, len(string), n)]
    print(*list_60dna, sep='\n')
print_lines(dna)
```

    GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTT
    CTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTT
    GCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCA
    GACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
    TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTC
    CCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATG
    GTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGT
    GGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
    GTCATCTTCT


I used list comprehension to create a list of codons. You could expand this into a longer for loop. I also use a shorthand to iterate through my list, \*expression. Check here for more detail https://docs.python.org/3/reference/expressions.html#calls

#### 2. Modify your function so that it will work whether the DNA string does or does not have newlines.


```python
dna='''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

def print_lines(string):
    string = string.replace("\n", "") #get rid of \n
    #print(dna)
    list_60 = [string[i:i+60] for i in range(0, len(string), 60)]
    print(*list_60, sep='\n')
print_lines(dna)
```

    GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTT
    CTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTT
    GCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCA
    GACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
    TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTC
    CCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATG
    GTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGT
    GGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
    GTCATCTTCT


I use string.replace() to remove newline characters to an empty string. Sometimes string.strip() doesn't work when newline chaeacters are in the middle of strings. 

#### 3. Modify your function so that it takes two arguments, the DNA string and the max length of each line.


```python
def print_lines(string, len_line):
    string = string.replace("\n","")
    len_line = int(len_line)
    to_print = [string[i:i+len_line] for i in range(0, len(string), len_line)]
    return print(*to_print, sep='\n')
```

#### 4. Modify your script so that it can take two command line arguments:


```python
import argparse
#name your parser
parser = argparse.ArgumentParser(description="A test program that reads in some number of lines from an input file. The output can be screen or an output file")

#name and describe the input you want
parser.add_argument("file", help="path to string filename, full path please.")
parser.add_argument("lines", type=int, help ="how long you want the printed lines to be, interger only!")

args = parser.parse_args()
# arguments appear in args
filename = args.file
#lines = args.line
max_line = args.lines

#open file
fh = open(filename, "r")

#initialize 
dic = {} #key: header, sequence : value
dna = ""

#loop through the input file
for line in fh:
    line = line.strip()
    if line.startswith(">"):
        header = line
        dic[header] = dna
        dna = "" #empty sequence!! 
    else:
        dna += line
        dic[header] = dna
        
#print to stdout
for k, v in dic.items():
    print(k)
    print_lines(v, max_line)
```
