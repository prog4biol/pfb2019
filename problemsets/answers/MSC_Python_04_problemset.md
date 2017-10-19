Python 4 Problem Set
===================

1. **Write a script that uses a `while` loop to print out the numbers 1 to 100**

```python
#!/usr/bin/env python3                                                              
count = 1
while count <= 100:
  print("count:" , count)
  count+=1
print("Done")
```

run it

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py 
count: 1
count: 2
count: 3
count: 4
count: 5
count: 6
count: 7
count: 8
...
count: 95
count: 96
count: 97
count: 98
count: 99
count: 100
Done
```
2. **Write a script that uses a `while loop` to calculate the [factorial](https://en.wikipedia.org/wiki/Factorial) of 1000.**

```python
#!/usr/bin/env python3                                                              
factorial = 1000
count = 1000
while count > 1:
  count -= 1
  factorial *= count

print(factorial)
```  

run it

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py 
402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461062892187960223838971476088506276862967146674697562911234082439208160153780889893964518263243671616762179168909779911903754031274622289988005195444414282012187361745992642956581746628302955570299024324153181617210465832036786906117260158783520751516284225540265170483304226143974286933061690897968482590125458327168226458066526769958652682272807075781391858178889652208164348344825993266043367660176999612831860788386150279465955131156552036093988180612138558600301435694527224206344631797460594682573103790084024432438465657245014402821885252470935190620929023136493273497565513958720559654228749774011413346962715422845862377387538230483865688976461927383814900140767310446640259899490222221765904339901886018566526485061799702356193897017860040811889729918311021171229845901641921068884387121855646124960798722908519296819372388642614839657382291123125024186649353143970137428531926649875337218940694281434118520158014123344828015051399694290153483077644569099073152433278288269864602789864321139083506217095002597389863554277196742822248757586765752344220207573630569498825087968928162753848863396909959826280956121450994871701244516461260379029309120889086942028510640182154399457156805941872748998094254742173582401063677404595741785160829230135358081840096996372524230560855903700624271243416909004153690105933983835777939410970027753472000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```
3. **Iterate through each element of this list using a `for` loop: [101,2,15,22,95,33,2,27,72,15,52]**
   * **Print out only the values that are even (use modulus operator).**
```python
#!/usr/bin/env python3

numbers = [101,2,15,22,95,33,2,27,72,15,52]

for number in numbers:
    if number % 2 ==0: #is even
    	  print(number)


```
run it

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py
2
22
2
72
52
```

4. * **Sort the elements of the above list, then Iterate through each element and:**
   * **Print each element.**
   * **Calculate two cumulative sums, one of all the even values and one of all the odd values.** 
   * **Print the two sums.**
```python
#!/usr/bin/env python3

numbers = [101,2,15,22,95,33,2,27,72,15,52]
odds  = []
evens = []
for number in numbers:
  if number % 2 ==0: #is even
    evens.append(number)
  else:
    odds.append(number)
    
cume_odd=0
cume_even=0
for odd in odds:
  cume_odd += odd
for even in evens:
  cume_even += even

print("cumulative even sum", cume_even)
print("cumulative odd sum", cume_odd)
```

run it

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py
cumulative even sum 150
cumulative odd sum 286
```
5. **Use `pop()` and `remove()` with the list of integers.**

   * ** `pop()`**

     * **Print your list before you start.**
     * **Store the value returned by `pop()`.** 
     * **Print the value and the list.**
     * ** What happened to the orginal list?**
```python
#!/usr/bin/env python3

numbers = [101,2,15,22,95,33,2,27,72,15,52]

print(numbers)
popped = numbers.pop()
print(popped)
print(numbers)
```

