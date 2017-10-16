Problem Set Answers
===================

The original problem set questions are in **bold** and their answers in regular weight font.

1. **Log into your machine.**
    1. Log into your iMac through the standard macOS graphical user interface (GUI) by typing your password and pressing the <Enter> key.

    2. Use Finder (blue and white square face icon) in the Dock to navigate to the Applications directory. Expand by clicking on the rightward-facing arrow to the left of the folder icon the Utilities subdirectory, then double-click on the Applications icon.

        Alternatively, you could hold the Command button and press the space bar to open the Spotlight Search utility and type "terminal", then press <Enter>

2. **What is the full path to your home directory?**
    ```sh
    $ pwd
    /Users/admin
    ```
3. **Go up one directory?**
    If we want to move into the directory above (or parent to) the present working directory, we do not need to know what that directory is actually called, we can just use the shorthand: `..`
    ```sh
    $ cd ..
    ```
    * **How many files does it contain?**
        The following two problems require multiple subcommands strung together with pipe (`|`) characters to form one larger command. *Try gradually building the full command by adding each subcommnad and examining the output of each addition to understand how the inputs are being manipulated.* 
        
        The first subcommand uses `ls` to print the files and directories with fancy (`-F`) formatting, one file or directory per line (`-1` *i.e.*, number "one" flag). The second subcommand exploits the fact that the first subcommand appended a forward-slash (`/`) character to each directory, we can exclude all directories from the listing with the `grep` command to obtain only files. By default, `grep` will *select for* the pattern you give it, but we want to *exclude* the pattern, so we invert the match result with the `-v` flag. Finally, we want to count the number of items (*i.e.*, lines) that have made it through our `grep` filter, so we can use `wc` augmented with the `-l` flag to count only lines.
        ```sh
        $ ls -1 -F | grep -v '/' | wc -l
        ```
    * **How many directories?**
        To solve this problem set question, we perform a process very similar to the previous question. However, this time we do want to use `grep` to select for the pattern we are interested in (*i.e*. the `/` character), so we omit the `-v` flag. 
        ```sh
        $ ls -1 -F | grep '/' | wc -l
        ```
        or more succinctly, we can use the `-c` flag to have `grep` count for us:
        ```sh
        $ ls -1 -F | grep -c '/'
        ```
        
4. **Make a dirctory called `problemsets`.**
    ```sh
    $ mkdir problemsets
    ```
    
5. **Navigate into this new directory called problemsets. Verify that you are in the correct directory by using `pwd`.**
    ```sh
    $ cd problemsets
    $ pwd
    /Users/problemsets
    ```
    
