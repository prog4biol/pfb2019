### Good Practices in Coding

* Writing clear scripts
  * Commenting
  * Naming variables
* Creating README files

####Writing clear scripts

```
vi script.py
```

```python
#!/usr/bin/env python3
import sys
n = int(sys.argv[1])
if n == 0:
	print(n, 'equals 0')
elif n > 0:
	print(n, 'is positive')
else:
	print(n, 'is negative')
```

A clearer version:

```
vi PFB_PS_2.5.py
```

```python
#!/usr/bin/env python3

# Filename: PFB_PS_2.5.py
# Owner: Shasta Webb
# Description: This script tests and prints to standard output whether a number is 0, positive, or negative.

#====================
# Required Libraries
#====================

import sys

#===========
# Variables
#===========

myNum = int(sys.argv[1]) #Remember to turn command line arguments into integers!

#========
# Script
#========

if myNum == 0: #This line tests if n is equal to 0
	print(myNum, 'equals 0.') 
elif n > 0:
	print(myNum, 'is positive.')
else:
	print(myNum, 'is negative.')
	
print('\nEnd of script.\n')

#========
# Notes
#========

#elif n >= 0: <---did not work
#etc etc
```
####Consider creating a README.md file

When are README's useful?

* For personal organization when you have many projects ongoing
* For collaborators or people interested in your code need an overview of what it does
* To archive the purpose of the code, special instructions for installing or using, the language it is written in etc.
* Listing authorship and acknowledgements



