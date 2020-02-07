
<!----- Conversion time: 0.88 seconds.


Using this Markdown file:

1. Cut and paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β17
* Mon Oct 21 2019 16:23:23 GMT-0700 (PDT)
* Source doc: https://docs.google.com/open?id=1HGxjb10-Kqx-ZaJUHzpuRA41kngeJU1vlzEiOAAX4aA
----->


# Gene Function Annotation and Gene Set Analysis: Workshop

Oct. 25th, 2019

The goal of this exercise is to learn how to use a python script to retrieve PANTHER annotation data or perform a statistical overrepresentation test through an Application Programming Interface (API)


## Download

The script is developed in the GitHub repository in the following location:

[https://github.com/pantherdb/pantherapi-pyclient](https://github.com/pantherdb/pantherapi-pyclient) 

If you have a GitHub account, you can clone the repo to your desktop app. If not, you can simply download the repo to your desktop. 

Sofia Says: __Don't Clone This Into Another Repository__

_<span style="text-decoration:underline;">PANTHER API Service</span>_

PANTHER API is an interface to allow client to access PANTHER data and tools. The users can access directly through command-line command, or embed the commands/codes in various scripts and programs (Perl, Python, R, etc.).

Example client code for calling can be found in the[ Panther API services](http://panthertest3.med.usc.edu:8083/services/tryItOut.jsp?url=%2Fservices%2Fapi%2Fpanther)


## Installation

```
$ git clone https://github.com/pantherdb/pantherapi-pyclient.git

$ cd pantherapi-pyclient

$ python3 -m venv env

$ . env/bin/activate (bash) or source env/bin/activate.csh (C-shell or tcsh)

$ pip install -r requirements.txt
```

## Running

```
$ python3 pthr_go_annots.py --service <service type> --params_file <parameter file> --seq_id_file <gene list file>
```

### Service Types

Currently, there are three options for service types (--service or -s).



*   _enrich_ -- This is the statistical overrepresentation test on a list of genes.
*   _geneinfo_ -- This call provides GO and pathway annnotations to the uploaded genes.
*   _ortholog_ -- This call returns the orthologs of the uploaded list. Maximum of 10 genes can be loaded. The orthologs can be from a specified genome, or from all genomes in the PANTHER database (132 total).


### Parameter File

These files (in JSON format) are in the params/ folder. They should be edited according to the uploaded data and the type of call. 
 
**enrich.json**   
This file should be used when _enrich_ is specified as the service type. There are four items to be specified in this file.
 1. "organism": "**9606**" --specify an organism with a taxon ID. (see Appendix on How to find a taxon ID?)
 2. "annotDataSet": "**GO:0008150**" --specify an annotation data set. (see Appendix on How to find the ID for supported annotation dataset?)  
 3. "enrichmentTestType": "**FISHER**", --enter either FISHER (for Fisher's Exact test) or BINOMIAL (for binomial distribution test)  
 4. "correction": "**FDR**" --specify the multi test correction method (FDR, BONFERRONI, or NONE)
 
**geneinfo.json**   
This file should be used when _geneinfo_ is specified as the service type. The organism taxon ID needs to be specified to match the uploaded data.
 
 **ortholog.json**   
 This file should be used when _ortholog_ is specified as the service type. There are three items to be specified
 1. "organism": "**9606**" -- specify the organism of the uploaded genes
 2. "orthologType": "**LDO**" -- specify the type of ortholog, e.g., LDO (for least divergent ortholog), or all.
 3. "targetOrganism": “10090,7227” -- specifiy the taxon ids for the target organisms, separated by a comma.


### User Gene List

This should be a simple text file (.txt) with one gene identifier per line. Please visit the following page to find out the supported IDs.

[www.pantherdb.org/tips/tips_batchIdSearch_supportedId.jsp](www.pantherdb.org/tips/tips_batchIdSearch_supportedId.jsp)


## Usage


Sofia Says: Check out the nice usage of `argparse`!!!

```
$ python3 pthr_go_annots.py -h

usage: pthr_go_annots.py [-h] [-s SERVICE] [-p PARAMS_FILE] [-f SEQ_ID_FILE]

optional arguments:

  -h, --help            show this help message and exit

  -s SERVICE, --service SERVICE

                        Panther API service to call (e.g. 'enrich', 'geneinfo', 'ortholog')

  -p PARAMS_FILE, --params_file PARAMS_FILE

                        File path to request parameters JSON file

  -f SEQ_ID_FILE, --seq_id_file SEQ_ID_FILE

                        File path to list of sequence identifiers


```

_<span style="text-decoration:underline;">Examples:</span>_


__geneinfo__
```
% python3 pthr_go_annots.py -s geneinfo -p params/geneinfo.json -f resources/test_ids.txt
```

__enrich__
```
% python3 pthr_go_annots.py -s enrich -p params/enrich.json -f resources/test_ids.txt
```

__ortholog__
```
% python3 pthr_go_annots.py -s ortholog -p params/ortholog.json -f resources/test_ids_ortholog.txt
```

## Appendix


### How to find a Taxon ID?

There are three ways to find the exact taxon IDs for genomes supported by PANTHER. 



1. Go to the PANTHER Open API site ([http://panthertest3.med.usc.edu:8083/services/tryItOut.jsp?url=%2Fservices%2Fapi%2Fpanther](http://panthertest3.med.usc.edu:8083/services/tryItOut.jsp?url=%2Fservices%2Fapi%2Fpanther)), and use the /supportedgenomes service.
2. Go directly to the API link page ([http://panthertest3.med.usc.edu:8083/services/oai/pantherdb/supportedgenomes](http://panthertest3.med.usc.edu:8083/services/oai/pantherdb/supportedgenomes)). 
3. Run the following command: 
```
curl -X POST "http://panthertest3.med.usc.edu:8083/services/oai/pantherdb/supportedgenomes" -H  "accept: application/json"
```

Use the taxon ID that corresponds to the genomes in the ‘name’ field.


### How to find the ID for supported annotation dataset?

There are three similar ways to find the IDs or text needed for the supported annotation dataset.



1. Go to the PANTHER Open API site ([http://panthertest3.med.usc.edu:8083/services/tryItOut.jsp?url=%2Fservices%2Fapi%2Fpanther](http://panthertest3.med.usc.edu:8083/services/tryItOut.jsp?url=%2Fservices%2Fapi%2Fpanther)), and use the /supportedannotdatasets service.
2. Go directly to the API link page ([http://panthertest3.med.usc.edu:8083/services/oai/pantherdb/supportedannotdatasets](http://panthertest3.med.usc.edu:8083/services/oai/pantherdb/supportedannotdatasets)). 
3. Run the following command:  
```
curl -X POST "http://panthertest3.med.usc.edu:8083/services/oai/pantherdb/supportedannotdatasets" -H  "accept: application/json"
```

Use the text in the ‘id’ field for the parameter files.


<!-- Docs to Markdown version 1.0β17 -->
