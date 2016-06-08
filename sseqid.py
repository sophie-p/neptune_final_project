#! /usr/bin/env python
import re
import sys

arguments = sys.argv
print (arguments)

InFileName = sys.argv [1]
InFile = open ( InFileName, 'r' )

#InFileName = 'resultsblastxNvNvtest.out'
#InFile = open ( InFileName, 'r' )

for Line in InFile:

	ElementList = Line.split( '\t' )
	print('{}'.format (ElementList [1]))

InFile.close()