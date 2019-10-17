
Python 2 Problem Set -- Operators, Truth, Logic
===================

###Solutions
###Author: Shasta Webb

1. Use the Interactive Interpretor to test to see if you can find an ['ATG' in](https://github.com/prog4biol/pfb2018#membership-operators) the following DNA string:

```
GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA
```

```
python3
>>>'ATG' in 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
False 
```

2. How about 'TTT'?

```
python3
>>>'ATG' in 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
True
```

3. If you didn't already save the DNA string to a variable, do that now and redo [1 and 2](https://github.com/prog4biol/pfb2018#membership-operators).

```
python3
>>>mySeq = 'ATG'
>>>mySeq in 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
False
```

```
>>>myOtherSeq = 'TTT'
>>>myOtherSeq in 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
True
```
4. In the interpretor use `bool` to test a variety of values like '', 0, 0.0, FALSE, false, True, true, 'True', 'False' to see if they evalue to True or False.

```
>>>bool(0)
False
>>>bool(False)
False
>>>bool('False')
True
```

5. Using a text editor, write a script that 
    - Assigns a value to a variable
    - Has a [if/else statment](https://github.com/prog4biol/pfb2018#logic-control-statements) in which:
       - It prints out a confirmation of truth if the value is true
       - It prints out "Not True" if the value is not true. 

```
$ vi ps2.5.py
```

```python
#!/usr/bin/env python3

myVar = 'cat'

if bool(myVar) is True:
	print(myVar, "is true.")
else:
	print(myVar, "is not true.")

print("Done.")
```

6. Make sure to commit your changes along the way. You can wait until the end to push them to your remote repo, if you like, or you can do it now. 

```
$ git add ps2.5.py
$ git commit -m 'adding ps2.5.py'
$ git push
```

7. Write a new script that does the same as the question #5, but gets the value you will store in the variable from the command line. [Remember `sys` in the notes](pfb2018#command-line-parameters-a-special-built-in-list). 

```
#!/usr/bin/env python3

import sys

user_input = sys.argv[1]

if bool(user_input) is False:
	print(user_input, "is false.")
else:
	print(user_input, "is true.")

print("End of script.\n")
```

8. Create a script that has a [if/else statement](https://github.com/prog4biol/pfb2018#if-statement) that (remember to write a little bit at a time and test it)
    - Test to see if a number is positive or negative
    - print "positive" if it is positive
    - print "negative" if it is negative
    - save it and run it.

```python
!/usr/bin/env python3
import sys

user_input = int(sys.argv[1])
if user_input > 0:
	print(user_input, "is positive.")
else:
	print(user_input, "is negative.")

print("End of script.\n")
```

9. Add an [elif](https://github.com/prog4biol/pfb2018#ifelif) to test if the number is equal to 0. Save it and run it.

```python
!/usr/bin/env python3
import sys

user_input = int(sys.argv[1])
if user_input > 0:
	print(user_input, "is positive.")
elif user_input == 0:
	print(user_input, "is equal to 0.")
else:
	print(user_input, "is negative.")

print("End of script.\n")
```

10. Add nested tests to your last script
    - if it is positive, in addition to printing "positive"
    - test if it is smaller than 50
    - save it and run it    

```python
!/usr/bin/env python3
import sys

user_input = int(sys.argv[1])
if user_input > 0:
	if user_input < 50:
		print(user_input, "is positive and less than 50.")
	else:
		print(user_input, "is positive and greater than 50.")
elif user_input == 0:
	print(user_input, "is equal to 0.")
else:
	print(user_input, "is negative.")

print("End of script.\n")
```

11. Add more nested tests to your script.
    - if it is smaller than 50
    - test if the number is even
    - if it is smaller than 50 and even, print "it is an even number that is smaller than 50"
    - save it and run it

```python
!/usr/bin/env python3
import sys

user_input = int(sys.argv[1])
if user_input > 0:
	if user_input < 50:
		if user_input % 2 == 0:
			print(user_input, "is positive, even, and less than 50.")
		else:
			print(user_input, "is positive, odd, and less than 50.")
	else:
		print(user_input, "is positive and greater than 50.")
elif user_input == 0:
	print(user_input, "is equal to 0.")
else:
	print(user_input, "is negative.")

print("End of script.\n")
```

12. Add more nested tests.  
    -  if it is larger than 50,  
    -  test if the number is divisible by 3  
    -  if the number is larger than 50 and divisible by 3, print "it is larger than 50 and divisible by 3"  
    -  save it and run it

```python
!/usr/bin/env python3
import sys

user_input = int(sys.argv[1])
if user_input > 0:
	if user_input > 50:
		if user_input % 3 == 0:
			print(user_input, "is positive, divisible by 3, and greater than 50.")
		else:
			print(user_input, "is positive, not divisible by 3, and less than 50.")
	elif user_input < 50:
		if user_input % 2 == 0:
			print(user_input, "is smaller than 50, and is an even number.")
		else:
			print(user_input, "is smaller than 50, but is an odd number.")
	else:
		print(user_input, "is positive and greater than 50.")
elif user_input == 0:
	print(user_input, "is equal to 0.")
else:
	print(user_input, "is negative.")

print("End of script.\n")
```



13. In your previous nested loops, test the number 50. What prints to the screen? Is it the correct response? If not, you have a semantic error and need to alter your code to be correct with any number.

```python
!/usr/bin/env python3
import sys

user_input = int(sys.argv[1])
if user_input > 0:
	if user_input > 50:
		if user_input % 3 == 0:
			print(user_input, "is positive, divisible by 3, and greater than 50.")
		else:
			print(user_input, "is positive, not divisible by 3, and less than 50.")
	elif user_input < 50:
		if user_input % 2 == 0:
			print(user_input, "is smaller than 50, and is an even number.")
		else:
			print(user_input, "is smaller than 50, but is an odd number.")
	elif user_input == 50:
		print(user_input, "is equal to 50.")
	else:
		print(user_input, "is positive and greater than 50.")
        
elif user_input == 0:
	print(user_input, "is equal to 0.")
else:
	print(user_input, "is negative.")

print("End of script.\n")
```

14. ADD/COMMIT/PUSH


```
$ git add ps2scripts.py
$ git commit -m 'adding ps2scripts'
$ git push

```