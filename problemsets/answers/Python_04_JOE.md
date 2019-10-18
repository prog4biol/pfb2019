
#!/usr/bin/env python

# Problem 1

a. Create a list of 5 of your favorite things.
```
>>> favs = ["Pinkerton","Maple Dips", "Forests", "Euphoria", "Murakami"]
```
b. Use the print() function to print your list.
```
>>> print(favs)
['Pinkerton', 'Maple Dips', 'Forests', 'Euphoria', 'Murakami']
```
c. Use the print() function to print out the middle element.
```
>>> print(favs[2])
Forests
```
d. Now replace the middle element with a different item, your favorite song, or song bird.
```
>>> favs[2] = "King of Spain"
```
e. Use the same print statement from b. to print your new list. Check out the differences.
```
>>> print(favs)
['Pinkerton', 'Maple Dips', 'King of Spain', 'Euphoria', 'Murakami']
```
f. Add a new element to the end. Read about append().
```
>>> favs.append('Pesto')
```
g. Add a new element to the beginning. Read about insert().
```
>>> favs.insert(0, 'Banff')
```
h. Add a new element somewhere other than the beginning or the end.
```
>>> favs.insert(4, 'A well-made Manhattan')
```
i. Remove an element from the end. Read about pop().
```
>>> favs.pop()
'Pesto'
```
j. Remove an element from the beginning.
```
>>> favs.remove('Pinkerton')
```
k. Remove an element from somewhere other than the beginning or the end.
```
>>> favs.pop(2)
'Maple Dips'
```
l. Use join to create a string. Join the elements on ', '
```
>>> favs_string = ", ".join(favs)
>>> print(favs_string)
Banff, King of Spain, A well-made Manhattan, Euphoria, Murakami
```
# Problem 2
Write a script that splits a string into a list. In your script:

Save the string sapiens, erectus, neanderthalensis as a variable.
```
humans = "sapiens, erectus, neanderthalensis"
```
Print the string.
```
print(humans)
```
Split the string into individual words and print the result of the split. (Think about the ', '.). Store the resulting list in a new variable. Print the list.
```
split_humans = humans.split(', ')
print (split_humans)
```
Sort the list alphabetically and print (hint: lookup the function sorted()).
```
sorted_humans = sorted(split_humans)
print(sorted_humans)
```
Sort the list by length of each string and print. (The shortest string should be first). Check out documentation of the key argument.
```
print(sorted(split_humans, key=len))
```

# Problem 3
Using the Python interpreter, interrogate the difference between these two ways to copy a list. Careful! One of these is NOT what you might expect.
#### Method 1
Create a list. For example: my_list = ['a', 'bb', 'ccc']
```
>>> my_list = ['a', 'bb', 'ccc']
```
Make a copy using the = assignment operator: list_copy = my_list
```
>>> list_copy = my_list
```
Print the original list print(my_list)
```
>>> print(my_list)
['a', 'bb', 'ccc']
```
Alter the list_copy by adding a new element using append()
```
>>> list_copy.append('ddd')
```
Print the original list again print(my_list)
```
>>> print(my_list)
['a', 'bb', 'ccc', 'ddd']
```
#### Method 2
Create a list. For example: my_list2 = ['a', 'bb', 'ccc']
```
>>> my_list2 = ['a', 'bb', 'ccc']
```
Make a copy with the copy() method list_copy2 = my_list2.copy()
```
>>> list_copy2 = my_list2.copy()
```
Print the original list print(my_list2)
```
>>> print(my_list2)
['a', 'bb', 'ccc']
```
Alter the list_copy2 by adding a new element using append()
```
>>> list_copy2.append('ddd')
```
Print the original list again print(my_list2)
```
>>> print(my_list2)
['a', 'bb', 'ccc']
```
# Problem 4
Write a script that uses a while loop to print out the numbers 1 to 100.
```
x = 1
while x < 101:
	print (x)
	x += 1
```
# Problem 5
Write a script that uses a while loop to calculate the factorial of 1000.
```
x = 1
factorial = 1
while x < 1000:
	x += 1
	factorial *= x 
print(factorial)
```
# Problem 6
Iterate through each element of this list using a for loop: [101,2,15,22,95,33,2,27,72,15,52]

