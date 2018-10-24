#!/usr/bin/env python3

import sys
mi_dict = {}
mi = ""
for line in sys.stdin:
  line = line.rstrip("\n")
  line_elements = line.split("\t")
  #hint the MI tag is at the end of the line.
  mi = line_elements[-1]
  #print(mi)

  if mi in mi_dict:
    mi_dict[mi] += 1 #here you are just counting
    print(mi_dict[mi])
  else:
    mi_dict[mi] = 1 #start the party if you are the first one there

#now you can loupe through the dictionary and print the counts
for key in mi_dict:
  print(key,"\t",mi_dict[key])
