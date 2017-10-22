
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
  and dir()
  
  
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

  
Advanced Unix
  awk
```
BEGIN { print "File\tOwner"}
{ print $8, "\t", $3}
END { print " - DONE -" }
```
  
Workflows, and approaches
  saving time: assume your data is corrupted
  saving effort: google searches
  
Data
  consistency, corruption, sanity checks
  NGS data generation: illumina, pacbio
  formats - see biopython
  (un)compression
  
Bioinformatics How do I ...?
  filtering sequence data: 
  QC sequence data:
  genome assembly
  sequence search: blast
  alignment: gmap, gsnap, bwa mem,
  resequencing, variant calling
  finding genes
  predicting gene function
  view genes/genomes -> GMOD coming later
  databases store large data for easy searching and retrieval
  public databases
  write web apps
  tell if my code is slow
  
