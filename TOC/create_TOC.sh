
# rerun if any changes are made to the # ## ### #### in the README.md
head -n 8 ../pfb.md > toc.md
START=2
tail +$START ../unix.md | ./gh-md-toc - | perl -p -e 's/\(#/\(unix.md\/#/' >> toc.md
tail +$START ../pfb.md  | ./gh-md-toc - | perl -p -e 's/\(#/\(pfb.md\/#/' >> toc.md
tail +$START ../workshops/README.md | ./gh-md-toc - | perl -p -e 's/\(#/\(workshops.md\/#/' >> toc.md


## copy the contents of toc.md to README.md to create a TOC with more depth
