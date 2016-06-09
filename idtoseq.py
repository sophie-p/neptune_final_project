#! /usr/bin/env python
import sys
import re


#arguments = sys.argv
#print (arguments)

#InFileName = sys.argv [1]
#InFile = open ( InFileName, 'r' )

InFileName = 'Nv.fa'
InFile = open ( InFileName, 'r' )

#print ('database protein sequences: ' + InFileName)

InFileName2 = 'seqidnondb.fasta'
InFile2 = open ( InFileName2, 'r' )

OutFileName2 = 'sseq.fasta'
OutFile2 = open ( OutFileName2, 'w' )


searchset = set()
for line in InFile2:
	if 'Nv' in line:
		print (line)
		searchset.add('>'+ line)

for Line in InFile:
	if Line in searchset:
		Line = Line.strip ()
		print (Line)
		OutFile2.write(Line + '\n' + next (InFile) )

OutFile2.close()

InFile.close()