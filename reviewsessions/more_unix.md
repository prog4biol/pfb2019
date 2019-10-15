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


`paste file1.txt file2.txt`

This will join two files line by line and display on the screen

`column -t |less -S`

Makes a messy table have clean columns and presents it with an easily viewable scrolling display 

`zgrep -v "##" file.vcf.gz| column -t |less -S`

Display a vcf without all the header garbage

