#!/usr/bin/env python3

file = open("./review_session_2_loops_dicts.gff3", 'r')


genes = {}
for line in file:
    if not line.startswith('##'):
        entry = line.rstrip().split('\t')
        attributes = entry[8].split(';')
        for attr in attributes:
            name, genename = attr.split('=')
            if name == 'Name':
                genes[genename] = entry[6]

print(genes)
