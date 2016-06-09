#! /usr/bin/env python
import sys

arguments = sys.argv
#print (arguments)

InFileName = sys.argv [1]
InFile = open ( InFileName, 'r' )

#InFileName = 'seqidtest.fa'
#InFile = open ( InFileName, 'r' )

LineNumbre = 0

lines_seen = set() # holds lines already seen
for line in InFile:
	LineNumbre = LineNumbre + 1
	if LineNumbre > 1:
		if line not in lines_seen: # not a duplicate
			print(line)
   			lines_seen.add(line)

   			
InFile.close()