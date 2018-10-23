# STAR RNA-seq aligner



## Tutorial

**While you are working through this workshop, look at the files are in ~spr/starAlignerWorkshop/ and refer to the documentation for STAR `https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf` 

You can skip all the STAR tasks and go straight to writing a python script if you want

### Installation

STAR is available on github at `https://github.com/alexdobin/STAR`

Installation is very easy.

**You will need to log into your mac workstation as the `admin` user. **

You should have a `git` directory in your home directory for all the repos you have cloned. It's a good idea to organize your code like this. Clone the STAR repository into this directory.

```
% mkdir ~/git
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

**Log out as admin and log in with your own user name**

In unix, there is a list of directories that binaries live in called `PATH	`. Add the `/usr/local/bin`  directory to `PATH` if you don't see it in the output if you type this

```
%echo $PATH
/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin
```

In a text editor, add a line to `~/.profile` like this. This is how you add a directory to PATH

```
export PATH="/usr/local/bin:$PATH"
```

now type `source ~/.profile` and then `echo $PATH`

You should see `/usr/local/bin` at the beginning of the output.

STAR is installed! You can type `STAR` from any directory in your terminal to run the program.

### Find data

**Also see files in ~spr/starAlignerWorkshop/ **

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



### Make a database by indexing a fasta file

There is an example fasta file here

`~spr/starAlignerWorkshop/GRCh38.primary_assembly.chr22.fa`

We're going to give you a bit less help on this step. Can you work out how to make a database? You'll need to index the fasta file. There are instructions in the documentation here `https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf`

You'll end up with commands something like this to make the index 

```
% mkdir humanHG38chr22
% STAR --runThreadN 4 --runMode genomeGenerate --genomeDir humanHG38chr22/ --genomeFastaFiles GRCh38.primary_assembly.chr22.fa --sjdbGTFfile gencode.v29.annotation.gtf --sjdbOverhang 100 
```

Ask for help if you need it.

### Align RNAseq reads to a reference sequence

Here's the syntax for running STAR

```
STAR --genomeDir genomes --readFilesIn r1.snip.fq r2.snip.fq

# here's an example command line
% STAR --runThreadN 4 --genomeDir humanHG38chr22/ --readFilesIn ./r1.snip.fq ./r2.snip.fq

```

The alignments are in the .sam file, you can find a summary in the file `Log.final.out `

### Write a python script

Your script should read in the contents of `Log.final.out` and `Log.out ` and print out a single line with the following tab-separated columns of data in this order: 

input filename1
input filename 2 (if there is one)     
reference genome      
% reads uniquely mapped
mismatch rate per base
toal % reads mapped to multiple loci
total % reads unmapped

number of GT/AG splices     

number of GC/AG splices     
number of AT/AC splices     
number of non-canonical splices