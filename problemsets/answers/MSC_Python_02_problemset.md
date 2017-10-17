Python 2 Problem Set
===================

1. **Use the Interactive Interpretor to test to see if you can find an 'ATG' in the following DNA string:**

```
GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA
```

```sh
mcampbel@jabberwocky.cshl.edu:answers$ python3
Python 3.6.2 |Anaconda, Inc.| (default, Sep 21 2017, 18:29:43) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 'ATG' in 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
False 
```
	
2. **How about 'TTT'?**

```sh
>>> 'TTT' in 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
True
```
3. **Save the DNA string to a variable and do 1 and 2 again.**

```sh
>>> dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
>>> 'ATG' in dna
False
>>> 'TTT' in dna
True

```

4. **In the interpretor use `bool` to test a variety of values like '', 0, 0.0, FALSE, false, True, true, 'True', 'False' to see if they evalue to True or False.**

```sh
>>> bool('mike')
True
>>> bool(0)
False
>>> bool(mike)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mike' is not defined
>>> bool('0')
True
>>> bool(0.0)
False
>>> mike = False
>>> bool(mike)
False
>>> mike = True
>>> bool(mike)
True
>>> mike = 'False'
>>> bool(mike)
True

```

5. **Using a text editor, write a script that** 
 * **Assigns a value to a variable**
 * **Has a if/else statment in which:**
       * ** It prints out a confirmation of truth if the value is true**
       * ** It prints out "Not True" if the value is not true. **

       ```python
#!/usr/bin/env python3

my_favorite_number = 8

if my_favorite_number:
    print("Truth confirmed")
else:
    print("Not true")
```

```sh
mcampbel@jabberwocky.cshl.edu:answers$ ./truth.pl
Truth confirmed
```

6. **Make sure to commit your changes along the way. You can wait until the end to push them to your remote repo, if you like, or you can do it now.** 

7. **Write a new script that does the same as the last question, but gets the value from the command line.**

```python
#!/usr/bin/env python3
import sys

my_favorite_number = sys.argv[1]

if my_favorite_number:
    print("Truth confirmed")
else:
    print("Not true")
```

```python
mcampbel@jabberwocky.cshl.edu:answers$ ./truth_cl.pl 8
Truth confirmed
```
8. **Create a script that has a if/elif/else statement that**
   * ** Tests to see if a number is positive or negative**
   * ** if it is positive, is it bigger or smaller than 50**
   * ** if it is smaller, is it an even number**
   * ** if it is larger, is it divisible by 3.**  

```python
#!/usr/bin/env python3

import sys
number = int(sys.argv[1])
    
if number >= 0: #positive
    print(number, "is positive")
    if number > 50: #bigger than 50
        print(number, "is bigger than 50")
        if number % 3: #not divisible by three
            print(number, "is not divisable by 3")
        else: #divisible by 3
            print(number, "is divisable by 3")     
    elif number < 50: #smaller than 50
        print(number, "is smaller than 50")     
        if number % 2: #is odd
            print(number, "is odd")     
        else: #is even
            print(number, "is even")        
    elif number == 50: #negative or equal to 50
        print(number, "is equal to 50")                 
else:
    print(number, "is negative")
```

9. **ADD/COMMIT/PUSH**
