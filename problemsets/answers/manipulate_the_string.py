#!/usr/bin/env python3

dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'

ecori = "GAATTC"

#computers start counting at zero while humans start counting at one. This is good to remember to avoid "off by one" errors. These kinds of errors are pervasive in bioinformatics, and hard to debug because the code runs fine.
zero_based_ecori_pos = dna.find(ecori)
one_based_ecori_pos = zero_based_ecori_pos + 1 

#the cut is one base into the site G^AATTC so you add one to get the cut position
one_based_ecori_cut_pos = one_based_ecori_pos + 1 
zero_based_ecori_cut_pos = zero_based_ecori_pos + 1 

#use the zero based coordinates to work in python. Get the nucleotides at the begining and end of the fragments
begin_of_left_frag = dna[0]
end_of_left_frag = dna[zero_based_ecori_cut_pos -1]
begin_of_right_frag = dna[zero_based_ecori_cut_pos]
end_of_right_frag = dna[-1]

#get the sequence and print it, remember to use the zero based coordinates here
left_frag_seq = dna[0:zero_based_ecori_cut_pos]
right_frag_seq = dna[zero_based_ecori_cut_pos:]

# print it like this Fragment\tPostion\tLength using format
tabed_line="{}\t{}\t{}"
left_frag_start = "1"
right_frag_start = one_based_ecori_cut_pos

#print(tabed_line.format(left_frag_seq, left_frag_start, len(left_frag_seq)))
#print(tabed_line.format(left_frag_seq, right_frag_start, len(right_frag_seq)))

frags = []
frags.append(left_frag_seq)
frags.append(right_frag_seq)

s_frags = sorted(frags)

#print("unsorted", frags)
#print("sorted", s_frags)

s_by_len_frags = sorted(frags, key=len)

print("unsorted", frags)
print("len sorted", s_by_len_frags)
