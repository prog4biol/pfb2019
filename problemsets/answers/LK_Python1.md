# Python 1 Problem Set

Start up the Python Interactive Interpreter.
```sh
python
>>>
```
Print out "Hello New York"
```python
>>> print('Hello New York”')
Hello New York”
```
Store your name in a variable
```python
>>> my_name="Lukas"
```
Print the contents of this variable.
```python
>>> my_name="Lukas"
>>> print(my_name)
Lukas
```
Working with a text editor. Use nano to write a script.
Make sure to include #!/usr/bin/env python3 at the top!!
Add code to print out, your name
```python
#!/usr/bin/env python3
my_name="Lukas"
print("My name: ",my_name)
```
On the command line make it executable using chmod (only have to do this one time per script).
```sh
chmod u+x print_stuff_about_me.py
```
Run it from the command line.
```sh
./print_stuff_about_me.py
```
Remember it is important to write only a bit, test, then write more.
If it works, ADD/COMMIT. Make a good message, like "added name to print"
```sh
git add print_stuff_about_me.py
git commit -m"added my first python script"
git push
```
Now add some code to print out your favorite color:
```python
#!/usr/bin/env python3
my_name="Lukas"
my_fav_color="Blue"
print("My name: ",my_name,  "\nMy favorite color: ", my_fav_color)
```
Save it, and run it from the command line.
```sh
./print_stuff_about_me.py
```
Now add some code to create a variable with your favorite activity. Make sure to give your variable a descriptive name.
Print out the variable with your favorite activity. You will need to use a comma in your print statement to print text and your variable. print("some text" , your_variable)
```python
#!/usr/bin/env python3
my_name="Lukas"
my_fav_color="Blue"
my_fav_activity="Coding"
print("My name: ", my_name)
print("My favorite color: ", my_fav_color)
print("My favorite activity: ", my_fav_activity)
```
Save it, and run it from the command line.
```sh
./print_stuff_about_me.py
```
Now add some code to print out your favorite animal:

 My name: Sofia
 My favorite color: Green
 My favorite activity: Coding
 My favorite animal: Chicken
Remember, write a bit, then run your code, write some more, then run again. This makes code easier to debug.
```python
#!/usr/bin/env python3
my_name="Lukas"
my_fav_color="Blue"
my_fav_activity="Coding"
my_fav_animal="Chimp"
print("My name: ", my_name, "\nMy favorite color: ", my_fav_color, "\nMy favorite activity: ", my_fav_activity, "\nMy favorite animal: ", my_fav_animal)
```
Use sys.argv (make sure to import sys!!!) to retrieve your name, favorite color, favorite activity, and favorite animal from the command line. Remember to check out the example in the notes. Print all the variables in one print statement.
try using commas to separate your print arguments.
try using '+' to separate your print arguments.
```python
#!/usr/bin/env python3
import sys
my_name=sys.argv[1]
my_fav_color=sys.argv[2]
my_fav_activity=sys.argv[3]
my_fav_animal=sys.argv[4]
#print using coma
print("My name: ", my_name, "\nMy favorite color: ", my_fav_color, "\nMy favorite activity: ", my_fav_activity, "\nMy favorite animal: ", my_fav_animal)
# print using +
print("My name: " + my_name + "\nMy favorite color: " + my_fav_color + "\nMy favorite activity: " + my_fav_activity, "\nMy favorite animal: " + my_fav_animal)
```
```sh
./print_stuff_about_me.py Lukas Blue Coding Chimp
```
Make sure to keep your remote repository synced with your local repo. (ADD/COMMIT/PUSH)
```sh
git add print_stuff_about_me.py
git commit -m"added my first python script"
git push
```
