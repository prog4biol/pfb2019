Python 5 - Dictionaries and Sets - Problem Set
===================

1.  Write a script in which you construct a dictionary of your favorite things.

> Some of my favorites:
>
> | Type | Favorite                                 |
> | ---- | ---------------------------------------- |
> | book | [Jitterbug Perfume](https://en.wikipedia.org/wiki/Jitterbug_Perfume) |
> | song | [Tom Petty - I Won't Back Down](https://www.youtube.com/watch?v=nvlTJrNJ5lA) |
> | tree | [Cedar](https://sciencing.com/cedar-trees-5432718.html) |

```python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 5.1.py

fav_dict = {
		'book' : 'Lonesome Dove',
		'song' : 'Only Skin',
		'tree' : 'Sequoia'
		}
```

2. Print out your favorite book.

```python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 5.1.py

fav_dict = {
		'book' : 'Lonesome Dove',
		'song' : 'Only Skin',
		'tree' : 'Maple'
		}

print(fav_dict['book'])
```

3. Print out your favorite book but use a variable in the key.

``` python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 5.1.py

fav_dict = {
		'book' : 'Lonesome Dove',
		'song' : 'Only Skin',
		'tree' : 'Maple'
		}

fav_thing = 'book'

print(fav_dict[fav_thing])
```

4. Now print your favorite tree.

```python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 5.1.py

fav_dict = {
		'book' : 'Lonesome Dove',
		'song' : 'Only Skin',
		'tree' : 'Maple'
		}

print(fav_dict['tree'])

5. Add your favorite 'organism' to the dictionary. Make organism the new value of `fav_thing`

​```python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 5.1.py

fav_dict = {
		'book' : 'Lonesome Dove',
		'song' : 'Only Skin',
		'tree' : 'Maple',
		'organism' : 'cat'
		}

fav_dict['organism'] = 'cat'

print(fav_dict['organism'])
```

6. Take a value from the command line for `fav_thing` and print the value of that item from the dictionary. Maybe you want to print out all the keys to the user so that they know what to pick from. Check out `raw_input()`. Here is a <a href="https://www.tutorialspoint.com/python/python_files_io.htm">link</a>.

```python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename:PS5.1.py 

favs = {
		'book' : 'Lonesome Dove',
		'song' : 'Only Skin',
		'tree' : 'pine',
		'organism' : 'cat'
		}

keyOptions = []

for key in favs.keys():
	keyOptions.append(key)

print(keyOptions)

chosen = input("From the list of items above, in which category would you like to designate a favorite? Type your answer on the command line.\n")

if chosen in keyOptions:
	favThing = input("What is your favorite thing in the category you chose?\n")
	favs[chosen] = favThing

print(favs)

print('\nDone.\n')
```

7. Change the value of your favorite organism.

```python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename:PS5.1.py


favs = {
		'book' : 'Lonesome Dove',
		'song' : 'Only Skin',
		'tree' : 'pine',
		'organism' : 'cat'
		}

newOrganism = input("What is your favorite organism?\n\n")

favs['organism'] = newOrganism

print(favs)

print('\nDone.\n')
```

8. Get the `fav_thing` from the command line and a new value for that key. Change the value with the user inputted value.

```python
#! usr/bin/env/ python3

import sys

#Owner: Shasta Webb
#Filename:PS5.1.py

favs = {
		'book' : 'Lonesome Dove',
		'song' : 'Only Skin',
		'tree' : 'pine',
		'organism' : 'cat'
		}
		
newFavKey = sys.argv[1]

newFavValue = input("What is your favorite "+ newFavKey + " ?\n\n")

favs[newFavKey] = newFavValue

print(favs)

print('\nDone.\n')
```

9. Use a `for` loop to print out each key and value of the dictionary. 

```python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename:PS5.1.py

favs = {
		'book' : 'Lonesome Dove',
		'song' : 'Only Skin',
		'tree' : 'pine',
		'organism' : 'cat'
		}
		
for k, v in favs.items():
	print(k, ":", v)
	
print('\nDone.\n')
```

10. Write a script to find the intersection, difference, union, and symetrical difference between these two sets.

```
Set A = 3 14 15 9 26 5 35 9
Set B = 60 22 14 0 9
```

```python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename:PS5.1.py

setA = {3, 14, 15, 9, 26, 5, 35, 9}
setB = {60, 22, 14, 0, 9}

intersectionAB = setA & setB

print('The {} between Set A and Set B is {}'.format('intersection', intersectionAB))

differenceAB = setA - setB

print('The {} between Set A and Set B is {}'.format('difference', differenceAB))

unionAB = setA | setB

print('The {} between Set A and Set B is {}'.format('union', unionAB))

symDifferenceAB = setA ^ setB

print('The {} between Set A and Set B is {}'.format('symmetrical difference', symDifferenceAB))
```

11. If you create a set using a DNA sequence, what will you get back? Try it with this sequence:
```
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC
```

```
>>> setA = {aattggcc}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'aattggcc' is not defined
```

12.  Nucleotide Composition. Write a script that:
  - determines the unique characters in this sequence
```
GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA
```
  - iterate over each unique character and count the number found in the sequence
  - store each count in a dictionary. example: `nt_comp['A']=2`
  - when you are done counting each character calculate and report the nucleotide composition and the GC content.

```python
#!/usr/bin/env python3

#Filename: PS5.12.py
#Owner: Shasta Webb

mySeq = 'GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA'

uniqNT = list(set(mySeq))

myDict = {}

for NT in uniqNT:
    myDict[NT] = mySeq.count(NT)

countA = myDict['A']
countT = myDict['T']
countG = myDict['G']
countC = myDict['C']

print('A:', countA, '\nT:', countT, '\nG:', countG, '\nC:',  countC)

GCcontent = ((countG + countC)/len(mySeq))*100

print('GC content: {0:.2f} percent'.format(GCcontent))

print('\nDone.\n')
```


 13. Are you still committing your work?

```
$ git add *
$ git commit -m 'adding PS 5 scripts'
$ git push
```