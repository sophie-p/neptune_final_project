#! /usr/bin/env python
import re
import sys

arguments = sys.argv
#print (arguments)

InFileName = sys.argv [1]
InFile = open ( InFileName, 'r' )

#InFileName = 'resultsblastxNvNvtest.out'
#InFile = open ( InFileName, 'r' )

#LineNumbre = 0

for Line in InFile:

	ElementList = Line.split( '\t' )
	print('Query seq.: {} Subj. seq.: {} Evalue : {}'.format (ElementList [0], ElementList [1], ElementList [10
		]))

InFile.close()