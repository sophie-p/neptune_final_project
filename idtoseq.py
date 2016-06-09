#! /usr/bin/env python
#import sys
import re


#arguments = sys.argv
#print (arguments)

#InFileName = sys.argv [1]
#InFile = open ( InFileName, 'r' )

InFileName = 'miniprotNv.fa'
InFile = open ( InFileName, 'r' )

print ('Mini database Nematostella: ' + InFileName)

for Line in InFile:
	searchObj = re.search( r'(001623)(\d+)' , Line)
	if searchObj:
		print (searchObj.group(0))


>Nv|XP_001621560.1

#for Line in InFile:
#	searchObj = re.search( r'(001623)(\d+)' , Line)
#	if searchObj:
#		print (searchObj.group(0))








#	SearchString = '(XP_0016357)(\d+)'
#	Result = re.search( SearchString, InFile )
#	print (Result.group(0))
	


#InFile.close()