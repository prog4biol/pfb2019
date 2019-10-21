#!/usr/bin/env python3

# 9. Download this file: ftp://ftp.neb.com/pub/rebase/bionet.txt of enzymes and their cut sites to fill a dictionary of enzymes paired with their recognition patterns. Be aware of the header lines, and be aware of how the columns are delimited. You'll modify this script in the next question.

enzyme_file = open('bionet.txt', 'r')


enzyme_dict = {}
with enzyme_file as f:
    lines_after_10 = f.readlines()[10:]
    for line in lines_after_10:
        items = line.split()
        print(items)
        try:
            if len(items) == 3:
                key = "".join(items[0:2])
            else:
                key = items[0]
            enzyme_dict[key] = items[len(items)-1]
        except:
            print('Offending line contains:', items)


print(enzyme_dict)



# 10. Write a script which takes two command line arguments: the name of an enzyme and a fasta file with a sequence to be cut. Load a dictionary of enzyme names and cut sites from the code you developed in question 9.
#    If the enzyme is present in the dictionary, and can cut the sequence, print out:
#      - the sequence, annotated with cut sites
#      - the number of fragments
#      - the fragments in their natural order (unsorted)
#      - the fragments in sorted order (largest to smallest)