6. **Use `wget` to copy [sequences.nt.fa](https://raw.githubusercontent.com/srobb1/pfb2017/master/files/sequences.nt.fa) from the web into your problemsets directory.**
    Control+click the sequences.nt.fa link and select the "Copy Link" option from the pop-up context menu. Then on the command-line, type:
    ```sh
    $ wget https://raw.githubusercontent.com/srobb1/pfb2017/master/files/sequences.nt.fa
    ```
    
7. **Without using a text editor calculate or report these qualities for the file `sequences.nt.fa`. This file can be found [here](https://raw.githubusercontent.com/srobb1/pfb2017/master/files/sequences.nt.fa)**
    * **How many lines does this file contain?**
        ```sh
        $ wc -l sequences.nt.fa
        ```
    * **How many characters? (Hint: check out the options of wc)**
        ```sh
        $ wc -c sequences.nt.fa
        ```
    * **What is the first line of this file? (Hint: read the man page of head)**
        ```sh
        $ head -n 1 sequences.nt.fa
        ```
    * **What are the last 3 lines? (Hint: read the man page of tail)**
        ```sh
        $ tail -n 3 sequences.nt.fa
        ```
    * **How many sequences are in the file? (Hint: use grep)**
        This problem question requires the use of `grep` in order to count the number of sequences in the file. Conveniently, every sequence begins with the `>` character and easy to search for; *however*, the `>` symbol also has special meaning to the Unix/Linux environment, so we must quote the character to tell Unix/Linux not to interpret it as the redirection symbol (or we clobber our file!):
        ```sh
        $ grep -c '>' sequences.nt.fa
        ```
        Or we may "escape" the character with a backslash (`\`):
        ```sh
        $ grep -c \> sequences.nt.fa
        ```
        
8. **Rename `sequences.nt.fa` to `cancer_genes.fasta`. (Hint: read the man page for mv)**
    ```sh
    $ mv sequences.nt.fa cancer_genes.fasta
    ```
   
9. **Copy this remote file: [cuffdiff.txt](https://raw.githubusercontent.com/srobb1/pfb2017/master/files/cuffdiff.txt) to your problemset directory.**
    Control+click the cuffdiff.txt link and select the "Copy Link" option from the pop-up context menu. Then on the command-line, type:
    ```sh
    $ wget https://raw.githubusercontent.com/srobb1/pfb2017/master/files/cuffdiff.txt
    ```
    
10. **Do the following to cuffdiff.txt**
    * **look at the first few lines of the file**
        ```
        $ head -n 3 cuffdiff.txt
        AC148152.3_FG006  AC148152.3_FG006  AC148152.3_FG006  Chr2:231237971-231241387  B73.s  Mo17.s  NOTEST  0.0125804  0          -1.79769e+308  -1.79769e+308  0.32736      1            no
        AC148152.3_FG008  AC148152.3_FG008  AC148152.3_FG008  Chr2:231209190-231213723  B73.s  Mo17.s  OK      5.83386    0.0236324  -5.50882       4.61461        3.93829e-06  0.000124139  yes
        AC148167.6_FG001  AC148167.6_FG001  AC148167.6_FG001  Chr7:11663430-11671232    B73.s  Mo17.s  OK      14.539     14.2519    -0.0199491     0.023067       0.981597     1.04126      no
        ```
    * **sort the file by log fold change 'log2(fold_change)', from highest to lowest, and save in a new file in your directory called sorted.cuffdiff.out**
        The log2(fold_change) column is the 10th column, so we use `sort`'s `-k` flag to tell `sort` that the 10th column should be used as the sort key. By default, `sort` sorts the file lexigraphically in ascending order, but we need to sort numerically. There are two versions of the numeric sort algorithm, `-n` for simple numeric value types (integers and decimals), and `-g` for handling general numeric types (integers, decimals, scientific floating point numbers, etc). If we look closesly, we will see that cuffdiff.txt contains numbers formatted in scientific notation, so we must use the general sort form. Additionally, we must include the `-r` flag to reverse the order of the sort (sort descending, not ascending).
        ```sh
        $ sort -k10gr cuffdiff.txt >sorted.cuffdiff.out
        ```
        * **sort the file (log fold change highest to lowest) then print out only the first 100 lines. Save in a file called top100.sorted.cuffdiff.out**
            ```sh
            $ sort -k10gr cuffdiff.txt >sorted.cuffdiff.txt | head -n 100 >top100.sorted.cuffdiff.out
            ```
    * **sort the file, print only first column. Get a unique list of the genes, then print only the top 100. Save in a file called differentially.expressed.genes.txt**
        The problem question wants a non-redundant list of names for the top 100 differentially expressed genes.
        
        We extend the command used to solve the previous problem question and extend it by extracting only the first column/field using `cut`:
        ```sh
        $ sort -k10gr cuffdiff.txt | head -n 100 | cut -f1 >differentially.expressed.genes.txt
        ```
        Now we must verify that there are, indeed, 100 unique gene names in differentially.expressed.genes.txt by sorting this file by its first (and only) column and unique-ifying the list with the `-u` option flag, then passing that to `wc` to count the number of unique gene names (lines) with the `-l` flag.
        ```sh
        $ sort -k1 -u differentially.expressed.genes.txt | wc -l
             100
        ```