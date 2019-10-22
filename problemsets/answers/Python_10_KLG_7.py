#!/usr/bin/env python3

# 7. Pipelines:  
#   a. Create a script that runs a command with `subprocess.run`.    
#   b. Check the exit status  
#   c. If exit status is good, run a second command.  

import subprocess
import sys


fasta  = sys.argv[1]

## check if there are records in the fasta file

rtn    = subprocess.run(['grep', ">", fasta], stdout=subprocess.PIPE, check = True)  # specify you want to capture STDOUT

## if the previos command works, continue on
if rtn.returncode == 0:

    ## count the number of FASTA records
    rtn    = subprocess.run(['grep', "-c", ">", fasta], stdout=subprocess.PIPE, check = True)  # specify you want to capture STDOUT

    ## pull out the output
    bytes  = rtn.stdout
    stdout = bytes.decode('utf-8')

    ## break up the output
    lines = stdout.splitlines()
    print('Number of records in FASTA:', lines[0])
