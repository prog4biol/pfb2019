# STAR RNA-seq aligner



Tutorial

Available on github at `https://github.com/alexdobin/STAR`



```
cd ~/git
sprochnik:~/git% git clone https://github.com/alexdobin/STAR.git

```

[] download ref fasta

[] download ref annotation gff

[] make index

```
mkdir genomes
~/git/STAR/bin/MacOSX_x86_64/STAR --runThreadN 4 --runMode genomeGenerate --genomeDir ./genomes --genomeFastaFiles ./hsa.HG38.chr22.fa

```

