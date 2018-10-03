Python 4 Problem Set
===================

1. Write a script that uses a `while` loop to print out the numbers 1 to 100
2. Write a script that uses a `while loop` to calculate the [factorial](https://en.wikipedia.org/wiki/Factorial) of 1000.  
3. Iterate through each element of this list using a `for` loop: [101,2,15,22,95,33,2,27,72,15,52]
   - Print out only the values that are even (use modulus operator).
4. Sort the elements of the above list, then iterate through each element using a `for` loop and:
   - Print each element.
   - Calculate two cumulative sums, one of all the even values and one of all the odd values. 
   - Print the only the final two sums.

5. Write a script that uses `range()` in a `for` loop to print out every number between 0 and 99  
6. Add a loop that uses `range()` to print out every number bewteen 1 and 100
7. Rewrite the script to take to start and end values from the command line. If you call your script like this `count.py 3 10` it will print the numbers from 3 to 10.
8. Modify your script so that it will only print the number if it is odd.


9. Make a list with the following data  `['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']`. Use a `for` loop to iterate through each element of this list and:
   - Print out each element
   - Print out the length and the sequence i.e., "4\\tATGC\\n"
10. Rewrite the script from 9. using a list comprehension to generate a list of tuples of sequences and lengths. Print out the length and the sequence i.e., "4\\tATGC\\n".

11. Modify the script from 10 so that you also print out the number of each sequence i.e. "1\t4\tACGT\n"

12. Have you been commiting you work?


## No need to do all the below now, but come back to these as you have time. They are fun exercises. You have already learned all you need to know to do each.

13. Create a shuffled sequence ([Fisher-Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle))
    - Use a for loop to perform the following procedure N times (N = length of seq)
    - Select a random position A with randrange()
    - Select a random position B with randrange()
    - Exchange the letters at list indices A and B
    - Print the final shuffled sequence
    - Remember to test your code with test data. 

14. Calculate sequence identity: Start with 2 very similar DNA sequences. Use your favorites or use [Python_04.fasta](https://raw.githubusercontent.com/srobb1/pfb2018/master/files/Python_04.fasta)
    - Align with ClustalW, TCoffee, or some other web alignment application. 
    - Output should be in FASTA format.
    - Store (copy and paste) each aligned sequence, including dashes, as two separate string variables. 
    - Get rid of newlines (if any). Newline characters are not part of sequence!
    - Use a `for` loop with `range()` to compare each index for nucleotide differences.
    - Report percent identity of the two sequences.

15. A new Restriction Fragments script:
   - Find [EcoRI](https://www.neb.com/products/r0101-ecori#Product%20Information) in this DNA sequence
   ```
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC
   ```
   - replace the EcoRI site 'GAATTC' with this 'G^AATTC'
   - split the new formatted sequence on the cut sites, store the resulting fragments in a list
   - iterate over each fragment and report
      - the start position in the original sequence
      - the end posttion in the orginal sequence
      - the length of each fragemnt
   - sort the fragments by length and print out as they would appear on a agrose gel. (big to little)


16. Have you been commiting you work?
