Python 1 Problem Set
====================

1. **Start up the Python Interactive Interpreter. Print out "Hello New York"**

```sh
jabberwocky:answers mcampbel$ python
Python 3.6.2 |Anaconda, Inc.| (default, Sep 21 2017, 18:29:43) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello New York")
Hello New York 
```

2. **Store your name in a variable and print the contents of this variable.**

```sh
>>> name = "Mike"
>>> print(name)
Mike
```

3. **Use nano to write a script. Make sure to include # !/usr/bin/python3 at the top!!**

* **Make and open the file with nano.**

```sh
jabberwocky:answers mcampbel$ nano about_me.py
```

* **Write the script.**

```python
#!/usr/bin/env python3

print("my name is Mike")
print("my favorite color is blue")
print("my favorite activity is camping")
print("my favorite animal is a Snake")

```

* **Make it exicutable.**

```sh
chmod +x about_me.py
```

* **Run it from the command line*

```sh
jabberwocky:answers mcampbel$ ./about_me.py 
my name is Mike
my favorite color is blue
my favorite activity is camping
my favorite animal is a Snake
```

4. **Use sys.argv (make sure to import sys!!!) to retrieve your name, favorite color, favorite activity, and favorite animal from the command line.**

```python
#!/usr/bin/env python3

import sys

name     = sys.argv[1]
color    = sys.argv[2]
activity = sys.argv[3]
animal   = sys.argv[4]

print("my name is", name)
print("my favorite color is", color)
print("my favorite activity is", activity)
print("my favorite animal is a", animal)

```

Run it.

```sh
jabberwocky:answers mcampbel$ ./about_me.py Mike Blue Camping Snake
my name is Mike
my favorite color is Blue
my favorite activity is Camping
my favorite animal is a Snake
```

Run it agian.

```sh
jabberwocky:answers mcampbel$ ./about_me.py Michael Navy Backpacking "corn snake"
my name is Michael
my favorite color is Navy
my favorite activity is Backpacking
my favorite animal is a corn snake
```
I used the double quotes to deal with the white space in corn snake. This is what happend if you don't use the quotes.

```sh
jabberwocky:answers mcampbel$ ./about_me.py Michael Navy Backpacking corn snake
my name is Michael
my favorite color is Navy
my favorite activity is Backpacking
my favorite animal is a corn
```

"snake" ended up in sys.argv[5], which we didn't do anything with in the script.

5. **Make sure to keep your remote repository synced with your local repo. (ADD/COMMIT/PUSH)**

```sh
jabberwocky:answers mcampbel$ git add about_me.p

jabberwocky:answers mcampbel$ git commit -m "adding a script for python 1 problems"
[master 54b9249] adding a script for python1 problems
 1 file changed, 14 insertions(+)
 create mode 100755 problemsets/answers/about_me.py

jabberwocky:answers mcampbel$ git push origin maser
Counting objects: 5, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 562 bytes | 0 bytes/s, done.
Total 5 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/mscampbell/pfb2017.git
   1460df9..54b9249  master -> master
```
