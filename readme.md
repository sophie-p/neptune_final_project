# Neptune Computational Biology - Final Project

## Guidelines - you can delete this section before submission

This repository is a stub for your final project. Fork it, develop your project, and submit it as a pull request. Edit/ delete the text in this readme as needed.

Some guidelines and tips:

- Use the stubs below to write up your final project.

- For information on formatting text files with markdown, see https://guides.github.com/features/mastering-markdown/ . You can use markdown to include images in this document by linking to files in the repository, eg `![Figure 1](./Figure1.png?raw=true)`.

- The project must be entirely reproducible. In addition to the results, the repository must include all the data (or links to data) and code needed to reproduce the results.

- If you are working with unpublished data that you would prefer not to publicly share at this time, please contact me to discuss options. In most cases, the data can be anonymized in a way that putting them in a public repo does not compromise your other goals.

- Paste references (including urls) into the reference section, and cite them with the general format (Smith at al. 2003).

- Commit and push often as you work.

OK, here we go.

# Building a phylogeny of cnidarians tropomyosin

## Introduction and Goals

I would like to build a phylogenetic tree of the cnidarians tropomyosin to identify the tropomyosin (tpm) genes of Nematostella vectensis. 

First I will look on the pubmed database for some well characterised tropomyosins sequences. Those sequences will be used as query for the blast search. Then I will write a program allowing to find tropomyosin genes from the genomes of several cnidarians (Nematostella, Hydra, Acropora..) using a blast search and save the sequences in a fasta file. Finally I will build the phylogenetic tree. 

The data I will use are published genome and transcriptome from cnidarians. 

## Methods

I first copied the mRNA sequences of tpm from Clytia hemisphaerica, Podocoryne carnea and 1 from Nematostella vectensis from the NCBI database and combined them into a fasta file (Tpmqueryblast.fasta).

Then I performed a blastx search against the proteome of Nematostella, using the Tpm sequences from NCBI as query. 
The first step is to create a database from the proteome file with the following cocmmand line: makeblastdb -in Nv.fa -dbtype 'prot'
3 files are created.
The blastsearch is launched using: blastx -db Nv.fa.p* -query Tpmqueryblast.fasta -evalue 0.1 -outfmt 6 -out results.out

To get the query sequence, the matching sequence in Nematostella, and the evalue, I wrote the miniprogram called sseqidevalue.py.
To get only the sequence id of nematostella, I wrote the miniprogram called sseqid.py.
Some sequences id appear several times, the duplicates can be removed using the miniprogram rmdb.py.
Finally to get the sequences corresponding to the id, I wrote the miniprogram called idtoseq.py.

Then I combined all the miniprogram into a bigger program called blastseq.py, permitting to get directly from the blast result a fasta file with the protein sequences.



The tools I used were... See analysis files at (links to analysis files).

## Results

![Figure 1](./Figure1.png?raw=true)

In Figure 1...

## Discussion

These results indicate...

The biggest difficulty in implementing these analyses was...

If I did these analyses again, I would...

## References


