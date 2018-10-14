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




10. ADD/COMMIT/PUSH
