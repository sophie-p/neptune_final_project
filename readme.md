# Neptune Computational Biology - Final Project

# Building a phylogeny of cnidarians tropomyosin

## Introduction and Goals

I would like to build a phylogenetic tree of the cnidarians tropomyosin to identify the tropomyosin (tpm) genes of Nematostella vectensis. 

First I will look on the pubmed database for some well characterised tropomyosins sequences. Those sequences will be used as query for the blast search. Then I will write a program allowing to find tropomyosin genes from the genomes of several cnidarians (Nematostella, Hydra, Acropora..) using a blast search and save the sequences in a fasta file. Finally I will build the phylogenetic tree. 

The data I will use are published genome and transcriptome from cnidarians. 

## Methods

I first copied the mRNA sequences of tpm from Clytia hemisphaerica, Podocoryne carnea and 1 from Nematostella vectensis from the NCBI database and combined them into a fasta file (Tpmqueryblast.fasta).

Then I performed a blastx search against the proteome of Nematostella, using the Tpm sequences from NCBI as query with the Blast Standalone program from NCBI.
The first step is to create a database from the proteome file with the following cocmmand line: makeblastdb -in Nv.fa -dbtype 'prot'
3 files are created.
The blastsearch is launched using: blastx -db Nv.fa -query Tpmqueryblast.fasta -evalue 0.1 -outfmt 6 -out results.out

To get the query sequence, the matching sequence in Nematostella, and the evalue, I wrote the miniprogram with python called sseqidevalue.py.
To get only the sequence id of nematostella, I wrote the miniprogram called sseqid.py.
Some sequences id appear several times, the duplicates can be removed using the miniprogram rmdb.py.
Finally to get the sequences corresponding to the id, I wrote the miniprogram called idtoseq.py.

Then I combined all the miniprogram into a bigger program called blastseq.py, permitting to get directly from the blast result a fasta file with the protein sequences. This program needs 2 files as input: the file with the blast results and the proteome databasese. In the output files are the blast results with evalue, the sequences id, and the protein sequences.

(The command blastdbcmd can also be used to get the sequences from the database file.)

## Results / Discussion

The blast search results are: 
- 5 sequences from Nematostella
- 5 from Hydra
- 6 from Acropora

However, the Evalue used for the search is high (0,1), therefore, I need to check whether the sequences are tropomyosin.
I will keep only sequences having the tropomyosin domain and with tropomyosin sequences as results of a reciprocal blast.

All the sequences match a tropomyosin domain from the pfam database.

To build the phylogenetic tree, I will also need to get sequences from other cnidarian like Aiptasia, Aurelia, Clytia...


## References


