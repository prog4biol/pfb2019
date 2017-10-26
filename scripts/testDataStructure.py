
#!/usr/bin/env python3

from Bio import SeqIO
fastas = SeqIO.to_dict(SeqIO.parse('files/sequences.nt.fa', 'fasta'))

records = [] #outermost data structure

for id in fastas:
    print(id)
    summary = {} #dict for this sequence
    seq = str(fastas[id].seq)
    acount = seq.count('A')
    ccount = seq.count('C')
    counts = {'A' : acount, 'C' : ccount } # details
                                          # on this sequence
    summary['id'] = id
    summary['counts'] = counts
    summary['desc'] = fastas[id].description

    records.append(summary)

print('Loaded these records')
print(records)


