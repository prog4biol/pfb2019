##1. How do we explain the difference between methods vs functions? How do you know if you need a method or a function?  
###Just look it up...
That is what I do.

```
str = "some string"
str_length = len(str)
cap_str = str.capitalize()
```

##2. How do we explain the use of `with`? I looked it up and it is pretty complicated explaination of try/catch/always closing the file.  
###This is the way you open a file...

```
file = "somefile.txt"
with open(file,"r") as f
```
