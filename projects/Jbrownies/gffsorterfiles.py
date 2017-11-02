#!/usr/bin/env python3

import sys

fh = open(sys.argv[1], 'r')
#maker_file = open('maker.txt', 'a')


for line in fh:
	if not line.startswith('#'):
		line = line.rstrip()
		col = line.split('\t')
		if col[1] is not '.':
			outfile = open(col[1]+'.gff', 'a')

			outfile.write(line+'\n')
			outfile.close()

fh.close()			
		