Print out only the values that are even (hint: use the modulus operator).
```
elements = [101,2,15,22,95,33,2,27,72,15,52]

for element in iter(elements):
	if element % 2 == 0:
		print(element)
```
# Problem 7
Sort the elements of the above list, then iterate through each element using a for loop and:
- Print each element.
- Calculate two cumulative sums, one of all the even values - and one of all the odd values.
- Print only the final two sums. The output from your script should be:
Sum of even numbers: 150 
Sum of odds: 286
```
elements = [101,2,15,22,95,33,2,27,72,15,52]
sorted_elements = sorted(elements)

even_sum = 0
odd_sum = 0

for element in sorted_elements:
	print (element)
	if element % 2 == 0:
		even_sum += element
	else:
		odd_sum += element
print ("Sum of even numbers :", even_sum, "\nSum of odds:", odd_sum)
```
# Problem 8
Write a script that uses range() in a for loop to print out every number between 0 and 99

- Modify your loop to print out every number between 1 and 100.
```
for item in range(0,100):
	print(item)
for item in range(1,101):
	print (item)
```
# Problem 9
Create a new script that uses list comprehension to do the same thing as problem 8. (Use range() to print out every number between 1 and 100.)
```
[print (item) for item in range(1,101)]
```
# Problem 10
Write a new script that takes the start and end values from the command line. If you call your script like this count.py 3 10 it will print the numbers from 3 to 10.
```
import sys

start = int(sys.argv[1])
end = int(sys.argv[2]) +1

[print (item) for item in range(start,end)]

[print (item) for item in range(start,end) if item % 2 != 0]
```

# Problem 11
Write a new script to create a list with the following data ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']. Use a for loop to iterate through each element of this list and:

- Print out each element.
- Print out the length and the sequence, separated by a tab. The output should look like:
14	ATGCCCGGCCCGGC
24	GCGTGCTAGCAATACGATAAACCGG
12	ATATATATCGAT
8	ATGGGCCC
```
elements =  ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for element in elements:
	element_length = len(element)
	print ("{:d}\t{:s}".format(element_length,element))
```
# Problem 12
Use list comprehension to generate a list of tuples. The tuples should contain sequences and lengths from the previous problem. Print out the length and the sequence (i.e., "4\tATGC\n").
```
DNAtuple = [(len(element), element) for element in elements]
for item in DNAtuple:
	print ("{}\t{}".format(item[0], item[1]))
```
# Problem 13 
Modify the script from #11 so that you also print out the number (postion in the list) of each sequence (i.e., "1\t4\tACGT\n")
```
DNAtuple = [(len(element), element) for element in elements]
counter = 1
for item in DNAtuple:
	print ("{} {}: {}\t{}".format("position", counter,item[0], item[1]))
	counter += 1
```
# Problem 14 
Have you been commiting you work?

# Fun challenge problems! These are real script is you might use in real life. You have already learned all you need to know to do each. If you don't have enough time in this session to complete, come back and try later.


# Fun Challenge 1
Create a shuffled sequence (Fisher-Yates shuffle)
- Use a for loop to perform the following procedure N times (N = length of seq)
- Select a random position A with randrange()
- Select a random position B with randrange()
- Exchange the letters at list indices A and B
- Print the final shuffled sequence
- Remember to test your code with test data.

```
import random

sequence = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG"

seq_list = list(sequence)

for iteration in range(len(sequence)):
	posA = random.randrange(len(sequence))
	posB = random.randrange(len(sequence))
	posAprime = posA
	seq_list[posA] = seq_list[posB]
	seq_list[posB] = seq_list[posAprime]
print(''.join(seq_list))	
```

# Fun Challenge  2
Calculate sequence identity: Start with 2 very similar DNA sequences. Use your favorites or use Python_04.fasta

