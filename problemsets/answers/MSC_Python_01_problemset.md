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
