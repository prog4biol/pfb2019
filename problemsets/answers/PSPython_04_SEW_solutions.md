Python 4 Problem Set -- Lists and Loops
===================

1. For the next series of tasks about lists use the interpreter:  
  a.  Create a list of 5 of your favorite things.  

  ```python
  >>> myList = ['cats', 'bikes', 'bread', 'Python', 'trees']
  ```
  b. Use the print() function to print your list.
  
  ```python
  >>> print(myList)
  ```
  
  c.  Use the `print()` function to print out the middle element.  

```python
>>> print(myList[2])
```

  d.  Now replace the middle element with a different item, your favorite song, or song bird. 

```python
>>> myList[2] = 'warbler'
```
  e.  Use the same print statement from b. to print your new list.  

```python
>>> print(myList)
```
  f.  Add a new element to the end. [Read about append()](https://www.tutorialspoint.com/python/list_append.htm). 

```python
>>> myList.append('mountains')
```
  g.  Add a new element to the beginning. [Read about insert()](https://www.tutorialspoint.com/python/list_insert.htm).  

```python
>>> myList.insert(0, 'summer')
```

  h.  Add a new element somewhere other than the beginning or the end.  

```python
>>> myList.insert(4, 'tacos')
```
  i.  Remove an element from the end. [Read about pop()](https://www.tutorialspoint.com/python/list_pop.htm).  

```python
>>> myList.pop()
```

  j.  Remove an element from the beginning.

```python
>>> myList.pop(0)
```

  k.  Remove an element from somewhere other than the beginning or the end.  

```python
>>> myList.pop(3)
```
  l.  Use `join` to create a string. Join the elements on ', ' 

```python
>>> myString = ''
>>> myString = myString.join(myList)
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
#!/usr/bin/env python3

import sys

myString = 'sapiens, erectus, neanderthalensis'

print(myString)

myList = myString.split(', ') #splitting string on the comma and the space

print(sorted(myList)) #sorting my list; default is alphabetical

print(sorted(myList, key = len)) #sorting my list by length; must tell sorted to use length
```

3. Using the Python interpreter, interrogate the difference between these two ways to copy a list. Careful! One of these is NOT what you might expect. 
   - Method 1
     - Create a list. For example: `my_list = ['a', 'bb', 'ccc']`
     - Make a copy using the `=` assignment operator:  `list_copy = my_list`
     - Print the original list `print(my_list)`
     - Alter the `list_copy` by adding a new element using `append()`
     - Print the original list again `print(my_list)`

```python
>>> myList = ['a', 'b', 'c']
>>> list_copy = myList
>>> print(myList)
['a', 'b', 'c']
>>> list_copy.append('d')
>>> print(myList)
['a', 'b', 'c', 'd']
```

   - Method 2  
     - Create a list. For example: `my_list2 = ['a', 'bb', 'ccc']`  
     - Make a copy with the copy() method `list_copy2 = my_list2.copy()`  
     - Print the original list `print(my_list2)`
     - Alter the `list_copy2` by adding a new element using `append()`   
     - Print the original list again `print(my_list2)` 

```python
>>> myList2 = ['a', 'bb', 'ccc']
>>> list_copy2 = myList2.copy()
>>> print(myList2)
['a', 'bb', 'ccc']
>>> list_copy2.append('ddd')
>>> print(list_copy2)
['a', 'bb', 'ccc', 'ddd']
>>> print(myList2)
['a', 'bb', 'ccc']
```

4. Write a script that uses a `while` loop to print out the numbers 1 to 100

```python
#! usr/bin/env python3

#Owner: Shasta Webb
#Filename: 4.1.py
#Description: Write a script that uses a while loop to print out the numbers 1 to 100.

count = 0

while count < 101:
	if count > 0:
		print(count)
	count += 1

print("\n\nDone.\n")
```

5. Write a script that uses a `while loop` to calculate the [factorial](https://en.wikipedia.org/wiki/Factorial) of 1000.  

```python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 4.5.py
#Description: Write a script that uses a while loop to calculate the factorial of 1000.

count = 1
factorial = 1
while count < 1001:
	factorial = factorial * count
	count += 1

print("The factorial of 1000 is:", factorial)
print("\n\nDone.")
```
6. Iterate through each element of this list using a `for` loop: [101,2,15,22,95,33,2,27,72,15,52]

   - Print out only the values that are even (use modulus operator).

```python
#! usr/bin/env/ python3 

#Owner: Shasta Webb
#Filename: 4.6.py
#Description: Iterate through each element of this list using a for loop: [101,2,15,22,95,33,2,27,72,15,52]. Print out only the values that are even (use modulus operator).

nums = [101,2,15,22,95,33,2,27,72,15,52]

for num in nums:
	if num % 2 == 0:
		print(num)

print("\nDone.\n")
```

7. Sort the elements of the above list, then iterate through each element using a `for` loop and:
   - Print each element.
   - Calculate two cumulative sums, one of all the even values and one of all the odd values. 
   - Print the only the final two sums.

```python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 4.7.py
#Description: Sort the elements of the above list, then iterate through each element using a for loop and: Print each element, Calculate two cumulative sums, one of all the even values and one of all the odd values, Print the only the final two sums.

nums = [101,2,15,22,95,33,2,27,72,15,52]
evens = []
odds = []

for num in sorted(nums):
	print(num)
	if num % 2 == 0:
		evens.append(num)
	else:
		odds.append(num)

print("Sum of numbers:", sum(nums) + "\nSum of even numbers:", sum(evens) + "\nSum of odds:", sum(odds))

print("\n\nDone.\n")
```

8. Write a script that uses `range()` in a `for` loop to print out every number between 0 and 99  
      - Modify your loop to print out every number bewteen 1 and 100
      - Create a new script that uses list comprehension to do the same, uses range to print out every number bewteen 1 and 100

```python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 4.8.py
#Description: Write a script that uses range() in a for loop to print out every number between 0 and 99

#Range will consider the number in the 0th position, so if you want 1-98 (between 0 and 99) your range is 1,99. If want 0-99, your range is 0,100.

for i in range(1,99):
	print(i)

print("\nDone.\n")
```

9. Write a new script that takes the start and end values from the command line. If you call your script like this `count.py 3 10` it will print the numbers from 3 to 10.

      - Modify your script so that it will only print the number if it is odd.

```python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 4.9.py
#Description: Rewrite the script to take to start and end values from the command line. If you call your script like this count.py 3 10 it will print the numbers from 3 to 10.

#note: To ensure that the code interprets command line arguments as integers, you have to specify that. Otherwise the default is string.

import sys

startNum = int(sys.argv[1])
endNum = int(sys.argv[2]) + 1

for i in range(startNum,endNum):
	print(i)

print("\nDone.\n")
```
10. Make a list with the following data  `['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']`. Use a `for` loop to iterate through each element of this list and:
  - Print out each element
  - Print out the length and the sequence i.e., "4\\tATGC\\n"

  ```python
  #! usr/bin/env/ python3
  
  #Owner: Shasta Webb
  #Filename: 4.10.py
  #Description: Make a list with the following data ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']. Use a for loop to iterate through each element of this list and: Print out each element. Print out the length and the sequence i.e., "4\tATGC\n"
  
  seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
  
  for seq in seqs:
  	print(len(seq), "\t", seq, "\n")
  
  print("Done.")
  ```

11. Use list comprehension to generate a list of tuples of sequences and lengths with the list from #10. Print out the length and the sequence i.e., "4\\tATGC\\n".

```python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 4.11.py
#Description: Use list comprehension to generate a list of tuples of sequences and lengths with the list from #10. Print out the length and the sequence i.e., "4\tATGC\n".

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

lengths = [(len(seq), seq) for seq in seqs] 

for length in lengths:
	print(length[0], "\t", length[1])


print("\nDone.\n")
```

12. Modify the script from #11 so that you also print out the number (postion in the list) of each sequence i.e. "1\\t4\\tACGT\\n"

```python
#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 4.12.py
#Description: Modify the script from #11 so that you also print out the number (postion in the list) of each sequence i.e. "1\t4\tACGT\n"

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

lengths = [(seqs.index(seq), len(seq), seq) for seq in seqs] 

for length in lengths:
	print(length[0], "\t", length[1], "\t", length[2])


print("\nDone.\n")
```

12. Have you been commiting you work?

```
$ git add myScript.py
$ git commit -m 'adding PS4 problems'
$ git push
```


## Fun challenge problems! These are real scripts you might use in real life. You have already learned all you need to know to do each. If you don't have enough time in this session to complete, come back and try later.

1. Create a shuffled sequence ([Fisher-Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle))
    - Use a `for` loop to perform the following procedure N times (N = length of seq)
    - Select a random position A with `randrange()`
    - Select a random position B with `randrange()`
    - Exchange the letters at list indices A and B
    - Print the final shuffled sequence
    - Remember to test your code with test data. 

```python
#!/usr/bin/env python    

import random
    
sequence = 'GCGTGCTAGCAATACGATAAACCGG'

# Strings are immutable objects, which means you cannot modify them in place.
# Instead convert the immutable string to a mutable list of characters:

shuffled = list(sequence)  # converts a string to a list

N = len(sequence)
for iteration in range(N):
	rand_pos_A = random.randrange(N)
	rand_pos_B = random.randrange(N)
    
# Python allows us to swap two variables in a single expression:
# (X, Y) = (Y, X)

(shuffled[rand_pos_A], shuffled[rand_pos_B]) = (shuffled[rand_pos_B], shuffled[rand_pos_A])

print("Original: {:s}".format(sequence))
print("Shuffled: {:s}".format(''.join(shuffled)))
```

2. Calculate sequence identity: Start with 2 very similar DNA sequences. Use your favorites or use [Python_04.fasta](https://raw.githubusercontent.com/srobb1/pfb2018/master/files/Python_04.fasta)
    - Align with ClustalW, TCoffee, or some other web alignment application. 
    - Output should be in FASTA format.
    - Store (copy and paste) each aligned sequence, including dashes, as two separate string variables. 
    - Get rid of newlines (if any). Newline characters are not part of sequence!
    - Use a `for` loop with `range()` to compare each index for nucleotide differences.
    - Report percent identity of the two sequences.

```python
#!/usr/bin/env python3

seq1 = 'CCTCCAAAGCAGGCAGCAGCTCCTCTTCTTCCTAATCACACTATCTCGGA'
seq2 = 'ATTACTATATAAAGTACTGCTGCGAGGCTTGCCG--TGTTGCATTTTGTT'

matches = 0 
nonMatches = 0 

for position in range(len(seq1)):
    if seq1[position] == seq2[position]:
        matches += 1
    else:
        nonMatches += 1

print('Percent identity between {} and {} is {:.2f}%'.format(seq1, seq2, (matches/(matches + nonMatches))*100))
```

4. A new Restriction Fragments script:

   - Find [EcoRI](https://www.neb.com/products/r0101-ecori#Product%20Information) in this DNA sequence
```
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC
```
   - replace the EcoRI site 'GAATTC' with this 'G^AATTC'
   - split the new formatted sequence on the cut sites, store the resulting fragments in a list
   - iterate over each fragment and report
      - the start position in the original sequence
      - the end postion in the orginal sequence
      - the length of each fragemnt
   - sort the fragments by length and print out as they would appear on a agrose gel. (big to little)

```

```