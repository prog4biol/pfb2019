##Tips for Organized Coding

1. Naming directories

`mkdir pfb2019_SEW`

-Keep directory names informative.
-No spaces or special characters.
-No extensions (e.g., .txt, .fasta)

2. Naming files

`vi rawSeqData.fasta`

-Keep file names informative.
-No spaces or special characters. 
-Use appropriate extensions. 

3. Naming scripts

`vi fastaParser.py`

-Keep file names informative.
-No spaces or special characters. 
-Use appropriate extensions.

###Examples for PFB 2019

`sew$ mkdir ProblemSet1`
`sew$ vi ps1.1.py`
`sew$ vi ps1.2.py`

4. Creating daily "readMe" files

`mkdir dailyReadMe`

-Take notes daily for ongoing projects for yourself to keep track. 
-One way to do this is keep a daily journal of your progress. Use it for successes, failures, random notes, specific end points. 

`vi 10Oct2019ReadMe.md`
`vi 12Oct2019ReadMe.md`

5. Comment your code. 

-Sharing code is becoming more common and sometimes expected by journals. In order to maximize reproducibility, code that is shared publicly should be commented and accessible. 

`#!/usr/bin/env python3`
`import sys`
`myString = 'sapiens, erectus, neanderthalensis'`
`print(myString)`
`myList = myString.split(', ') #splitting string on the comma and the space`
`print(sorted(myList)) #sorting my list; default is alphabetical`
`print(sorted(myList, key = len)) #sorting my list by length; must tell sorted to use length`

##Unrelated fun & useful stuff

1. Create a beautiful prompt.

-Go to ezprompt.net.
-Create a beautiful prompt.
-Add (or create) a .bashrc or .bash_profile
-Source .bashrc or .bash_profi

2. Create a beautiful VI experience

`vi .vimrc`

Into your .vimrc file, type:

`syntax enable`
`set tabstop=2`
`set number`

Save the file. At the command line, type:

`source .vimrc`

Open vi again and the changes should be saved. 
