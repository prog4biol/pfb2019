Problem Set Answers
===================
1. **Start up the Python Interactive Interpreter. Print out "Hello New York"**
    I prefer to use iPython over the native python interactive interpreter because it is loaded with more and useful features, like rich coloring, autocomplete, and suggestions:
    ```
    $ ipython
    Python 3.5.4 |Anaconda custom (x86_64)| (default, Aug 14 2017, 12:43:10) 
    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.
    In [1]: print("Hello New York")
    Hello New York

    In [2]:
    ```
2. **Store your name in a variable and print the contents of this variable.**
    The only characters we can use in variable names are alphanumeric [A-Za-z0-9] and the underscore (`_`), no spaces!. Using descriptive variable names makes your code much more readable for yourself and others, especially 6 months in the future when you want to modify your script to include some new feature. This translates to fewer bugs in your code overall. A good practice is to create variable names that read like sentences when you use them in your code, for instance:
    ```python
    In [2]: my_name = "Jessen Bredeson"
    In [3]: print(my_name)
    ```

3. **Use nano to write a script. Make sure to include #!/usr/bin/env python3 at the top!!**
    * **The script should print out, your name, favorite color, favorite activity, and your favorite animal.**
        ```sh
        $ emacs aboutme.py
        ```
        ```python
        #!/usr/bin/env python3
        
        my_name = "Jessen Bredeson"
        my_favorite_color = "black"
        my_favorite_activity = "programming"
        my_favorite_animal = "griffin"
        
        print(my_name)
        print(my_favorite_color)
        print(my_favorite_activity)
        print(my_favorite_animal)
        ```
        > Pro tip: if you haven't closed your in-Terminal emacs/vi session yet, you can press `^z` (control+z) to "minimize" the session window, and type `fg` in the command line to bring it back up. If you have multiple closed sessions, type `jobs` to show all of your processes. You can load a specific process by its index, for example `fg 2` will reload the second process to your screen.
        
    * **Make it executable using chmod (only have to do this one time per script).**
            
        ```sh
        $ chmod +x aboutme.py
        ```
        
    * **Run it from the command line.**
        ```sh
        $ ./aboutme.py
        Jessen Bredeson
        black
        programming
        griffin
        ```
4. **Use `sys.argv` (make sure to import sys!!!) to retrieve your name, favorite color, favorite activity, and favorite animal from the command line.**
    ```sh
    $ emacs ./aboutme2.py
    ```
    ```python
    #!/usr/bin/env python3
        
    import sys
        
    # sys.argv holds a python list() and lists are 0-based 
    # indexed (first position has index 0), but sys.argv[0] holds
    # our script name, so we don't want to use it below:
    my_name = sys.argv[1]
    my_favorite_color = sys.argv[2]
    my_favorite_activity = sys.argv[3]
    my_favorite_animal = sys.argv[4]
        
    print(my_name)
    print(my_favorite_color)
    print(my_favorite_activity)
    print(my_favorite_animal)
    ```
    Save and quit, then test your code:
    ```sh
    $ ./aboutme2.py "Jessen Bredeson" "black" "programming" "griffin"
    Jessen Bredeson
    black
    programming
    griffin
    ```
    >Arguments on the command line that contain spaces need to be quoted or the spaces escaped with backslashes (`\`)
5. **Make sure to keep your remote repository synced with your local repo. (ADD/COMMIT/PUSH)**
    ```sh
    git add ./aboutme.py ./aboutme2.py
    git commit -m 'Learn a little about me'
    git push origin master
    ```
        
        