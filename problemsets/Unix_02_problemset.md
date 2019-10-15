# Unix 2 Problem Set


1. If you have not already done so, follow [Steps 1-3 in Unix: GIT for Beginners](https://github.com/prog4biol/pfb2019#git-for-beginners). Here is a **summary** of those steps, **Please go to lecture for detailed steps**:
   NOTE: Don't create a repository inside of another repostitory.
   - Create a GitHub Account and Click "New" to create a new repository.
   - Add info about your repository
   - Please see the lecture notes for more detailed steps. In summary you will be doing the following: Create a local (your machine) directory with `mkdir <dirname>`, move into the new directory with `cd <dirname>` and set it up as a repository with `git init`. Now link it to your remote repository with `git remote add`.
   
   
   Don't `git init` in your home directory. Make a new directory (something like pfb_problemsets or problemsets or problem_sets), change directory into the new directory, then `git init` 

2. Move any files you created in Unix_01 Problem set to your local problemset git repository.

3. Add all the new files in your local repository to your remote repository
   - `git status` to see all the files you need to add
   - `git add <filename>`  or  `git add <filename1> <filename2> <filename3> ...`  
   - `git commit -m 'adding previous problem set files'`
   - `git push`
   - Visit the your GitHub repository website (on github.com) and see the files from your local repository that you just pushed up to your remote repository.

4. If you are tired of typing your github username and password create and add an ssh key to your github account. Information can be found [here](https://help.github.com/articles/connecting-to-github-with-ssh/) on github.com. Follow the instructions for these two steps in the turorial.
   - [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) 
   - [Adding a new SSH key to your GitHub account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account)

5. Create a directory call `files` in your ProblemSets directory. 

6. Move the file you renamed from `sequences.nt.fa` to `cancer_genes.fasta` to your `files` directory

7. ADD/COMMIT/PUSH `cancer_genes.fasta` to your remote repository
  - `git add files/cancer_genes.fasta`
  - `git commit -m 'adding cancer_genes.fasta'`
  - `git push`
  - Visit the your GitHub repository website (on github.com) and see the file from your local repository that you just pushed up to your remote repository.

8. Using your vi text editor create a fasta file and name it `mysequences.txt`. Make sure it ends up in your problem sets files directory.

This is fasta file format:
```
>seqName description
ATGGCGTCTTGGCCTTAAAAGCTC
GGCGTCTTGGCCTTAAAAGCTCAT
ATTCTTGGCCTTAAATTGGCCTTG
```
  - add 10 lines of sequence
  - delete a line
  - insert a new line at line 4
  - Copy line 5
  - Paste this line above line 2
  - set to view line numbers
  - Cut line 3 and paste below line 6
  - Go to line 4
  - delete a line
  - undo your last delete
  - search for `CTT`
  - find next occurance of `CTT`
  - Save and exit


9. ADD/COMMIT/PUSH `mysequences.txt` to your remote.


10. Create a directory called `fastas`.     (Hint: use mkdir)
11. Copy the fasta file that you renamed to `cancer_genes.fasta` to the fasta directory.
12. Verify that the file is within the fasta directory.  
13. Delete the the original file that you used for copying.  
14. Sync your remote repo with your local repo. Make sure to add each file you changed or use `git add <filename>`. Don't forget to commit and push.
15. Practice with `git rm`
  - Create a file named `oops` and add a few characters of content.
  - Save and Exit. 
  - Add/Commit/Push this file 
  - `git rm oops` 
  - `git commit -m 'removing oops'`
  - `git push`
16. Practice with `rm`. Can you spot the little difference from `git rm`
  - Create a file named `oops2`. add some content. save and exit
  - Add/Commit/Push this file
  - `rm oops2`
  - `git add oops2`
  - `git commit -m 'removing oops2'`
  - `git push`
17. Imagine this: You created a file, `git add` it, but then realize you don't want to commit it. What do you do? [from google search](https://stackoverflow.com/questions/348170/how-do-i-undo-git-add-before-commit)
  - Create a file named `never`. 
  - `git add never`
  - `git reset never`
18. Read the man page for `rm` and `cp` to find out how to remove and copy a directory.
19. Print out your history and redirect it to a file called `unixBasics.history.txt`
20. Open your history file with your text editor and delete any lines you do not want to keep. See this [google search](https://www.google.com/search?rlz=1C5CHFA_enUS596US596&q=vi+delete+entire+line&oq=vi+delete+entire+line&gs_l=psy-ab.3..0j0i5i30k1.28765.29854.0.30351.7.6.0.0.0.0.186.526.0j3.3.0....0...1.1.64.psy-ab..5.2.362...0i13k1j0i7i5i30k1.0.Ub2zfH_lp_o) for info on deleting entire lines in vi.
21. Make sure all your files are synced with your remote repository. (`git status`)
