#!/usr/bin/env python3

import sys



#  Python 1 Problem Set
# ==================
 

    
# 2. Working with a text editor. Use nano to write a script. 
#    - Make sure to include `#!/usr/bin/env python3` at the top!! 
#    - Add code to print out, your name  

my_name = sys.argv[1]

print('My name:', my_name)




#     - Now add some code to print out your favorite color:  

color = sys.argv[2]

print('My favorite color:', color)


#    - Now add some code to create a variable with your favorite activity. Make sure to give your variable a descriptive name.
#    - Print out the variable with your favorite activity. You will need to use a comma in your print statement to print text and your variable. `print("some text" , your_variable)`

activity = sys.argv[3]
print('My favorite activity:', activity)


#    - Now add some code to print out your favorite animal:      
        
animal =  sys.argv[4]

print('My favorite animal:', animal)

## plus in the print remove the space
print('My favorite animal:' + animal)

# 4. Use `sys.argv` (make sure to import sys!!!) to retrieve your name, favorite color, favorite activity, and favorite animal from the command line. Remember to check out the [example in the notes](https://github.com/prog4biol/pfb2019#command-line-parameters-a-special-built-in-list). Print all the variables in one print statement.
#     - try using commas to separate your print arguments. 
#     - try using '+' to separate your print arguments.



