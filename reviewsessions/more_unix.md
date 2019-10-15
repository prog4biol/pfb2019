Here are some of the TAs and Instructors favorite or most used unix commands


__Sofia__

`ls -lt | head`

list the contents of your directory with all the information sorted by most recent at the top, but only show me the top 10.



`perl -pe s/\r/\n/g badfile > newfile`

Sometimes you have carriage returns instead of newline and you want to replace all of them. This command replaces all \r (carriage returns) with \n (newlines). The old file is not changed, but the new file has the changes.



`date ; someCommand ; date`

This will print out the date and time before you run some script and after. Now you can see how long it took



`comm -[1][2][3] file1 file2`

Compares two sorted files and prints out content depending on the flags



`comm -3 file1 file2`

`-3` will print out only the shared lines
`-1` will prit out the lines unique to file1
`-2` will pritn out the lines unique to file2



__Daniel__

test
test


__Jessen__
`cat badfile | tr '\r' '\n' >goodfile`

Sometimes you have carriage returns instead of newline and you want to replace all of them. This command replaces all \r (carriage returns) with \n (newlines). The old file is not changed, but the new file has the changes.


`find . -size +1g`

Recursively find files 1 Gb in size or larger.


`alias ll='ls -lGgotrh'`

Create a command alias to `ll` to pretty print files and directories with color, owner, group, and permissions.


`fold -w 100 one-line.fasta >line-wrapped.fasta`

Wrap the lines of a fasta file to 100 bp wide.


cat input.fastq | paste - - - - | cut -f1,2 | tr '@\t' '>\n' >output.fasta`

Convert a FASTQ file to FASTA file.

