#!/usr/bin/env python3

# 1. Write a script that calculates the AT content of the DNA string
#    found below. AT content is the proportion of bases that are either
#    A or T. You will need to use some mathmatical functions as well as
#    a python function. It is ALWAYS a good idea to test your code with
#    test data. For example, the below sequence is long and you don't 
#    know for sure how many As and Ts are present. Test your codee with
#    a DNA string that you KNOW the correct answer. In AATTGGCCA you 
#    know you have 3 As and 2 Ts.

DNA = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG"

content_AT  = DNA.count('A')  # first count A's
content_AT += DNA.count('T')  # then add T counts

print("AT content: {0:.2f}".format(content_AT / len(DNA)))

# 2. Now add in lines of code to calculate GC content of the above DNA
#    string. Run with test data first!!

# GC content is just 1 - AT content, so without performing any redundant
# operations:
print("GC content {0:.2f}".format(1 - content_AT / len(DNA)))

# 3. Write a new script that prints out the reverse complement of the
#    above DNA string. Hint for reverse

# In string (and list) slice notation, there are three fields separated
# by colons: start index, end index, index step, e.g. string[start:end:step].
# In order to reverse a string we could tell python to step through the
# string one index at a time in the negative direction (i.e. -1). Next, we
# standardize the character case to lower-case:
DNAreverse = DNA[::-1].lower()

# In order to complement a sequence with the str.replace() function, we
# need to replace each nucleotide type at a time, which requires 4 passes
# through the string. If after the first pass we've replaced 'A' with 'T',
# then attempt to replace 'T' with 'A', there will be no 'T' characters
# left in the string! They all will have been replaced with 'A'. A simple
# work-around is to use character case to block replacement in a later pass:
DNArevcomp = DNAreverse.replace('a','T')
DNArevcomp = DNArevcomp.replace('t','A')
DNArevcomp = DNArevcomp.replace('g','C')
DNArevcomp = DNArevcomp.replace('c','G')

# now our string is all uppercase. Win!

print(DNA)
print(DNArevcomp)

# run this script, piping the output to less -S to visualize:
# ./JVB_Python_03.1.py | less -S

# 5. Write a script to find the start position of an EcoRI in the above
#    sequence. Remember DNA sequences start with a 1 and a python string
#    starts with a 0. Run with test data first.

print("EcoRI at position {0:d}".format(DNA.find("GAATTC")+1))

# 6. What is the location in the DNA string of the EcoR1 cut site? Calculate
#    the first and last nucleotides of each restriction fragment.
frag1_beg = 1
frag1_end = DNA.find("GAATTC")+1
frag2_beg = frag1_end + 1
frag2_end = len(DNA)

print("EcoRI restriction fragments: {0:d}-{1:d}, {2:d}-{3:d}".format(
    frag1_beg, frag1_end, frag2_beg, frag2_end))

# 7. Extract the the restricion fragments. Print each fragment along with its
#    postion in the whole DNA sequence and its length. Use string formating to
#    format your print statemnt.
frag1_len = len(DNA[:frag1_end])
frag2_len = len(DNA[frag1_end:])
print("{0:s}\t{1:d}\t{2:d}".format(DNA[0:frag1_end], frag1_beg, frag1_len))
print("{0:s}\t{1:d}\t{2:d}".format(DNA[frag1_end:], frag2_beg, frag2_len))

# 8. Create a list and add each fragment to it.
#   for the fun of it, let's physically knick the cutsite then split on that
#   site to form the list:
knicked_DNA = DNA.replace('GAATTC','G^AATTC')
fragments = knicked_DNA.split('^')

# 9. Sort the list.
#    the list.sort() function sorts in-place, no need to assign an new variable
fragments.sort()

# 10. Sort the list by fragment length. Check out documentation of the key
#     argument.
# the sort() fuction takes a `key' keyword argument that accepts a function that
# returns data to sort on. Internally, Python does the following:
#  1) iterates over each item in our list, calling the function we passed it
#     via `key',  storing these values in a new list as 2-tuples of
#     (value, item)
#  2) Python, being intelligent, sorts this new list based on the value in the
#     tuple
#  3) Python then loops over our list again and unpacks the tuples to give us
#     our list of items sorted by the value. This whole process is very fast.
fragments.sort(key=len)

# 11. Interogate the difference between these two ways to copy a list. Both are
#     not correct.
#     * alter the lists after the "copy" by adding a new element to the list
#        This way of "copying" a list actually creates a new pointer/reference
#        to the same object. When you modify either variable, you're modifying
#        both!
#
#     * print the lists before and after you alter the "copy"
#        the list.copy() method is actually copying the data within the list,
#        *however*, copy() is performing a shallow copy of the data, not a deep/
#        recursive copy; meaning, if you have a list of lists and you modify
#        one of the nested lists, that nested list is copied in both:
#        L = [['foo'],['bar']]
#        K = L.copy()
#        K[0][0] = "baz"
#        L
#        [['baz'], ['bar']]
