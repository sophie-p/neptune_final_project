#! /usr/bin/env python
import sys
import re

arguments = sys.argv
#print (arguments)

InFileName = sys.argv [1]
InFile = open ( InFileName, 'r' )
print 'Results of blast search: ' + InFileName
#InFileName = 'resultstest.fa'
#InFile = open ( InFileName, 'r' )

InFileName3 = sys.argv [2]
InFile3 = open ( InFileName3, 'r' )
print 'Proteome database: ' + InFileName3

#InFileName3 = 'Nv.fa'
#InFile3 = open ( InFileName3, 'r' )

OutFileName = 'resultsblast' + InFileName3
OutFile = open(OutFileName, 'w')

OutFileName2 = 'seqiddb' + InFileName3
OutFile2 = open(OutFileName2, 'w')

OutFileName3 = 'seqid'+ InFileName3
OutFile3 = open(OutFileName3, 'w')

OutFileName4 = 'seqprotein'+ InFileName3
OutFile4 = open(OutFileName4, 'w')


for Line in InFile:
	ElementList = Line.split( '\t' )
	SeqInfo =  ('Query seq.: {} Subj. seq.: {} Evalue : {}'.format (ElementList [0], ElementList [1], ElementList [10
		]))
	OutFile.write (SeqInfo +'\n')
	SeqId = ('{}'.format (ElementList [1]))
	OutFile2.write (SeqId + '\n')
	
OutFile2.close()

InFileName2 = OutFileName2
InFile2 = open ( InFileName2, 'r' )

LineNumbre = 0
lines_seen = set() 
for line in InFile2:
	LineNumbre = LineNumbre + 1
	if LineNumbre > 1:
		if line not in lines_seen: 
			OutFile3.write ('>' + line + '\n')
			lines_seen.add(line)

OutFile3.close()


InFileName4 = OutFileName3
InFile4 = open ( InFileName4, 'r' )

searchset = set()
for line in InFile4:
	if '>' in line:
		searchset.add(line)

for Line in InFile3:
	if Line in searchset:
		Line = Line.strip ()
		print (Line)
		OutFile4.write(Line + '\n' + next (InFile3) )

print 'Protein sequences in file: '+ OutFileName4
print 'Sequences Id in file: '+ OutFileName3
print 'Blast results with Evalue in file: '+ OutFileName

OutFile4.close()

OutFile.close()
InFile.close()
InFile2.close()
InFile3.close()
InFile4.close()