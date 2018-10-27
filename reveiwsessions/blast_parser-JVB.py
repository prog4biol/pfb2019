#!/usr/bin/env python3

import re
import sys

blast_report_filename = sys.argv[1]

blast_report_fileobj = open(blast_report_filename, 'r')

query_info = dict()


is_query_length = True
for line in blast_report_fileobj:
    line = line.rstrip()

    if line.startswith('Query='):
        match = re.search(r'Query= (\S+)', line)
        if match is not None:
            query_info['query_name'] = match.group(1)
            
        else:
            sys.stderr.write("Bad Query name pattern, this should never happen\n")

    elif line.startswith('Length='):
        match = re.search(r'Length=(\d+)', line)
        if match is not None:
            if is_query_length:
                query_info['query_length'] = int(match.group(1))
                is_query_length = False
            else:
                query_info['subject_length'] = int(match.group(1))
        else:
            sys.stderr.write("Bad Query Length pattern, this should never happen\n")

    elif line.startswith('>'):
        match = re.search(r'>(\S+)', line)
        if match is not None:
            query_info['subject_name'] = match.group(1)
        else:
            sys.stderr.write("Bad Subject Length pattern, this should never happen\n")

    elif line.startswith(' Score ='):
        match = re.search(r'Expect = ([0-9eE\.\-]+)', line)
        if match is not None:
            query_info['expect'] = match.group(1)

        else:
            sys.stderr.write("Bad Expect pattern, this should never happen\n")
            
    elif line.startswith(' Identities ='):
        match = re.search(r'Identities = (\d+/\d+).+?Positives = (\d+/\d+)', line)
        if match is not None:
            query_info['identities'] = match.group(1)
            query_info['positives'] = match.group(2)

            break
        else:
            sys.stderr.write("Bad Expect pattern, this should never happen\n")

            
print(query_info)
