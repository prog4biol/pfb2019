Python 3 Problem Set
===================
1. What are considered sequences in Python?
2. What is the length of the following DNA string? Is this DNA string a Python sequence?
```
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG
```

3. Write a script that calculates the AT content of the DNA string found above. AT content is the proportion of bases that are either A or T. You will need to use some mathmatical functions as well as a python function. It is ALWAYS a good idea to test your code with test data. For example, the below sequence is long and you don't know for sure how many As and Ts are present. Test your codee with a DNA string that you KNOW the correct answer. In AATTGGCCA you know you have 3 As and 2 Ts.
	- Now add in lines of code to calculate GC content of the above DNA string. Run with test data first!!

4. Write a new script that prints out the reverse complement of the above DNA string. [Hint for reverse](http://bfy.tw/EXap)
	
>
> ```
>  Original Sequence  5'ATGCAGGGGAAACATGATTCAGGAC 3'  
>  Complement         3'TACGTCCCCTTTGTACTAAGTCCTG 5'  
>  Reverse Complement 5'GTCCTGAATCATGTTTCCCCTGCAT 3'  
> ```


5. Make sure to commit your changes along the way. You can wait until the end to push them to your remote repo, if you like, or you can do it now. It is probably smart to commit after each problem set question. 

6. Write a script to find the start position of an [EcoRI](https://www.neb.com/products/r0101-ecori#Product%20Information) site in the above DNA sequence. Remember DNA sequences start with a 1 and a python string starts with a 0. Run with test data first.
	- What is the end position of the EcoRI site?
	- Use [string formating](https://github.com/prog4biol/pfb2018/blob/master/README.md#string-formatting) to print out the start and end of the EcoRI site.

7. For the next series of tasks about lists use the interpreter:  
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
	
8. Write a script that splits a string into a list.
	- the string `sapiens, erectus, neanderthalensis`
	- print the string before you split. 
	- split the string and print the result of the split. Think about the ', '.
	- store the resulting list in a new variable
	- print the list
	- sort the list alphbetically and print
	- sort the list by length and print. [Check out documentation of the key argument](https://www.programiz.com/python-programming/methods/built-in/sorted).


9. Interrogate the difference between these two ways to copy a list. Both are not correct. 
  - use the assignment operator
     - create a list, for exampale: `my_list = ['a', 'bb', 'ccc']`
     - make a copy   `list_copy = my_list`
     - print the original list `print(my_list)`
     - alter the list_copy after the "copy" by adding a new element to list_copy
     - print the original list again `print(my_list)`
   - use the copy() method:  
     - create a list, for exampale: `my_list2 = ['a', 'bb', 'ccc']`  
     - make a copy with the copy() method `list_copy2 = my_list2.copy()`  
     - print the orginal list  
     - alter list_copy2  
     - print the orginal list   


10. ADD/COMMIT/PUSH
