#! /usr/bin/env python
import sys
import re


#arguments = sys.argv
#print (arguments)

#InFileName = sys.argv [1]
#InFile = open ( InFileName, 'r' )

#get sequences id

InFileName = 'resultstest.fa'
InFile = open ( InFileName, 'r' )

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
lines_seen = set() # holds lines already seen
for line in InFile2:
	LineNumbre = LineNumbre + 1
	if LineNumbre > 1:
		if line not in lines_seen: # not a duplicate
			print(line)
			OutFile3.write (line + '\n')
			lines_seen.add(line)

InFileName3 = 'Nv.fa'
InFile3 = open ( InFileName3, 'r' )


Id = 'Nv|XP_001631731.1'

for Line in InFile3:
	if Id in Line:
		Line = Line.strip ()
		print (Line)
		print next (InFile3)



OutFile.close()




