#!/usr/bin/env python3

seq_read  = open("../files/seq.nt.fa","r")
seq_write = open("../nt.counts.txt","w")

total_nts = 0
for line in seq_read:
  line = line.rstrip()
  nt_count = len(line)
  total_nts += nt_count
  seq_write.write(str(nt_count) + "\n")

seq_write.write("Total: " + str(total_nts))

seq_read.close()
seq_write.close()

