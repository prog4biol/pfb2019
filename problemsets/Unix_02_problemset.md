# Unix 2 Problem Set


1. If you have not already done so, follow [Steps 1-3 in Unix: GIT for Beginners](https://github.com/srobb1/pfb2017#git-for-beginners). Here is a summary of those steps:
   - Create a GitHub Account and Click "New" to create a new repository.
   - Add info about your repository
   - Create a local (your machine) directory with `mkdir <dirname>` and set it up as a repository with `git init <dirname>`. Now link it to your remote repository with `git remote add`.

2. Move any files you created in Unix_01 Problem set to your local problemset git repository.

3. Add all the new files in your local repository to your remote repository
   - `git add  *` . You can use `git add <filename>` if you only want to add one file.
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

8. Using your text editor (nano is a good one to start with) create a fasta file and name it `mysequences.txt`. Make sure it ends up in your problem sets files directory.

This is fasta file format:
```
>seqName description
ATGGCGTCTTGGCCTTAAAAGCTC
```

9. ADD/COMMIT/PUSH `mysequences.txt` to your remote.


10. Create a directory called `fastas`.     (Hint: use mkdir)
11. Copy the fasta file that you renamed to `cancer_genes.fasta` to the fasta directory.
12. Verify that the file is within the fasta directory.  
13. Delete the the original file that you used for copying.  
14. Sync your remote repo with your local repo. Make sure to add each file you changed or use `git add all *`. Don't forget to commit and push.
15. Read the man page for `rm` and `cp` to find out how to remove and copy a directory.
16. Print out your history and redirect it to a file called `unixBasics.history.txt`
17. Open this file with your text editor and delete any lines you do not want to keep. See this [google search](https://www.google.com/search?rlz=1C5CHFA_enUS596US596&q=nano+delete+entire+line&oq=nano+delete+entire+line&gs_l=psy-ab.3..0j0i5i30k1.28765.29854.0.30351.7.6.0.0.0.0.186.526.0j3.3.0....0...1.1.64.psy-ab..5.2.362...0i13k1j0i7i5i30k1.0.Ub2zfH_lp_o) for info on delete entire lines in nano.
18. Make sure all your files are synced with your remote repository.
