#!/usr/bin/env python3

# create a new empty dictionary
nt_count={}

# loop example from loops lecture
dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
for nt in dna:
 
  # is this nt in our dictionary?
  if nt in nt_count:
     # if it is, lets increment our count
     previous_count = nt_count[nt]
     new_count = previous_count + 1
     nt_count[nt] = new_count
  else:
    # if not, lets add this nt to the dictionary and make count 1
    nt_count[nt] = 1;

print(nt_count)