run it

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py
[101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
52
[101, 2, 15, 22, 95, 33, 2, 27, 72, 15]
```

One element was removed from the end of the list

   * **`remove()`**

      * **Print your list before you start.**
      * **Store the value returned by `remove()`.**
      * **Print the value and the list.**
      * **What happened to the orginal list?**

```python
#!/usr/bin/env python3

numbers = [101,2,15,22,95,33,2,27,72,15,52]

print(numbers)
removed = numbers.remove(52)
print(removed)
print(numbers)
```

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py
[101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
None
[101, 2, 15, 22, 95, 33, 2, 27, 72, 15]
```
6. **Write a script that uses `range()` in a `for loop` to print out every number between 0 and 99**

```python
#!/usr/bin/env python3

for num in range(100):
  print(num, end=' ')
```

run it

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99
```   
     
7. **Add a loop that uses `range()` to print out every number bewteen 1 and 100**

```python
#!/usr/bin/env python3

for num in range(1,101):
  print(num, end=' ')
```

run it

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
```
8. **Rewrite the script to take to start and end values from the command line. If you call your script like this `count.py 3 10` it will print the numbers from 3 to 10.**

```python
#!/usr/bin/env python3

import sys

start = int(sys.argv[1])
end = int(sys.argv[2])
 
for num in range(start, end + 1):
  print(num, end=' ')
```

run it

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py 2 5
2 3 4 5
```

9. **Modify your script so that it will only print the number if it is odd.**

```python
#!/usr/bin/env python3

import sys

start = int(sys.argv[1])
end = int(sys.argv[2])
 
for num in range(start, end + 1):
  if num % 2 ==0:
    continue
  else:
    print(num, end=' ')
```

run it

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py 2 5
3 5
```

10. **Make a list with the following data  `['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']`. Use a `for` loop to iterate through each element of this list and:**
   * **Print out each element**
   * **Print out the length and the sequence i.e., "4\\tATGC\\n"**

```python
#!/usr/bin/env python3

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
      
for seq in seqs:
  print(len(seq),"\t", seq)
```

run it

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py
14    ATGCCCGGCCCGGC
25    GCGTGCTAGCAATACGATAAACCGG
12    ATATATATCGAT
8     ATGGGCCC
```

11. **Rewrite the script from 10. using a list comprehension to generate a list of tuples of sequences and lengths. Print out the length and the sequence i.e., "4\\tATGC\\n".**

```python
#!/usr/bin/env python3                                                                      

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

lens = [(len(seq), seq) for seq in seqs]

for tuples in lens:
    print(tuples[0],"\t",tuples[1])
```

run it

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py
14 	ATGCCCGGCCCGGC
25 	GCGTGCTAGCAATACGATAAACCGG
12 	ATATATATCGAT
8 	ATGGGCCC
```

12. **Modify the script from 10 so that you also print out the number of each sequence i.e. "1\t4\tACGT\n"**

```python
#!/usr/bin/env python3

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

lens = [(len(seq), seq) for seq in seqs]
count = 1
for tuples in lens:
    print(count, "\t", tuples[0],"\t",tuples[1])
    count += 1
```

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py
1        14	 ATGCCCGGCCCGGC
2 	 25      GCGTGCTAGCAATACGATAAACCGG
3 	 12      ATATATATCGAT
4 	 8       ATGGGCCC

```

12. **Create a shuffled sequence (Fisher-Yates shuffle)**
    * ** Use a for loop to perform the following procedure N times (N = length of seq)**
    * ** Select a random position A with randrange()**
    * ** Select a random position B with randrange()**
    * ** Exchange the letters at list indices A and B**
    * ** Print the final shuffled sequence**
    * ** Remember to test your code with test data.** 

```python
#!/usr/bin/env python3
import random

sequence = 'AAATTT'
slen =  len(sequence)
iters = slen
seq_list = list(sequence)

while iters > 0:
    ri1 = random.randrange(0,slen -1, 1)
    ri2 = random.randrange(0,slen -1, 1)
    
    nuc1 = seq_list[ri1]
    nuc2 = seq_list[ri2]

    seq_list[ri2] = nuc1
    seq_list[ri1] = nuc2

    iters -= 1

print("".join(seq_list))
```

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py
TTAAAT
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py
TTAAAT
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py
AATTAT
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py
ATAATT
mcampbel@jabberwocky.cshl.edu:answers$ ./loops.py
AATATT
```
13. Start with 2 very similar DNA sequences. Use your favorites or use [Python_04.fasta](https://raw.githubusercontent.com/srobb1/pfb2017/master/files/Python_04.fasta)
    - Align with ClustalW, TCoffee, or some other web alignment application. 
    - Output should be in FASTA format.
    - Store (copy and paste) each aligned sequence, including dashes, as two separate string variables. 
    - Get rid of newlines (if any). Newline characters are not part of sequence!
    - Use a `for loop` with `range()` to compare each index for nucleotide differences.
    - Report percent identity of the two sequences.

14. Write a script in which you construct a dictionary of your favorite things.

> Some of my favorites:
>
> | Type | Favorite                                 | 
> | ---- | ---------------------------------------- | 
> | book | [Jitterbug Perfume](https://en.wikipedia.org/wiki/Jitterbug_Perfume) | 
> | song | [Tom Petty - I Won't Back Down](https://www.youtube.com/watch?v=nvlTJrNJ5lA) |
> | tree | [Cedar](https://sciencing.com/cedar-trees-5432718.html) |


15. Write a script that iterates through each nucleotide of a DNA string and keeps a tally of how many times each letter is seen in the sequence. Your script should be able to handle any characters it finds like N, n, X, x and so on. 
    -  Print out a table of all the counts of the different letters that occur in the sequence. It will look something like this

```
A = 34
T = 31
G = 29
C = 30
N = 2
...
```

16.   Write a script to find the intersection, difference, union, and symetrical difference between these two sets.

```
Set A = 3 14 15 9 26 5 35 9
Set B = 60 22 14 0 9
```

18. Have you been commiting you work?
