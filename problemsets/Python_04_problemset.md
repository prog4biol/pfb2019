Python 4 Problem Set
===================

1. Write a script that uses a `while` loop to print out the numbers 1 to 100
2. Write a script that uses a `while loop` to calculate the [factorial](https://en.wikipedia.org/wiki/Factorial) of 1000.  
3. Iterate through each element of this list using a `for` loop: [101,2,15,22,95,33,2,27,72,15,52]
   - Print out only the values that are even (use modulus operator).
4. Sort the elements of the above list, then Iterate through each element and:
   - Print each element.
   - Calculate two cumulative sums, one of all the even values and one of all the odd values. 
   - Print the two sums.
5. Use `pop()` and `remove()` with the list of integers.

   - `pop()`

     - Print your list before you start.
     - Store the value returned by `pop()`. 
     - Print the value and the list.
     - What happened to the orginal list?

   - `remove()`

      - Print your list before you start.
      - Store the value returned by `remove()`.
      - Print the value and the list.
      - What happened to the orginal list?
6. Write a script that uses `range()` in a `for loop` to print out every number between 0 and 99  
7. Add a loop that uses `range()` to print out every number bewteen 1 and 100
8. Rewrite the script to take to start and end values from the command line. If you call your script like this `count.py 3 10` it will print the numbers from 3 to 10.
9. Modify your script so that it will only print the number if it is odd.


10. Make a list with the following data  `['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']`. Use a `for` loop to iterate through each element of this list and:
   - Print out each element
   - Print out the length and the sequence i.e., "4\\tATGC\\n"
11. Rewrite the script from 10. using a list comprehension to generate a list of tuples of sequences and lengths. Print out the length and the sequence i.e., "4\\tATGC\\n".

12. Modify the script from 10 so that you also print out the number of each sequence i.e. "1\t4\tACGT\n"



13. Create a shuffled sequence (Fisher-Yates shuffle)
    - Use a for loop to perform the following procedure N times (N = length of seq)
    - Select a random position A with randrange()
    - Select a random position B with randrange()
    - Exchange the letters at list indices A and B
    - Print the final shuffled sequence
    - Remember to test your code with test data. 

14. Start with 2 very similar DNA sequences. Use your favorites or use [Python_04.fasta](https://raw.githubusercontent.com/srobb1/pfb2017/master/files/Python_04.fasta)
    - Align with ClustalW, TCoffee, or some other web alignment application. 
    - Output should be in FASTA format.
    - Store (copy and paste) each aligned sequence, including dashes, as two separate string variables. 
    - Get rid of newlines (if any). Newline characters are not part of sequence!
    - Use a `for loop` with `range()` to compare each index for nucleotide differences.
    - Report percent identity of the two sequences.


15.  Write a script in which you construct a dictionary of your favorite things.

> Some of my favorites:
>
> | Type | Favorite                                 | 
> | ---- | ---------------------------------------- | 
> | book | [Jitterbug Perfume](https://en.wikipedia.org/wiki/Jitterbug_Perfume) | 
> | song | [Tom Petty - I Won't Back Down](https://www.youtube.com/watch?v=nvlTJrNJ5lA) |
> | tree | [Cedar](https://sciencing.com/cedar-trees-5432718.html) |


16.  Write a script that iterates through each nucleotide of a DNA string and keeps a tally of how many times each letter is seen in the sequence. Your script should be able to handle any characters it finds like N, n, X, x and so on. 
    -  Print out a table of all the counts of the different letters that occur in the sequence. It will look something like this
```
A = 34
T = 31
G = 29
C = 30
N = 2
...
```

17.   Write a script to find the intersection, difference, union, and symetrical difference between these two sets.

```
Set A = 3 14 15 9 26 5 35 9
Set B = 60 22 14 0 9
```

18. Have you been commiting you work?
