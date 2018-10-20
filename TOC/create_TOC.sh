
# rerun if any changes are made to the # ## ### #### in the README.md
head -n 6 ../pfb.md > toc.md
START=2
tail +$START ../unix.md | ./gh-md-toc - >> toc.md
tail +$START ../pfb.md | ./gh-md-toc - >> toc.md



## copy the contents of toc.md to README.md to create a TOC with more depth
