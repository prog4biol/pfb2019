#==========================================
# Python 01 Problem Set Solutions
#==========================================

#File owner: 	Shasta Webb
#Date: 			October 15, 2018

1. Start up the Python Interactive Interpreter. 

	- Print out "Hello New York"

	```
	python3
	Python 3.6.3 |Anaconda, Inc.| (default, Oct  6 2017, 12:04:38) 
	[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> print("Hello New York")
	Hello New York
	```
    - Store your name in a variable

	```python
	>>>myName = "Shasta"
	```

    - Print the contents of this variable.

	```python
	>>>print(myName)
	Shasta
	```

2. Working with a text editor. Using nano to write a script. 
   - Make sure to include `#!/usr/bin/env python3` at the top!! 
   - Print out, your name  
   
        ```
         My name: Sofia
        ```

	I decided to do this in VI, a great text editor I would highly recommend!
		```
		$ vi aboutMe.py
		```

		```python
		#!/usr/bin/env python3

		print("My name is: Shasta")
		```
 
    - Make it executable using `chmod` (only have to do this one time per script).

	```
	$ chmod +x aboutMe.py
	```

    - Run it from the command line. 

	```
	$ aboutMe.py
	```
	- Remember it is important to write only a bit, test, then write more.
	- If it works, ADD/COMMIT. Make a good message, like "added name to print"

	```
	$ git add aboutMe.py
	$ git commit -m 'adding name to aboutMe.py'
	```

    - Now add some code to print out your favorite color:  
  
         ```
         My name: Sofia
         My favorite color: Green
        ```
		
		```python
		#!/usr/bin/env python3

		print("My name is: Shasta")
        print("My favorite color is: Green")
		```

  - Save it, and run it from the command line. 

		```
		$ aboutMe.py
		```

	- Now add some code to create a variable with your favorite activity. Make sure to give your variable a descriptive name.

       ```
         My name: Sofia
         My favorite color: Green
         My favorite activity: Coding
        ```

		```python3
		#!/usr/bin/env python3

		myFavActivity = "biking"
		
		print("My name is: Shasta")
		print("My favorite color is: Green")
		print("My favorite activity is:", myFavActivity)
		```
   - Save it, and run it from the command line. 

		```
		$ aboutMe.py
		```
	
   - Now add some code to print out your favorite animal:      
        
        ```
         My name: Sofia
         My favorite color: Green
         My favorite activity: Coding
         My favorite animal: Chicken
        ```
		
		```python3
		#! usr/bin/env/ python3
	
		myFavActivity = "biking"
		myFavAnimal = "cat"

		print("My name is: Shasta")
		print("My favorite color is: Green")
		print("My favorite activity is:", myFavActivity)
		print("My favorite animal is:", myFavAnimal)
		```
		
        >>>  Remember, write a bit, then run your code, write some more, then run again. This makes code easier to debug. 

3. Use `sys.argv` (make sure to import sys!!!) to retrieve your name, favorite color, favorite activity, and favorite animal from the command line. Remember to check out the [example in the notes](https://github.com/prog4biol/pfb2018#command-line-parameters-a-special-built-in-list)

		```python
		#!/usr/bin/env python3
		
		import sys
		
		myName = sys.argv[1]
		myFavColor = sys.argv[2]
		myFavActivity = sys.argv[3]
		myFavAnimal = sys.argv[4]

		print(myName, "is my name.")
		print(myFavColor, "is my favorite color.")
		print(myFavActivity, "is my favorite activity.")
		print(myFavAnimal, "is my favorite animal.")
		```

5. Make sure to keep your remote repository synced with your local repo. (ADD/COMMIT/PUSH)

	```
	$ git add aboutMe.py
	$ git commit -m 'adding updated aboutMe.py'
	$ git push
	```
