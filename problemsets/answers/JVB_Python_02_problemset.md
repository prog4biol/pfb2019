Problem Set Answers
===================
1. **Use the Interactive Interpretor to test to see if you can find an 'ATG' in the following DNA string**:
    ```python
    In [0]: "ATG" in "GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA"
    Out[0]: False
    ```
    
2. **How about 'TTT'?**
    ```python
    In [1]: "TTT" in "GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA"
    Out[1]: True
    ```
    
3. **Save the DNA string to a variable and do 1 and 2 again.**
    ```python
    In [2]: dna = "GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA"
    In [3]: "ATG" in dna
    Out[3]: False
    In [4]: "TTT" in dna
    Out[4]: True
    ```

4. **In the interpretor use bool to test a variety of values like '', 0, 0.0, FALSE, false, True, true, 'True', 'False' to see if they evalue to True or False.**
    ```python
    In [5]: bool('')  # empty strings are False (have 0 length)
    Out[5]: False
    In [6]: bool(0)  # 0 is False, always
    Out[6]: False
    In [7]: bool(0.0)  # this is just a float of 0, still False
    Out[7]: False
    # 'FALSE' is not a defined variable, so python throws an Exception:
    In [8]: bool(FALSE)
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-6-34130d9d8ef7> in <module>()
    ----> 1 bool(FALSE)
    NameError: name 'FALSE' is not defined
    # 'false' is not a defined variable, so python throws an Exception:
    In [9]: bool(false)
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-7-3536571ee15f> in <module>()
    ----> 1 bool(false)
    NameError: name 'false' is not defined
    In [10]: bool(True)
    Out[10]: True
    # 'true' is not a defined variable, so python throws an Exception:
    In [11]: bool(true)
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-8-5435428d3bef> in <module>()
    ----> 1 bool(true)
    NameError: name 'true' is not defined
    
    In [12]: bool('True')  # 'True' a non-empty string, is True
    Out[12]: True
    In [13]: bool('False')  # 'False' is a non-empty string, is True
    Out[13]: True
    ```
5. **Using a text editor, write a script that**
    * **Assigns a value to a variable**
    * **Has a if/else statment in which:**
        * **It prints out a confirmation of truth if the value is true**
        * **It prints out "Not True" if the value is not true.**
    ```python
    #!/usr/bin/env python3
    
    input_datum = 3.14159  # pi
    if bool(input_datum) is True: 
        # adding the `is True' part above is not strictly necessary (but
        # it reads more nicely), as bool() returns `True' or `False', which
        # is all `if' really cares about
        print("True")
    else:
        print("Not True")
    ```
6. **Make sure to commit your changes along the way. You can wait until the end to push them to your remote repo, if you like, or you can do it now.**
    ```sh
    git add booltest.py
    git commit -m 'Initial commit of booltest.py'
    git push origin master
    ```
    
7. **Write a new script that does the same as the last question, but gets the value from the command line.**
     ```python
    #!/usr/bin/env python3
    
    import sys
    
    # remember, python loads sys.argv[0] with your script's name, so use
    # sys.argv[1] instead:
    input_datum = sys.argv[1]
    if bool(input_datum) is True:
        print("True")
    else:
        print("Not True")
    ```
    
8. **Create a script that has a if/elif/else statement that**
    * **Tests to see if a number is positive or negative**
    * **if it is positive, is it bigger or smaller than 50**
        * **if it is smaller, is it an even number**
        * **if it is larger, is it divisible by 3.**
    ```python
    #!/usr/bin/env python3
    
    import sys
    
    # the most flexible form of a number is a float, so cast the input value
    # to be of float() type. 
    number = float(sys.argv[1])
    if number < 0:
        print("number is negative")
    elif number > 0:
        print("number is positive")
        if number < 50:
            # test if a value is even by dividing by two and testing if there is
            # any remainder. Even numbers should have no remainder. This can be
            # achieved in one line with the modulo operator:
            if number % 2 == 0: 
                print("less than 50, and even")
            else:
                print("less than 50, and odd")
        elif number > 50:
            # testing to determine if a number is divisible by three is the same
            # as testing if a number is even (divisible by two)
            if number % 3 == 0:
                print("greater than 50, and divisible by 3")
            else:
                print("greater than 50, and not divisible by 3")
        elif number == 50:
            # the problem statement didn't ask us to handle numbers when they
            # are equal to 50, so...
            pass
    ```
    
9. ADD/COMMIT/PUSH
    ```sh
    git add numbertest.py
    git commit -m 'Initial commit of numbertest.py'
    git push origin master
    ```