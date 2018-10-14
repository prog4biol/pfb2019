Python 4 Problem Set -- Lists and Loops
===================

1. For the next series of tasks about lists use the interpreter:  
	a.  Create a list of 5 of your favorite things.  
	b.  Use the `print()` function to print out the middle element.  
	c.  Now replace the middle element with a different item, your favorite song, or song bird.  
	d.  Use the same print statement from b. to print your new list.  
	e.  Add a new element to the end. [Read about append()](https://www.tutorialspoint.com/python/list_append.htm).  
	f.  Add a new element to the beginning. [Read about insert()](https://www.tutorialspoint.com/python/list_insert.htm).  
        g.  Add a new element somewhere other than the beginning or the end.  
        h.  Remove an element from the end. [Read about pop()](https://www.tutorialspoint.com/python/list_pop.htm).  
        i.  Remove an element from the beginning.  
        j.  Remove an element from somewhere other than the beginning or the end.  
	k.  Use `join` to create a string. Join the elements on ', ' 
	

2. Write a script that:
        - splits a string into a list.
	- the string `sapiens, erectus, neanderthalensis`
	- print the string before you split. 
	- split the string and print the result of the split. Think about the ', '.
	- store the resulting list in a new variable
	- print the list
	- sort the list alphbetically and print
	- sort the list by length and print. [Check out documentation of the key argument](https://www.programiz.com/python-programming/methods/built-in/sorted).


3. Interrogate the difference between these two ways to copy a list. Both are not correct. 
  - use the assignment operator
     - create a list, for exampale: `my_list = ['a', 'bb', 'ccc']`
     - make a copy   `list_copy = my_list`
     - print the original list `print(my_list)`
     - alter the list_copy after the "copy" by adding a new element to list_copy
     - print the original list again `print(my_list)`
   - use the copy() method:  
     - create a list, for exampale: `my_list2 = ['a', 'bb', 'ccc']`  
     - make a copy with the copy() method `list_copy2 = my_list2.copy()`  
     - print the original list  
     - alter list_copy2  
     - print the original list   

4. Write a script that uses a `while` loop to print out the numbers 1 to 100
5. Write a script that uses a `while loop` to calculate the [factorial](https://en.wikipedia.org/wiki/Factorial) of 1000.  
6. Iterate through each element of this list using a `for` loop: [101,2,15,22,95,33,2,27,72,15,52]
   - Print out only the values that are even (use modulus operator).
7. Sort the elements of the above list, then iterate through each element using a `for` loop and:
   - Print each element.
   - Calculate two cumulative sums, one of all the even values and one of all the odd values. 
   - Print the only the final two sums.
8. Write a script that uses `range()` in a `for` loop to print out every number between 0 and 99  
      - Modify your loop to print out every number bewteen 1 and 100
      - Create a new script that uses list comprehension to do the same, uses range to print out every number bewteen 1 and 100
9. Write a new script that takes the start and end values from the command line. If you call your script like this `count.py 3 10` it will print the numbers from 3 to 10.
      - Modify your script so that it will only print the number if it is odd.
10. Make a list with the following data  `['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']`. Use a `for` loop to iterate through each element of this list and:
   - Print out each element
   - Print out the length and the sequence i.e., "4\\tATGC\\n"
11. Use list comprehension to generate a list of tuples of sequences and lengths with the list from #10. Print out the length and the sequence i.e., "4\\tATGC\\n".
12. Modify the script from #11 so that you also print out the number (postion in the list) of each sequence i.e. "1\\t4\\tACGT\\n"

13. Have you been commiting you work?


## Fun Challange Problems. These are real scripts you might use in real life. You have already learned all you need to know to do each. If you don't have enough time in this session to complete, come back and try later.

1. Create a shuffled sequence ([Fisher-Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle))
    - Use a for loop to perform the following procedure N times (N = length of seq)
    - Select a random position A with randrange()
    - Select a random position B with randrange()
    - Exchange the letters at list indices A and B
    - Print the final shuffled sequence
    - Remember to test your code with test data. 

2. Calculate sequence identity: Start with 2 very similar DNA sequences. Use your favorites or use [Python_04.fasta](https://raw.githubusercontent.com/srobb1/pfb2018/master/files/Python_04.fasta)
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


16. Have you been commiting you work?
