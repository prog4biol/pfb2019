
# Bioinformatics and Useful Tools

> Mike is covering NGS; scott GMOD etc
> Deb is covering genome assembly

### Getting help
  pydoc
  google 'python3 list comprehensions`
  https://docs.python.org/3/    -> Quick search
  inside python interactive shell
```python
>>>help()
```
Just like for `man`, help text appears inside a pager like `more` or `less`. 
space -> next page
b -> back a page
return -> next line
/ -> search for a string
q quits the pager

```
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
...
|  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
...
```
  and `dir()`


```  
  >>> help(str.split)

Help on method_descriptor:

split(...)
    S.split(sep=None, maxsplit=-1) -> list of strings
    
    Return a list of the words in S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are
    removed from the result.
(END)

```


## Advanced Unix
### awk

awk is a simple unix utility for reformatting text files. An awk script would look like this

```
BEGIN { print "File\tOwner"}   # block executed before main script
{ print $9, "\t", $3}          # main script
END { print " - DONE -" }      # block executed after main script
```

You could run it like this `awk table.awk`. Each column (whitespace-separated) in the input appears in your script as $1, $2, $3 etc. A bit like sys.argv in python.

Let's ignore the BEGIN and END blocks for now.

How could you take a long file listing and print out the owner of each file?

```bash
% ls -l
-rw-r--r--  1 simonp  staff  312 Oct 20 11:05 scope_global.py
-rw-r--r--  1 simonp  staff  201 Oct 20 11:03 scope_global.py~
-rw-r--r--  1 simonp  staff  323 Oct 20 10:40 scope_w_function.py
-rw-r--r--  1 simonp  staff  210 Oct 20 10:33 scope_w_function.py~
-rw-r--r--  1 simonp  staff    5 Oct 15 14:15 test.nt.fa
-rw-r--r--  1 simonp  staff  103 Oct 17 19:27 while.py
-rw-r--r--  1 simonp  staff  160 Oct 17 19:27 while_else.py

```

Here are the column variables explicitly. This is not shell output. Just a picture.

```
$1         $2 $3      $4     $5  $6  $7 $8    $9
-rw-r--r--  1 simonp  staff  160 Oct 17 19:27 while_else.py
```

We want to print the file and the owner. Find the variables. The order can be whatever we want. The awk part would look like this 

`awk '{print $9, "\t" , $3 }'`

How do we get the long listing? `ls -l`

Put these together with our friend pipe `|`

```
% ls -l | awk '{print $9, "\t" , $3}'
scope_global.py 	 simonp
scope_global.py~ 	 simonp
scope_w_function.py 	 simonp
scope_w_function.py~ 	 simonp
test.nt.fa 	 simonp
while.py 	 simonp
while_else.py 	 simonp

```



### $PATH



### alias

Here's a way to save typing

`alias` is a unix comand that goes in your ~/.profile file. Make one with emacs if you don't have one already. 

```bash
alias ll='ls -l'
alias lr='ls -ltrh'
```

To get these changes, `source ~/.profile` or open a new window in terminal. Now you can type `lr`



Workflows, and approaches
  saving time: assume your data is corrupted
  saving effort: google searches

Data
  consistency, corruption, sanity checks
  NGS data generation: illumina, pacbio
  formats - see biopython
  (un)compression

## Bioinformatics How do I ...?
### filtering sequence data: 
#### QC sequence data:
### genome assembly
### sequence search: blast
### alignment: gmap, gsnap, bwa mem,
### resequencing, variant calling
### finding genes
### predicting gene function
### view genes/genomes -> GMOD coming later
### databases store large data for easy searching and retrieval
### public databases
### write web apps
### debug my script

Run your script with the debugger module `pdb` for python debugger. Not very sophisticated, but very useful. It starts an interactive debugger that's a bit like the python interactive shell, but you are inside your script. 

We were doing this
```bash
% python3 fasta_sequence.py
```
Now we add `-m pdb` so it becomes
```bash
% python3 -m pdb fasta_sequence.py
```

Good idea to make alias for this in .profile


### write bigger python coding projects? PyCharm
### tell if my code is slow

