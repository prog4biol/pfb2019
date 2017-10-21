Problem Set Answers
===================

1. **Write a script that uses a `while loop` to print out the number 1 to 100**
    A `while` loop keeps iterating so long as our test condition evaluates to `True`. Since we want to count to 100, a natural condition that would remain `True` up to 100, would be to ask if our iteration count is still less than or equal to 100:
    ```python
    #!/usr/bin/env python3
    
    iteration = 0
    while iteration < 100:
        iteration += 1
        print("Iteration: {0:d}".format(iteration))
    ```

2. **Write a script that uses a `while loop` to calculate the [factorial](https://en.wikipedia.org/wiki/Factorial) of 1000.**
    N! (N factorial) means N x (N-1) x (N-2) x .. 3 x 2 x 1, so we need to iterate from 1 to N (in this case 1000) multiplying that value by the product of all previous values. This is acheived most conveniently with the `*=` operator:
    ```python
    #!/usr/bin/env python3
    
    iteration = 1
    factorial = 1  # we initialize with `1' because 0! == 1
    while iteration <= 1000:
        factorial *= iteration
        iteration += 1

    print("1000! = {0:d}".format(factorial))
    ```

3. **Iterate through each element of this list using a `for` loop: [101,2,15,22,95,33,2,27,72,15,52]**
    * **Print out only the values that are even (use modulus operator).**
        The modulus operator (`%`) returns the integer remainder from dividing the left side of the operator by the right side, *e.g.* long division of 5 divided by 2 yields remainder 2 with remainder 1, so `5 % 2 == 1`. And because even values have no remainder when divided by 2, we can use that as our test:
    ```python
    #!/usr/bin/env python3
    
    for item in [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]:
        if item % 2 == 0:
            print(item)
    ```
    
4. **Iterate through each of the elements of the above list, but make sure to sort them numerically.**
    * **Print each element.**
    * **Create two cumulative sums, one of all the even values one for all the odd values.**
    * **Print the two sums.**
    In order to calculate and print the sums of even and odd numbers, we must initialize our summation variables outside of the loop, at the top-level of our program, so that those sums are "remembered" by our script while and after we have concluded looping.
    ```python
    #!/usr/bin/env python3

    sum_odd = 0
    sum_even = 0
    for item in sorted([101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]):
        print(item)
        if item % 2 == 0:
            sum_even += item
        else:
            sum_odd += item
    print("Odd sum: {0:d}".format(sum_odd))
    print("Even sum: {0:d}".format(sum_even))
    ```

5. **Use `pop()` and `remove()` with the list of integers.**
    * **`pop()`**
        * **Print our list before you start.**
        * **Store the value returned by `pop()`.**
        * **Print the value and the list.**
        ```python
        #!/usr/bin/env python3
    
        list_obj = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
        print(list_obj)
        popped_item = list_obj.pop()
        print("Popped item: {0:d}".format(popped_item))
        print("Remaining list: {0:s}".format(str(list_obj)))
        ```
        * **What happened to the original list?**
            The original list was truncated by 1, `pop()` returning the truncated value. `pop()` takes as an optional argument the index of the list element to pop off/out, *e.g.* `L.pop(2)` will pop the second element out of the list `L` and return the value to be caught in a variable.

    * **`remove()`**
        * **Print our list before you start.**
        * **Store the value returned by remove().**
        * **Print the value and the list.**
        ```python
        #!/usr/bin/env python
        
        list_obj = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
        print(list_obj)
        removed_item = list_obj.remove(15)
        print("Removed item: {0:s}".format(str(removed_item)))
        print("Remaining list: {0:s}".format(str(list_obj)))
        ```
        * **What happened to the original list?**
            `remove()` removed the first occurance of it's argument ("15"); but unlike `pop()`, `remove()` does not return a value (instead returns `None`). Also, note that `remove()`'s argument is *not* an element's index, but the element's value.

6. **Write a script that uses `range()` in a `for loop` to print out every number between 0 and 99**
    `range()` requires at least one argument, the end value of to iterate toward. `range()`'s end value, as strange as it may seem at first, is non-inclusive.
    ```python
    #!/usr/bin/env python
    
    for item in range(100):
        print(item)
    ```
    This non-inclusivity makes perfect sense from a programmer's perspective, however, because its perfectly analogous to the following `while` loop idiom for iterating from 0 to 99 (*i.e.*, 100 total iterations over the `while` loop):
    ```python
    #!/usr/bin/env python
    
    item = 0
    while item < 100:
        print(item)
    ```

7. **Add a loop that uses `range()` to print out every number bewteen 1 and 100**
    `range` optionally takes a starting argument that comes before the end value. The default value of the start is 0, but below we set it to 1:
    ```python
    #!/usr/bin/env python
    
    for item in range(1, 101):
        print(item)
    ```
    Alternatively, we could have written the code above as:
    ```python
    #!/usr/bin/env python
    
    for item in range(100):
        print(item+1)
    ```

8. **Rewrite the script to take to start and end values from the command line. If you call your script like this `count.py 3 10` it will print the numbers from 3 to 10** 
    ```python
    #!/usr/bin/env python3

    import sys

    # arguments coming in from the command line are all strings, so we must
    # convert the values to integers
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    # again, the end value is non-inclusive, so we must +1 the end value we
    # wish to iterate to:
    for iteration in range(start, end+1):
        print("Iteration {0:d}".format(iteration))
    ```

9. **Modify your script so that it will only print the number if it is odd.**
    Put the individual components from previous questions together into a single script:
    ```python
    #!/usr/bin/env python3

    import sys

    start = int(sys.argv[1])
    end = int(sys.argv[2])

    for iteration in range(start, end+1):
        if iteration % 2 != 0:
            print("Iteration {0:d}".format(iteration))    
    ```

10. **Make a list with the following data `['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']`. Use a `for` loop to iterate through each element of this list and:**
    * **Print out each element**
        ```python
        #!/usr/bin/env python3
    
        # python allows you to wrap list initialization lines across
        # multiple lines for readability, here's an example:
        dna_frags = [
            'ATGCCCGGCCCGGC', 
            'GCGTGCTAGCAATACGATAAACCGG', 
            'ATATATATCGAT',
            'ATGGGCCC'
        ]
        for fragment in dna_frags:
            print(fragment)
        ```

    * **Print out the length and the sequence *i.e.*, "4\tATGC\n"**
        ```python
        #!/usr/bin/env python3
    
        dna_frags = [
            'ATGCCCGGCCCGGC', 
            'GCGTGCTAGCAATACGATAAACCGG', 
            'ATATATATCGAT',
            'ATGGGCCC'
        ]
        # the str.format() function allows you to use more readble labels
        # within the `{ }` part of the format string, which relate to keyword
        # arguments you may pass to the format() function:
        for fragment in dna_frags:
            print("{fraglen:d}\t{fragseq:s}".format(
                  fraglen=len(fragment), fragseq=fragment))
        ```

11. **Rewrite the script from 10. using a list comprehension to generate a list of tuples of sequences and lengths. Print out the length and the sequence *i.e.*, "4\tATGC\n".**
    List comprehesion converts the standard `for` loop into a single-line expression:
    ```python
    #!/usr/bin/env python3
    
    frag_lengths = [ (len(frag), frag) for frag in dna_frags ]
    for frag_tuple in frag_lengths:
    # in the line below, for lists and tuples, you can use * notation to
    # "unpack" the list or tuple for positional argument-requiring methods
    # or functions
    print("{0:d}\t{1:s}".format(*frag_tuple))
    ```
    The output of the above list comprehension is equivalent to the following standard form `for` loop:
    ```python
    #!/usr/bin/env python3
    
    frag_lengths = []
    for frag in dna_frags:
        frag_lengths.append( (len(frag), frag) )
    ```
    
12. **Modify the script from 10 so that you also print out the number of each sequence *i.e.* "1\t4\tACGT\n"**
    ```python
    #!/usr/bin/env python3
    
    for iteration, fragment in enumerate(dna_frags):
        print("{fragnum:d}\t{fraglen:d}\t{fragseq:s}".format(
              fragnum=iteration+1, fraglen=len(fragment), fragseq=fragment))
    ```

13. **Create a shuffled sequence (Fisher-Yates shuffle)**
    * **Use a for loop to perform the following procedure N times (N = length of seq)**
    * **Select a random position A with randrange()**
    * **Select a random position B with randrange()**
    * **Exchange the letters at list indices A and B**
    * **Print the final shuffled sequence**
    * **Remember to test your code with test data.**
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
        # The backslash at the end of the following line just allows us to
        # wrap a very long line onto multiple lines:
        (shuffled[rand_pos_A], shuffled[rand_pos_B]) \
            = (shuffled[rand_pos_B], shuffled[rand_pos_A])

    print("Original: {:s}".format(sequence))
    print("Shuffled: {:s}".format(''.join(shuffled)))
    ```

14. **Start with 2 very similar DNA sequences. Use your favorites or use [Python_04.fasta](https://raw.githubusercontent.com/srobb1/pfb2017/master/files/Python_04.fasta)**
    * **Align with ClustalW, TCoffee, or some other web alignment application.**
    * **Output should be in FASTA format.**
    * **Store (copy and paste) each aligned sequence, including dashes, as two separate string variables.**
    * **Get rid of newlines (if any). Newline characters are not part of sequence!**
    * **Use a `for loop` with `range()` to compare each index for nucleotide differences.**
    * **Report percent identity of the two sequences.**
    ```python
    #!/usr/bin/env python
    
    sequence1 = 'GCG-TGCTAGCAATACGATAAACCGG'  # no newlines!
    sequence2 = 'GCGGTGCTAGCTATACGAT-AACCGG'
    matchstr = ''
    matches = 0
    nonmatches = 0
    for position in range(len(sequence1)):
        if sequence1[position] == sequence2[position]:
            matches += 1
            matchstr += '|'
        else:
            nonmatches += 1
            matchstr += '*'

    print("Sequence 1: {:s}".format(sequence1))
    print("            {:s}".format(matchstr))  # Bonus!
    print("Sequence 2: {:s}".format(sequence2))
    print("Percent identity: {:.2f}".format(100 * matches/(matches+nonmatches)))
    ```

15. **Write a script in which you construct a dictionary of your favorite things.**
    The `range()` function also takes a third optional argument, the `by` or `step` size. The following code steps over the list's every second item (starting at the 0-th element).
    ```python
    #!/usr/bin/env python
    
    List = ["book", "Game of Thrones", "color", "black", "animal", "griffin"]
    favorites = {}
    for iteration in range(0, len(List), 2):
        favorites[List[iteration]] = List[iteration + 1]
    
    print(favorites)
    ```

16. **Write a script that iterates through each nucleotide of a DNA string and keeps a tally of how many times each letter is seen in the sequence. Your script should be able to handle any characters it finds like N, n, X, x and so on.**
    * Print out a table of all the counts of the different letters that occur in the sequence. It will look something like this
    ```python
    #!/usr/bin/env python
    
    nt_count = {}
    sequence = 'GCGTGCTAGCAANTACGATAAACCGGXx'
    for position in range(len(sequence)):
        nucleotide = sequence[position].upper()
        # if we observe a nucleotide we haven't encountered before and
        # we try to append the count directly the dict, we will get a 
        # KeyError (because we haven't initialized the dict key prior),
        # so we have to check whether the key exists in the dict before
        # we can increment the counter        
        if nucleotide not in nt_count:
            # initialize counter for nucleotide with 1
            nt_count[nucleotide] = 1
        else:
            # increment the counter for nucleotide by 1
            nt_count[nucleotide] += 1

    # any iteration operation dict is going to act on that dict's keys by 
    # default. We could call `sorted(nt_count.keys()) explicitly, or:
    for nucleotide in sorted(nt_count):
        print("{0:s} = {1:d}".format(nucleotide, nt_count[nucleotide]))
    ```

17. **Write a script to find the intersection, difference, union, and symetrical difference between these two sets.**
    ```python
    #!/usr/bin/env python
    
    setA = set((3, 14, 15, 9, 26, 5, 35, 9))
    setB = set((60, 22, 14, 0, 9))

    # find the elements common to both sets A and B:
    intersection = setA & setB
    # subtract any common elements between A & B from A:
    differenceA = setA - setB
    # subtract any common elements between A & B from B:
    differenceB = setB - setA
    # find the superset (union) of both sets:
    union = setA | setB
    # return only the elements that are NOT common between the two sets:
    symdifference = setA ^ setB

    print("Set A {:s}".format(str(setA)))
    print("Set B {:s}".format(str(setB)))
    print("Intersection: {:s}".format(str(intersection)))
    print("Difference A: {:s}".format(str(differenceA)))
    print("Difference B: {:s}".format(str(differenceB)))
    print("Union: {:s}".format(str(union)))
    print("Symmetric difference: {:s}".format(str(symdifference)))
    ```
    
18. **Have you been commiting you work?**
    ```sh
    git add JVB_Python_04_problemset.md
    git commit -m 'Initial commit if JVB_Python_04_problemset.py'
    git push origin master
    ```