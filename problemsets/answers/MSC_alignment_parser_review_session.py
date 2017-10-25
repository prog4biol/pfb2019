#!/usr/bin/env python3

import sys
field_names = ['query', 'subject', 'percent_identity', 'alignment_length', 'mismatches', 'gap_opens', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bit_score']

list_of_files = sys.argv[1:]
print("input_file", "subject", "pi", "e", sep="\t")
for input_file in list_of_files:
    file = open(input_file, "r")
    for line in file:
        line = line.rstrip()
        if not line.startswith('#'):
            line_list = line.split("\t")
            align_dict = dict(zip(field_names, line_list))
#            print(input_file, align_dict['subject'], align_dict['percent_identity'], align_dict['evalue'], sep="\t")
                  
            print(line_list[2:4])
