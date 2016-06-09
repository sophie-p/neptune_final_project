#! /usr/bin/env python
import sys
import re

arguments = sys.argv
#print (arguments)

InFileName = sys.argv [1]
InFile = open ( InFileName, 'r' )

#InFileName = 'resultstest.fa'
#InFile = open ( InFileName, 'r' )

OutFileName = 'resultsblast.fa'
OutFile = open(OutFileName, 'w')

OutFileName2 = 'seqid.fa'
OutFile2 = open(OutFileName2, 'w')

OutFileName3 = 'seqidnodb.fa'
OutFile3 = open(OutFileName3, 'w')

OutFileName4 = 'seqprotein.fa'
OutFile4 = open(OutFileName4, 'w')


for Line in InFile:
	ElementList = Line.split( '\t' )
	SeqInfo =  ('Query seq.: {} Subj. seq.: {} Evalue : {}'.format (ElementList [0], ElementList [1], ElementList [10
		]))
	OutFile.write (SeqInfo +'\n')
	SeqId = ('{}'.format (ElementList [1]))
	OutFile2.write (SeqId + '\n')
	
OutFile2.close()
#remove double sequences	

InFileName2 = 'seqid.fa'
InFile2 = open ( InFileName2, 'r' )

LineNumbre = 0
lines_seen = set() 
for line in InFile2:
	LineNumbre = LineNumbre + 1
	if LineNumbre > 1:
		if line not in lines_seen: 
			OutFile3.write (line + '\n')
			lines_seen.add(line)

OutFile3.close()

InFileName3 = 'Nv.fa'
InFile3 = open ( InFileName3, 'r' )

InFileName4 = 'seqidnodb.fa'
InFile4 = open ( InFileName4, 'r' )

searchset = set()
for line in InFile4:
	if '00' in line:
		searchset.add('>'+ line)

for Line in InFile3:
	if Line in searchset:
		Line = Line.strip ()
		print (Line)
		OutFile4.write(Line + '\n' + next (InFile3) )

OutFile4.close()

OutFile.close()
InFile.close()
InFile2.close()
InFile3.close()
InFile4.close()