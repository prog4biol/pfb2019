# STAR RNA-seq aligner



## Tutorial



### Installation

STAR is available on github at `https://github.com/alexdobin/STAR`

Installation is very easy.

You will need to log into your mac workstation as the `admin` user. 

You should have a `git` directory in your home directory for all the repos you have cloned. It's a good idea to organize your code like this. Clone the STAR repository into this directory.

```
% cd ~/git
% git clone https://github.com/alexdobin/STAR.git

```

STAR comes with a precompiled binary that is ready to run on OS X (also available for linux)

```
% cd STAR/bin
% ls
Linux_x86_64		Linux_x86_64_static	MacOSX_x86_64
% cd MacOSX_x86_64
# run the STAR program in this directory
% ./STAR    
Usage: STAR  [options]... --genomeDir REFERENCE   --readFilesIn R1.fq R2.fq
Spliced Transcripts Alignment to a Reference (c) Alexander Dobin, 2009-2015

### versions
versionSTAR             020201
...
```

A typical and easy way to install code on a unix system is to put the binary in the `/usr/local/bin/` directory. Make one if it doesn't exist yet.

```
% sudo mkdir /usr/local/bin/
```

and copy the STAR program to `/usr/local/bin`

```
% sudo cp STAR /usr/local/bin
```

Add this directory to your path if you don't see it if you type this

```
%echo $PATH
/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin
```

In a text editor, add a line to `~/.profile` like this

```
export PATH='/usr/local/bin:$PATH'
```

now type `source ~/.profile` and then `echo $PATH`

You should see `/usr/local/bin` at the beginning of the output.

STAR is installed! You can type `STAR` from any directory in your terminal to run the program.

### Find data

see `https://www.gencodegenes.org/human/`

Here's the download link for the human genome annotations

```
ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_29/gencode.v29.annotation.gtf.gz
```

use `wget` to get download the data

```
#extract the lines for chr22 sequence with 
tail -4593059 GRCh38.primary_assembly.genome.fa | head -846976 > GRCh38.primary_assembly.chr22.fa
```



### Make a database

Here is an example fasta file. Can you work out how to make a database? You'll need to index the fasta file. There are instructions in the documentation here `https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf`

You'll end up with something like this

```
% mkdir humanHG38chr22
% STAR --runThreadN 4 --runMode genomeGenerate --genomeDir humanHG38chr22/ --genomeFastaFiles GRCh38.primary_assembly.chr22.fa --sjdbGTFfile gencode.v29.annotation.gtf --sjdbOverhang 100 
```



### Align RNAseq reads to a reference sequence

Here's the syntax for running STAR

```
STAR --genomeDir genomes --readFilesIn r1.snip.fq r2.snip.fq

# here's an example command line
% STAR --runThreadN 4 --genomeDir humanHG38chr22/ --readFilesIn ./r1.snip.fq ./r2.snip.fq

```

The alignments are in the .sam file, you can find a summary in the file `Log.final.out `

