
# rerun if any changes are made to the # ## ### #### in the README.md
START=`grep -n Instructors ../README.md | tail -1 | awk -F ':'  {'print $1'}`
tail +$START ../README.md | ./gh-md-toc - > toc.md



## copy the contents of toc.md to README.md to create a TOC with more depth
