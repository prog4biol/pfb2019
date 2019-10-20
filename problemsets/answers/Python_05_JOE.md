
#!/usr/bin/env python

# Problem 1
Write a script in which you construct a dictionary of your favorite things.
```
favorites_list = ['book', 'kafka on the shore', 'song', 'king of spain', 'tree', 'redwood']

favorites = {}

for iteration in range(0,len(favorites_list),2):
    favorites[favorites_list[iteration]] = favorites_list[iteration + 1]
```

# Problem 2
Print out your favorite book
```
print(favorites['book'])
```

# Problem 3
Print out your favorite book but use a variable in the key.
```
fav_thing = 'book'
print (favorites[fav_thing])
```
# Problem 4
Now print your favorite tree
```
print (favorites['tree')
```
# Problem 5

Add your favorite 'organism' to the dictionary. Make organism the new value of 
```
fav_thing
favorites['organism'] = 'gibbon'
fav_thing = 'organism'
print(favorites[fav_thing])
```
# Problem 6
Take a value from the command line for fav_thing and print the value of that item from the dictionary. Maybe you want to print out all the keys to the user so that they know what to pick from. Check out input(). Here is a link.

```
import sys

print("Choose a value for your favorite thing. Choose among: {}".format(favorites.keys()))
category=input()
print(favorites[category])

```

# Problem 7
Change the value of your favorite organism.

```
value = sys.argv[2]
favorites['fav_thing'] = value
print(favorites)

```

# Problem 8
Get the fav_thing from the command line and a new value for that key. Change the value with the user inputted value.

```
new_category = sys.argv[1]
new_fav = sys.argv[2]
favorites[new_category]=new_fav

print("what is your favorite {}?".format(new_category))
new_fav = input()

favorites[new_category]=new_fav

for key in favorites:
    print (key,"\t", favorites[key])
```

# Problem 9
Use a for loop to print out each key and value of the dictionary.

```
for key,value in favorites.items():
    print("My favorite {} is {}".format(key,value))
```

# Problem 10
Make a set using the two different syntaxes for creating a set myset = set() and myset2 = {}. What is the difference? Does it matter how you make it?

```
mySet = set('ATGTGGG')
mySet2 = {'ATGCCT'}

print(mySet)
print(mySet2)

>>> {'A', 'T', 'G'}
>>> {'ATGCCT'}
```
The differences is that when using the "set" command, each item in the string becomes a separate item in the set

# Problem 11
Write a script to find the intersection, difference, union, and symetrical difference between these two sets.

```
Set_A = set(['3','14','15','9','26','5','35','9'])
Set_B = set(['60','22','14','0','9'])

print("intersection = ", Set_A & Set_B,"\ndifference = ",Set_A - Set_B,"\nunion = ", Set_A | Set_B,"\nsymetrical difference = ",Set_A ^ Set_B)

```

# Problem 12

If you create a set using a DNA sequence, what will you get back? Try it with this sequence:

```
Set_Seq = set('GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC')

print(Set_Seq)

>>> set(['A', 'C', 'T', 'G'])

```

# Problem 13

Nucleotide Composition. Write a script that:
- determines the unique characters in this sequence
- iterate over each unique character and count the number found in the sequence
store each count in a dictionary. example: nt_comp['A']=2
- when you are done counting each character calculate and report the nucleotide composition and the GC content.


```
sequence = list('GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA')

Set_Seq = set(sequence)

nucDict = {}

for character in sorted(Set_Seq):
    count = sequence.count(character)
    nucDict[character] = count  
    print (character, count) 

GC = (nucDict['G'] + nucDict['C'])/len(sequence)

print("GC content = {:.2}".format(GC))
```

# Problem 14

Git over it, dude...