- Align with ClustalW, TCoffee, or some other web alignment application.
- Output should be in FASTA format.
- Store (copy and paste) each aligned sequence, including dashes, as two separate string variables.
- Get rid of newlines (if any). Newline characters are not part of sequence!
- Use a for loop with range() to compare each index for nucleotide differences.
- Report percent identity of the two sequences.
```
seq1 = '-------------------------------------------------------------------------------------AGCACCCTCCCACCTCATCCCACCCTTCTGATCTCAATCCAACGTCGCATCTCCACCGTCTCGC-----GGATCGACCCAGCGAAGTCC----CTCCCGCCCCCAAAGTCCC----------CCAAATCTTGCAGTTCCCTCCTAAATCCTCCCCATATAAACCAACCCCCCGCCCTCAGATCCCTAATC-CCATCGCA--AGCATCAGACTCCCTCCAAAGCAGGCAGCAGCTCCTCTTCTTCCTAATCACACTATCTCGGAGAGGAGCGGCCATGTCTGGGCGCGACAAGGGCGGCAAGGGGCTGGGCAAGGGCGGCGCCAAGCGGCACCGGAAGGTCCTCCGCGACAACATCCAGGGCATCACCAAGCCGGCGATCCGGAGGCTGGCCAGGAGGGGCGGCGTGAAGCGCATCTCCGGCCTCATCTACGAGGAGACCCGCGGCGTCCTCAAGATCTTCCTCGAGAACGTCATCCGCGACGCCGTCACCTACACCGAGCACGCCCGCCGCAAAACCGTCACCGCCATGGACGTCGTCTACGCGCTCAAGCGCCAGGGCCGCACCCTCTACGGCTTCGGAGGCTAGATTTGTGTGGTGAAGCAACTTCCTCGTTTGCTCTGTGATCTGTGCTGTCGTAGATGAGATTTACTGATTTGGCGTGCGCC---GGTTGTATTCTGTCATGGGGTTCAGTGGGCTGTGTAATACCTTGCTCTGTACTTCTGTTCAA----TGCAATCACTTCTATTC-------------------TGAA-----------------'

seq2 = 'TCTAGAGATGGCGCCATTTGATTCCAGCAGCCACAAAGCACTAGAACAATCGATGCTAAGAGGTGACAGGAAAAACAGGCTGCAAAGACCCAGACAATGGAATGCAGCGGTGGTCAGCCTAAAACACTGTAGAAGGGCAAGATGAGCTGAGTAATTTTTAACTGGGCATCATTTTTAGAAACTGGAGTTTAAGTACCCCCTTTTCCATTTTTTCCTGAAGTCGTGGGCAGGGCGCAAGGTCTGTGAATCGGCCGACCGGATGCAGCTGGTGTGGAGAGTTCCCAATCAGGTCCGATTTATTACTATATAAAGTACTGCTGC--GAGGCTTGCCGTGTTGCATTTTGTTTAGTACAAGACATGTCTGGGCGCGGCAAAGGCGGGAAGGGTCTGGGCAAAGGAGGCGCTAAGCGCCACCGCAAAGTTCTGCGCGACAACATTCAGGGCATCACCAAGCCCGCCATCCGACGCCTGGCACGGCGTGGAGGCGTTAAGCGCATCTCAGGCCTTATATACGAGGAGACACGCGGAGTTCTTAAAGTGTTTTTGGAGAATGTAATCCGCGATGCAGTTACCTACACGGAGCACGCCAAACGCAAGACAGTCACAGCCATGGACGTGGTTTACGCGCTCAAGCGCCAGGGCCGCACCCTGTATGGCTTTGGCGGCTGAGTGTTTTACTTACTTACACGGTTCCTCAAAGGCCCTTCTCAGGGCCACCCATGAAGTCTGTGAAAGAGCTGTAGACTAAAGATAGTTAATTTCTTAAGAAC-----ACTTAAACGTATGGCAGTTTTGGCAAATTAGCGATTCCACATAAGCAGTCGCTGAAGTTTGAGGTTCGGTGCCCCTTTCAGCATTACTTAGTGGTTAAAA'

seq1 = list(seq1)
seq2 = list(seq2)

diffs = 0

for position in range(len(seq1)):
	if seq1[position] != seq2[position]:
		diffs +=1
	else:
		continue

print("{:.3f}".format(diffs/len(seq1)))
```

# Fun Challenge 3

A new Restriction Fragments script:
- Find EcoRI in this DNA sequence
```GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC```
- replace the EcoRI site 'GAATTC' with this 'G^AATTC'
- split the new formatted sequence on the cut sites, store the resulting fragments in a list
- iterate over each fragment and report
- the start position in the original sequence
- the end postion in the orginal sequence
- the length of each fragemnt
- sort the fragments by length and print out as they would appear on a agrose gel. (big to little)
```
sequence = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC'

EcoRI = 'GAATTC'

seq_cut = sequence.replace(EcoRI, 'G^AATTC')
fragments = seq_cut.split('^')

prior_fragment = 0
counter = 1
for fragment in fragments:
	start = prior_fragment + 1
	end = start + len(fragment) - 1
	length = len(fragment)
	print ("{}{}\t{} {}\t{} {}\t{} {}".format("Fragment",counter,"start position:",start,"end position:", end, "length:",length))
	prior_fragment += length
	counter +=1
```






