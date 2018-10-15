#==========================================
# Python 01 Problem Set Solutions
#==========================================

#File owner: 	Shasta Webb
#Date: 			October 15, 2018

1. Start up the Python Interactive Interpreter. Print out "Hello New York"

python3
print('"Hello New York"')

2. Working with variables:
    - Store your name in a variable
    - Print the contents of this variable.

myName = 'Shasta'
print(myName)

3. Working with a text editor. Using nano to write a script. 
   - Make sure to include `#!/usr/bin/env python3` at the top!! 
   - Print out, your name  
   
        ```
         My name: Sofia
        ```
		```
		$ vi aboutMe.py
		```

		```python
		#!/usr/bin/env python3

		myName = "Shasta"

		print(myName + "is my name.")
		```
 
    - Make it executable using `chmod` (only have to do this one time per script).

	```
	$ chmod +x aboutMe.py
	```

    - Run it from the command line. 

	```
	$ aboutMe.py
	```

    - Now add some code to print out your favorite color:  
  
         ```
         My name: Sofia
         My favorite color: Green
        ```

		```python

		#! usr/bin/env/ python3

		myName = "Shasta"
        myFavColor = "green"
        
		print(myName + "is my name.")
        print(myFavAnimal + "is my favorite animal.")

		```

  - Save it, and run it from the command line. 

		```
		$ aboutMe.py
		```

   - Now add some code to print out your favorite activity:

       ```
         My name: Sofia
         My favorite color: Green
         My favorite activity: Coding
        ```

		```python3
		#! usr/bin/env/ python3

		myName = "Shasta"
		myFavColor = "green"
		myFavActivity = "biking"

		print(myName + "is my name.")
		print(myFavAnimal + "is my favorite animal.")
		print(myFavActivity + "is my favorite activity.")

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
	
		myName = "Shasta"
		myFavColor = "green"
		myFavActivity = "biking"
		myFavAnimal = "cat"

		print(myName + "is my name.")
		print(myFavColor + "is my favorite color.")
		print(myFavActivity + "is my favorite activity.")
		print(myFavAnimal + "is my favorite animal.")	
		```
		
        >>>  Remeber, write a bit, then run your code, write some more, then run again. This makes code easier to debug. 

4. Use `sys.argv` (make sure to import sys!!!) to retrieve your name, favorite color, favorite activity, and favorite animal from the command line. Remember to check out the [example in the notes](https://github.com/prog4biol/pfb2018#command-line-parameters-a-special-built-in-list)
		```python
		#!/usr/bin/env python3
		
		import sys
		
		myName = sys.ARGV[1]
		myFavColor = sys.ARGV[2]
		myFavActivity = sys.ARGV[3]
		myFavAnimal = sys.ARGV[4]

		print(myName + "is my name.")
		print(myFavColor + "is my favorite color.")
		print(myFavActivity + "is my favorite activity.")
		print(myFavAnimal + "is my favorite animal.")
		```



5. Make sure to keep your remote repository synced with your local repo. (ADD/COMMIT/PUSH)

	```
	$ git add aboutMe.py
	$ git commit -m 'adding aboutMe.py'
	$ git push
	```





