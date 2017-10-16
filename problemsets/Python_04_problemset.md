Python 4 Problem Set
===================

1. Write a script that uses a `while loop` to print out the number 1 to 100

2. Write a script that uses a `while loop` to calculate the [factorial](https://en.wikipedia.org/wiki/Factorial) of 1000.  

1. Iterate through each element of this list using a for loop: [101,2,15,22,95,33,2,27,72,15,52]
   - Print out only the values that are even (use modulus operator).

2. Iterate through each of the elements of the above list, but make sure to sort them numerically.
   - Print each element.
   - Create two cumulative sums, one of all the even values and one of all the odd values. 
   - Print the two sums.

5. Use `pop()` and `remove()` with the list of integers.

   - __`pop()`__

     - Print your list before you start.
     - Store the value returned by `pop()`. 
     - Print the value and the list.
     - What happened to the orginal list?
 
   -  __`remove()`__

      - Print your list before you start.
      - Store the value returned by `remove()`.
      - Print the value and the list.
      - What happened to the orginal list?

6. Write a script that uses `range()` in a `for loop` to print out every number between 0 and 99  

6. Add a loop that uses `range()` to print out every number bewteen 1 and 100

7. Rewrite the script to take to values from the command line

9. Now only print the number if it is odd.


10. Use a `for loop`, with the variable containing the list as the _sequence_, to iterate through each element of this list `['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']`. i.e, `for var in list:`
    - Print out each element
    - Print out the length along with the sequence i.e., "4\\tATGC\\n"

11. Use a `for loop` with `range()` instead of using the list variable to iterate through each element the list from the last Question. i.e, `for var in range(x):`

   - Print out each element
   - Print out the length along with the sequence  i.e., "4\\tATGC\\n" 



12. Create a shuffled sequence
    - Use a for loop to perform the following procedure N times (N = length of seq)
    -   Select a random position A with randrange()
    -   Select a random position B with randrange()
    -   Exchange the letters at list indices A and B
    - Print the final shuffled sequence
    - Remember to test your code with test data. 
 
13. Start with 2 very similar DNA sequences. Use your favorites or use [Python_04.fasta](https://raw.githubusercontent.com/srobb1/pfb2017/master/files/Python_04.fasta)
    - Align with ClustalW, TCoffee, or some other web alignment application. 
    - Output should be in FASTA format.
    - Store (copy and paste) each aligned sequence, including dashes, as two separate string variables. 
    - Be aware of the newlines (if any)
    - Use a `for loop` with `range()` to compare each index for nucleotide differences.
    - Report the nucleotide position of each difference.
  
14. Write a script in which you construct a dictionary of your favorite things.

> Some of my favorites:
>
> Type  |  Favorite |
> -----|------------|
> book | [Jitterbug Perfume](https://en.wikipedia.org/wiki/Jitterbug_Perfume)
> song | [Tom Petty - I Won't Back Down](https://www.youtube.com/watch?v=nvlTJrNJ5lA)
> tree | [Cedar](https://sciencing.com/cedar-trees-5432718.html) 
   

15. Write a script that iterates through each nucleotide of a DNA string:
    -  Print out each nucleotide
    -  Create a counter for each nucleotide. Count each nucleotide without using `count()`. 
    -  Print out the final count of each nucleotide. 

```
A = A_total
T = T_total
G = G_total
C = C_total
```
 
16.  Alter your counter in the last script use a dictionary for counting each nucleotide.


17. Write a script to find the intersection, difference, union, and symetrical difference between these two sets.

```
Set A = 3 14 15 9 26 5 35 9
Set B = 60 22 14 0 9
```

18. Have you been commiting you work?
