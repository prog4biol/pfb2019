Python 4 Problem Set -- Lists and Loops
===================

1. For the next series of tasks about lists use the interpreter:  
	a.  Create a list of 5 of your favorite things.
	```python
	my_favorites=['Music', 'Movies', 'Coding', 'Biology', 'Python']
	```

	b.  Use the `print()` function to print your list.  
	```python
	print(my_favorites)
	```
	c.  Use the `print()` function to print out the middle element.
	```python
	print(my_favorites[2])
	```
	d.  Now replace the middle element with a different item, your favorite song, or song bird.  
	```python
	my_favorites[2]='European robin'
	```
	e.  Use the same print statement from b. to print your new list. Check out the differences.   
	```python
	print(my_favorites)
	```
	f.  Add a new element to the end. [Read about append()](https://www.tutorialspoint.com/python/list_append.htm).  
	```python
	my_favorites.append('Monkeys')
	```
	g.  Add a new element to the beginning. [Read about insert()](https://www.tutorialspoint.com/python/list_insert.htm).  
	```python
	my_favorites.insert(0, 'Evolution')
	```
        h.  Add a new element somewhere other than the beginning or the end.
				```python
				my_favorites.insert(3, 'Coffee')
				```
        i.  Remove an element from the end. [Read about pop()](https://www.tutorialspoint.com/python/list_pop.htm).
				```python
				my_favorites.pop()
				```
        j.  Remove an element from the beginning.  
				```python
				my_favorites.pop(0)
				```
        k.  Remove an element from somewhere other than the beginning or the end.  
				```python
				my_favorites.pop(3)
				```
	l.  Use `join` to create a string. Join the elements on ', '
	```python
	my_favorite_string=','.join(my_favorites)
	print(my_favorite_string)
	```

2. Write a script that splits a string into a list. In your script:
	- Save the string `sapiens, erectus, neanderthalensis` as a variable.
	- Print the string.
	- Split the string into individual words and print the result of the split. (Think about the ', '.)
	- Store the resulting list in a new variable.
	- Print the list.
	- Sort the list alphabetically and print (hint: lookup the function `sorted()`).
	- Sort the list by length of each string and print. (The shortest string should be first). [Check out documentation of the key argument](https://www.programiz.com/python-programming/methods/built-in/sorted).
```python
hominins='sapiens, erectus, neanderthalensis'
print(hominins)
hominin_individuals=hominins.split(',')
print('hominin_individuals')
hominin_individuals=sorted(hominin_individuals)
print(hominin_individuals)
hominin_individuals=sorted(hominin_individuals, key=len)
print(hominin_individuals)
```
3. Using the Python interpreter, interrogate the difference between these two ways to copy a list. Careful! One of these is NOT what you might expect.
   - Method 1
     - Create a list. For example: `my_list = ['a', 'bb', 'ccc']`
     - Make a copy using the `=` assignment operator:  `list_copy = my_list`
     - Print the original list `print(my_list)`
     - Alter the `list_copy` by adding a new element using `append()`
     - Print the original list again `print(my_list)`
   - Method 2  
     - Create a list. For example: `my_list2 = ['a', 'bb', 'ccc']`  
     - Make a copy with the copy() method `list_copy2 = my_list2.copy()`  
     - Print the original list `print(my_list2)`
     - Alter the `list_copy2` by adding a new element using `append()`   
     - Print the original list again `print(my_list2)`

		 ```python
		 >>>my_list = ['a', 'bb', 'ccc']
		 >>>list_copy = my_list
		 >>>print(my_list)
		 ['a', 'bb', 'ccc']
		 >>>list_copy
		 >>>list_copy.append('dddd')
		 >>>print(my_list)
		 ['a', 'bb', 'ccc', 'dddd']

		 ```
4. Write a script that uses a `while` loop to print out the numbers 1 to 100.
```python
counter=1
while counter<=100:
	print(counter)
	counter+=1

```
5. Write a script that uses a `while` loop to calculate the [factorial](https://en.wikipedia.org/wiki/Factorial) of 1000.
```python
incrementer=1
factorial=1
while incrementer<=1000:
	factorial*=incrementer
	incrementer+=1

print("The factorial of 1000 is {}".format(factorial))

```
6. Iterate through each element of this list using a `for` loop: [101,2,15,22,95,33,2,27,72,15,52]
   - Print out only the values that are even (hint: use the modulus operator).
	 ```python
	 for i in [101,2,15,22,95,33,2,27,72,15,52]:
		 if i%2==0:
			 print(i)
	 ```
7. Sort the elements of the above list, then iterate through each element using a `for` loop and:
   - Print each element.
   - Calculate two cumulative sums, one of all the even values and one of all the odd values.
   - Print only the final two sums. The output from your script should be:

   ```
   Sum of even numbers: 150
   Sum of odds: 286
   ```
	 ```python
numbers=[101,2,15,22,95,33,2,27,72,15,52]
numbers=sorted(numbers)
even_sums=0
odd_sums=0
for number in numbers:
    if number%2==0:
        even_sums+=number
    else:
        odd_sums+=number
    print(number)
print("Sum of even numbers: {}".format(even_sums))
print("Sum of odds: {}".format(odd_sums))


	 ```
8. Write a script that uses `range()` in a `for` loop to print out every number between 0 and 99  
      - Modify your loop to print out every number between 1 and 100.
			```python
for i in range(100):
    print(i)

for i in range(1,101):
    print(i)				


			```
9. Create a new script that uses list comprehension to do the same thing as problem 8. (Use `range()` to print out every number between 1 and 100.)
```python
print ([i for i in range(1,101)])
```
10. Write a new script that takes the start and end values from the command line. If you call your script like this `count.py 3 10` it will print the numbers from 3 to 10.
      - Modify your script so that it will only print the number if it is odd.
			```python
			#!/usr/bin/env python3
			import sys
			lower=int(sys.argv[1])
			upper=int(sys.argv[2])

			for i in range(lower, upper+1):
				print(i)

			for i in range(lower, upper+1):
				if i%2 != 0:
					print(i)
			```
11. Write a new script to create a list with the following data  `['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']`. Use a `for` loop to iterate through each element of this list and:
   - Print out each element.
   - Print out the length and the sequence, separated by a tab. The output should look like:

   ```
   14	ATGCCCGGCCCGGC
   24	GCGTGCTAGCAATACGATAAACCGG
   12	ATATATATCGAT
   8	ATGGGCCC
   ```
	 ```python

sequences=['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for sequence in sequences:
	print("{}\t{}".format(len(sequence), sequence))
	 ```
12. Use list comprehension to generate a list of tuples. The tuples should contain sequences and lengths from the previous problem. Print out the length and the sequence (i.e., "4\\tATGC\\n").
```python
sequences=['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
seq_lengths=[(seq, len(seq)) for seq in sequences]
print(seq_lengths)

```
13. Modify the script from #11 so that you also print out the number (postion in the list) of each sequence (i.e., "1\\t4\\tACGT\\n")
```python
sequences=['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for index, sequence in enumerate(sequences):
	print("{}\t{}\t{}".format(len(sequence), index+1, sequence))
```
14. Have you been commiting you work?

## Fun challenge problems! These are real scripts you might use in real life. You have already learned all you need to know to do each. If you don't have enough time in this session to complete, come back and try later.

1. Create a shuffled sequence ([Fisher-Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle))
    - Use a `for` loop to perform the following procedure N times (N = length of seq)
    - Select a random position A with `randrange()`
    - Select a random position B with `randrange()`
    - Exchange the letters at list indices A and B
    - Print the final shuffled sequence
    - Remember to test your code with test data
```python
from random import randrange
DNA='ATGGGCCC'

seq=list(DNA)
seq_len=len(seq)

for i in range(seq_len):
	A=randrange(seq_len)
	B=randrange(seq_len)
	seq[A], seq[B] = seq[B], seq[A]
print("".join(seq))
```

2. Calculate sequence identity: Start with 2 very similar DNA sequences. Use your favorites or use [Python_04.fasta](https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/Python_04.fasta)
    - Align with ClustalW, TCoffee, or some other web alignment application.
    - Output should be in FASTA format.
    - Store (copy and paste) each aligned sequence, including dashes, as two separate string variables.
    - Get rid of newlines (if any). Newline characters are not part of sequence!
    - Use a `for` loop with `range()` to compare each index for nucleotide differences.
    - Report percent identity of the two sequences.
```python
seq_A='''AGC----ACCCTCCCACCTCATCCCACCCTTCTGATCTC------------AATCCAACGTCGCATCTCCACCGTCTCGC
G-GATCGACCCAGCGAAGTC----CCTC--CCG-----------------------------------------------
------------------------CCCCCAAAGTCCCCCAAATCTTGCAGTTCCCTCCTAAATCCTCCCCAT--------
----ATAAACCAACCCCCCGCCCTCAGATCCCT-AATCCCATCGCAAGCA--TCAGACTCCCTCCAAAGCAGGCAGCAGC
TCCTCTTCTTC-CTAATCACACTATCTCGGAGAGGAGCGGCCATGTCTGGGCGCGACAAGGGCGGCAAGGGGCTGGGCAA
GGGCGGCGCCAAGCGGCACCGGAAGGTCCTCCGCGACAACATCCAGGGCATCACCAAGCCGGCGATCCGGAGGCTGGCCA
GGAGGGGCGGCGTGAAGCGCATCTCCGGCCTCATCTACGAGGAGACCCGCGGCGTCCTCAAGATCTTCCTCGAGAACGTC
ATCCGCGACGCCGTCACCTACACCGAGCACGCCCGCCGCAAAACCGTCACCGCCATGGACGTCGTCTACGCGCTCAAGCG
CCAGGGCCGCACCCTCTACGGCTTCGGAGGCTAGATTTGTGTGGTGAAGCAACTTCCTCGTTTGCTCTGTG------ATC
TGTGCTGTCGTAGATGAGATTTACTGATTTGGCGTGCGCCGGTTGTATTCTGTCATGGGGTTCAGTGGGCTG--TGTAAT
A-----------------------------------------CCTTGCTCTGTACTTCTGTTCAATGCAATCACTTCTAT
TCTGAA'''
seq_B='''TCTAGAGATGGCGCCATTTGATTCCAGCAGCCACAAAGCACTAGAACAATCGATGCTAAGAGGTGACAGGAAAAACAGGC
TGCAAAGACCCAGACAATGGAATGCAGCGGTGGTCAGCCTAAAACACTGTAGAAGGGCAAGATGAGCTGAGTAATTTTTA
ACTGGGCATCATTTTTAGAAACTGGAGTTTAAGTACCCC--CTTTTCCATTTTTTCCTGAAGTCGTGGGCAGGGCGCAAG
GTCTGTGAATCGGCCGACCGGATGCAGCTGGTGTGGAGAGTTCCCAATCAGGTCCGATTTATTACTATATAAAGTACTGC
TGCGAGGCTTGCCGTGTT---GCATTTTGTTTAGTACAAGACATGTCTGGGCGCGGCAAAGGCGGGAAGGGTCTGGGCAA
AGGAGGCGCTAAGCGCCACCGCAAAGTTCTGCGCGACAACATTCAGGGCATCACCAAGCCCGCCATCCGACGCCTGGCAC
GGCGTGGAGGCGTTAAGCGCATCTCAGGCCTTATATACGAGGAGACACGCGGAGTTCTTAAAGTGTTTTTGGAGAATGTA
ATCCGCGATGCAGTTACCTACACGGAGCACGCCAAACGCAAGACAGTCACAGCCATGGACGTGGTTTACGCGCTCAAGCG
CCAGGGCCGCACCCTGTATGGCTTTGGCGGCTGAGT------GTTTTACTTACTTACACGGTTCCTCAAAGGCCCTTCTC
AGGGCCACCCATGAAGTCTGTGAAAGAGCTGTAGACTAAAGATAGTT-AATTTCTTAAG-AACACTTAAACGTATGGCAG
TTTTGGCAAATTAGCGATTCCACATAAGCAGTCGCTGAAGTTTGAGGTTCGGTGCCCCTT-TCAG--CATTACTTAGTGG
TTAAAA'''
len(seq_A)
len(seq_B)
#get rid of newlines
seq_A=seq_A.replace("\n","")
seq_B=seq_B.replace("\n","")

#counters for identical and non-identicatl positions:
identical=0
different=0

for i in range(len(seq_A)):
	if seq_A[i] == seq_B[i]:
		identical+=1
	else:
		different+=1
print(identical)
print(different)
print("The sequences are {0:.2f}% identical".format(identical/(identical+different)*100))
```
