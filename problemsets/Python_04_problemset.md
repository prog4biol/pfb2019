Python 4 Problem Set -- Lists and Loops
===================

1. For the next series of tasks about lists use the interpreter:  
	a.  Create a list of 5 of your favorite things.  
	b.  Use the `print()` function to print your list.  
	c.  Use the `print()` function to print out the middle element.  
	d.  Now replace the middle element with a different item, your favorite song, or song bird.  
	e.  Use the same print statement from b. to print your new list. Check out the differences.   
	f.  Add a new element to the end. [Read about append()](https://www.tutorialspoint.com/python/list_append.htm).  
	g.  Add a new element to the beginning. [Read about insert()](https://www.tutorialspoint.com/python/list_insert.htm).  
        h.  Add a new element somewhere other than the beginning or the end.  
        i.  Remove an element from the end. [Read about pop()](https://www.tutorialspoint.com/python/list_pop.htm).  
        j.  Remove an element from the beginning.  
        k.  Remove an element from somewhere other than the beginning or the end.  
	l.  Use `join` to create a string. Join the elements on ', ' 
	
2. Write a script that splits a string into a list. In your script: 
	- Save the string `sapiens, erectus, neanderthalensis` as a variable named `taxa`.
	- Print `taxa`.
	- Print `taxa[1]`, what do you get?
	- Print `type(taxa)`. What is it's type?
	- Split `taxa` into individual words and print the result of the split. (Think about the ', '.)
	- Store the result of `split` in a new variable named `species`.
	- Print `species`.
	- Print the `species[1]`, What do you get?
	- Print `type(species)`. What is it's type?
	- Sort the list alphabetically and print (hint: lookup the function `sorted()`). 
	- Sort the list by length of each string and print. (The shortest string should be first). [Check out documentation of the key argument](https://www.programiz.com/python-programming/methods/built-in/sorted).

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

4. Write a script that uses a `while` loop to print out the numbers 1 to 100.

5. Write a script that uses a `while` loop to calculate the [factorial](https://en.wikipedia.org/wiki/Factorial) of 1000. 

6. Iterate through each element of this list using a `for` loop: [101,2,15,22,95,33,2,27,72,15,52]
   - Print out only the values that are even (hint: use the modulus operator).
   
7. Sort the elements of the above list, then iterate through each element using a `for` loop and:
   - Print each element.
   - Calculate two cumulative sums, one of all the even values and one of all the odd values. 
   - Print only the final two sums. The output from your script should be:
   
   ```
   Sum of even numbers: 150 
   Sum of odds: 286
   ```
   
8. Write a script that uses `range()` in a `for` loop to print out every number between 0 and 99  
      - Modify your loop to print out every number between 1 and 100.
      
9. Create a new script that uses list comprehension to do the same thing as problem 8. (Use `range()` to print out every number between 1 and 100.)

10. Write a new script that takes the start and end values from the command line. If you call your script like this `count.py 3 10` it will print the numbers from 3 to 10.
      - Modify your script so that it will only print the number if it is odd.
      
11. Write a new script to create a list with the following data  `['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']`. Use a `for` loop to iterate through each element of this list and:
   - Print out each element.
   - Print out the length and the sequence, separated by a tab. The output should look like:
   
   ```
   14	ATGCCCGGCCCGGC
   25	GCGTGCTAGCAATACGATAAACCGG
   12	ATATATATCGAT
   8	ATGGGCCC
   ```
   
12. Use list comprehension to generate a list of tuples. The tuples should contain sequences and lengths from the previous problem. Print out the length and the sequence (i.e., "4\\tATGC\\n").  A list of tuples looks like this [(4,'ATGC'),(2,'GC')].

13. Modify the script from #11 so that you also print out the number (postion in the list) of each sequence (i.e., "1\\t4\\tACGT\\n")

14. Have you been commiting you work?

## Fun challenge problems! These are real scripts you might use in real life. You have already learned all you need to know to do each. If you don't have enough time in this session to complete, come back and try later.

1. Create a shuffled sequence ([Fisher-Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle))
    - Use a `for` loop to perform the following procedure N times (N = length of seq)
    - Select a random position A with `randrange()`
    - Select a random position B with `randrange()`
    - Exchange the letters at list indices A and B
    - Print the final shuffled sequence
    - Remember to test your code with test data. 

2. Calculate sequence identity: Start with 2 very similar DNA sequences. Use your favorites or use [Python_04.fasta](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_04.fasta)
    - Align with ClustalW, TCoffee, or some other web alignment application. 
    - Output should be in FASTA format.
    - Store (copy and paste) each aligned sequence, including dashes, as two separate string variables. 
    - Get rid of newlines (if any). Newline characters are not part of sequence!
    - Use a `for` loop with `range()` to compare each index for nucleotide differences.
    - Report percent identity of the two sequences.

3. A new Restriction Fragments script:
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
