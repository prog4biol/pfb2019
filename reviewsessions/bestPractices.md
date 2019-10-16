## Tips for Organized Coding

1. Naming directories

`mkdir pfb2019_SEW`

 - Keep directory names informative.
 - No spaces or special characters.
 - No extensions (e.g., .txt, .fasta)

2. Naming files

`vi rawSeqData.fasta`

•Keep file names informative.
•No spaces or special characters. 
•Use appropriate extensions. 

3. Naming scripts

`vi fastaParser.py`

•Keep file names informative.
•No spaces or special characters. 
•Use appropriate extensions.

###Examples for PFB 2019

`sew$ mkdir ProblemSet1`
`sew$ vi ps1.1.py`
`sew$ vi ps1.2.py`

4. Creating daily "readMe" files

`mkdir dailyReadMe`

•Take notes daily for ongoing projects for yourself to keep track. 
•One way to do this is keep a daily journal of your progress. Use it for successes, failures, random notes, specific end points. 

`vi 10Oct2019ReadMe.md`
`vi 12Oct2019ReadMe.md`

5. Comment your code. 

Sharing code is becoming more common and sometimes expected by journals. In order to maximize reproducibility, code that is shared publicly should be commented and accessible. 

```
#!/usr/bin/env python3
import sys

myString = 'sapiens, erectus, neanderthalensis'

print(myString)

myList = myString.split(', ') #splitting string on the comma and the space
print(sorted(myList)) #sorting my list; default is alphabetical
print(sorted(myList, key = len)) #sorting my list by length; must tell sorted to use length
```

##Changing your bash prompt

Create a beautiful prompt.

1. Go to ezprompt.net and create a beautiful prompt.
2. Type: `cd ~`
3. Type: `vi .bash_profile`
3. Paste code from ezprompt.net into your .bash_profile at the bottom.
4. Type: `source .bash_profile`

Create a beautiful VI experience.

1. Type `vi .vimrc`
2. Into your .vimrc file, type:

```
syntax enable #enables programming syntax and color change
set tabstop=2 #makes your tabs the size of 2 spaces
set number #adds numbers on the left side of your vi window
```

3. Save the file by typing `:wq`. 
4. At the command line, type `source .vimrc`
5. Open vi again and the changes should be saved. 
