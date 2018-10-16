Python 2 Problem Set -- Operators, Truth, Logic
===================

1. Use the Interactive Interpretor to test to see if you can find an ['ATG' in](https://github.com/prog4biol/pfb2018#membership-operators) the following DNA string:

```
GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA
```
```python
>>> 'ATG' in 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
False
```
2. How about 'TTT'?
```python
>>> 'TTT' in 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
True
```
3. If you didn't already save the DNA string to a variable, do that now and redo [1 and 2](https://github.com/prog4biol/pfb2018#membership-operators).
```python
>>> dna_sequence='GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
>>> 'ATG' in dna_sequence
False
>>> 'TTT' in dna_sequence
True
```
4. In the interpretor use `bool` to test a variety of values like '', 0, 0.0, FALSE, false, True, true, 'True', 'False' to see if they evalue to True or False.
```python
>>> bool('')
False
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool(FALSE)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'FALSE' is not defined
>>> bool(false)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'false' is not defined
>>> bool(True)
True
>>> bool(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> bool('True')
True
>>> bool('False')
True
```
5. Using a text editor, write a script that
    - Assigns a value to a variable
    - Has a [if/else statment](https://github.com/prog4biol/pfb2018#logic-control-statements) in which:
       - It prints out a confirmation of truth if the value is true
       - It prints out "Not True" if the value is not true.
```python
#!/usr/bin/env python3
is_this_true = 'Coding is the most fun thing in the world'
if is_this_true:
    print("This is True!")
else:
    print("Not True")
```
6. Make sure to commit your changes along the way. You can wait until the end to push them to your remote repo, if you like, or you can do it now.
```sh
git add check_truth.py
git commit -m'adding check_truth.py'
git push
```
7. Write a new script that does the same as the question #5, but gets the value you will store in the variable from the command line. [Remember `sys` in the notes](pfb2018#command-line-parameters-a-special-built-in-list).
```python
#!/usr/bin/env python3
import sys
is_this_true = sys.argv[1]
if is_this_true:
    print("This is True!")
else:
    print("Not True")
```
8. Create a script that has a [if/else statement](https://github.com/prog4biol/pfb2018#if-statement) that (remember to write a little bit at a time and test it)
    - Test to see if a number is positive or negative
    - print "positive" if it is positive
    - print "negative" if it is negative
    - save it and run it.
```python
#!/usr/bin/env python3
import sys
my_number=int(sys.argv[1])
if my_number >= 0:
    print("positive")
else:
    print("negative")
```
9. Add an [elif](https://github.com/prog4biol/pfb2018#ifelif) to test if the number is equal to 0. Save it and run it.
```python
#!/usr/bin/env python3
import sys
my_number=int(sys.argv[1])
if my_number > 0:
    print("positive")
elif my_number == 0:
    print("zero")
else:
    print("negative")
```
10. Add nested tests to your last script
    - if it is positive, in addition to printing "positive"
    - test if it is smaller than 50
    - save it and run it    
```python
#!/usr/bin/env python3
import sys
my_number=int(sys.argv[1])
if my_number > 0:
    print("positive")
    if my_number < 50:
        print("Smaller than 50!")
elif my_number == 0:
    print("zero")
else:
    print("negative")
```
11. Add more nested tests to your script.
    - if it is smaller than 50
    - test if the number is even
    - if it is smaller than 50 and even, print "it is an even number that is smaller than 50"
    - save it and run it
```python
#!/usr/bin/env python3
import sys
my_number=int(sys.argv[1])
if my_number > 0:
    print("positive")
    if my_number < 50:
        if my_number % 2 ==0:
            print("it is an even number that is smaller than 50")
elif my_number == 0:
    print("zero")
else:
    print("negative")
```         
12. Add more nested tests.  
    -  if it is larger than 50,  
    -  test if the number is divisible by 3  
    -  if the number is larger than 50 and divisible by 3, print "it is larger than 50 and divisible by 3"  
    -  save it and run it
```python
#!/usr/bin/env python3
import sys
my_number=int(sys.argv[1])
if my_number > 0:
    print("positive")
    if my_number < 50:
        if my_number % 2 ==0:
            print("it is an even number that is smaller than 50")
    elif my_number > 50:
        if my_number % 3 == 0:
            print("it is larger than 50 and divisible by 3")
elif my_number == 0:
    print("zero")
else:
    print("negative")
```         
13. In your previous nested loops, test the number 50. What prints to the screen? Is it the correct response? If not, you have a semantic error and need to alter your code to be correct with any number.

```python
#!/usr/bin/env python3
import sys
my_number=int(sys.argv[1])
if my_number > 0:
    print("positive")
    if my_number < 50:
        if my_number % 2 ==0:
            print("it is an even number that is smaller than 50")
    elif my_number > 50:
        if my_number % 3 == 0:
            print("it is larger than 50 and divisible by 3")
    else:
        print("That's 50!")
elif my_number == 0:
    print("zero")
else:
    print("negative")
```  

14. ADD/COMMIT/PUSH

``` sh
git add check_numbers.py
git commit -m'added check_numbers.py'
git push
```
