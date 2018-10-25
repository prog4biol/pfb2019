# Project Ideas



# 1 DNA Assembler

Write a simple De Bruijn graph-based assembler for DNA sequences that takes kmer- length and other parameters as inputs. 



TA: 

Students:













# 2 Protein evolution

Visualize how the classes and localization of human proteins emerged over time

 o   For (a set of) human proteins, estimate the evolutionary age by detection of orthologs

§  Using <https://www.orthodb.org/> or some other similar tool

o   Classify the proteins based on GO terms

§  Function

§  Molecular class

§  Subcellular location

o   Visualize how the distributions of GO terms has changed over evolutionary time

o   BONUS ROUND: find proteins that share a similar evolutionary age as a queried protein -proffer a guess as to the function based on distinguishing features from that time

 Second Bonus round: add in a prediction of indel possibility (see paper describing the compactness of a residue (it’s Ooi number) here   <https://www.ncbi.nlm.nih.gov/pubmed/3818558>)



TA: 

Students:

















# 3 Evolution Simulation Program 

Create a program that simulates virtual people (veeples) with typified behavior and families. Veeples will have genomes made up of fixed length strings (genes) with associated fitnesses that can be passed on the to the next generation if they successfully mate (so we will have ‘male’ and ‘female’ veeples). 

Veeples will have different evolutionary strategies (e.g. fight, forage, find a mate, care for family), which translates to numerical outcomes with each interaction/strategy similar to game theory. Interactions between veeples will occur randomly, until mating successfully occurs - creating a new veeple. Ideally, the simulation would keep track of relatedness (e.g. F statistic, parent-child), and veeples might be able to change tactics based on this. 

Upon mating the veeples genes will go through a process similar to meiosis, which can contain processes such as recombination and the generation of mutations. Newly created alleles will be assigned a fitness score when created. 

Another potential layer of sophistication would be cut-offs for mating/death. For example, perhaps foraging, winning fights, or having family care for you would add to your ‘fitness’ (from whatever baseline is determined by your genes). If your fitness goes above a certain level any mating attempt will be successful, otherwise mating attempts will not be, and if one’s fitness drops low enough (from losing fights, failed mating attempts, ‘bad’ genes), they will die. 

Initial inputs into the game will include parameters such as number of veeples, number of iterations. Possible additional inputs could include parameters such as number (or percent) of veeples with a given strategy, mutation rates, recombination frequencies, ‘payouts’ for fighting/foraging/familial care, which otherwise would be set to some default. The inputs could be read in by a simply formatted text file. 

Initial outputs would be changes in allele frequencies (including new alleles created), changes in population size. Other ‘bonus’ outputs might include ‘winning’ strageties (i.e. stragety played most frequently by whatever group expanded the most), amount of familal care, foraging, fighting, etc. The output would also be a text file. 

Consider making the steps in the simulator interactive so a user can decide whether to forage, fight, get cared for etc. This would turn the simulator into a turn-based game. This could be an option at run time.



TA: 

Students:













# 4 Sound idea



When DNA sequences are input into the prompt, the program will translate them into codons. The 20 unique codons and the stop codon (21 total) will then be converted into musical notation which will be played using a third party software. Twenty one codons will span one and a half octaves plus sharps and a pause. The program will also have BLASTed the sequence to find the most likely gene the sequence originates from so that in the next prompt the user can choose to play the corresponding DNA-song for the references (human, yeast, grape). 

The program will also have the reverse functionality. When a song (in music letters only) is submitted or selected from a pre-set list of songs, it will convert the musical notes to amino acids then DNA. This will then be BLASTed to find the gene with the highest E-value and output in a fasta-style file with a header detailing the organism and gene name. The inputted song will also be projected onto a pre-existing PCA containing songs from a variety of genres to determine potential genre-population. PCA will be printed to screen and saved to a file. 

PCA details: plotting parameters might include codon composition, frequency, type, DNA GC content, year of song composition, etc





TA: 

Students:















# 5 RNA-seq pipeline

Construct a python wrapper to run RNAseq on multiple samples using STAR & DESeq and kallisto and sleuth. Compare two pipelines.

### 

TA: 

Students:















 








