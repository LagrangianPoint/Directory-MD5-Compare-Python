#!/usr/bin/python
import os
import sys
import re
import  cPickle 
from pprint import pprint


if len(sys.argv) < 3:
	print "ERROR: You need to send two files as parameters"
	sys.exit(1)

strFileA = sys.argv[1]
strFileB = sys.argv[2]

dictData = {}
strRegex = '([a-z0-9]{32})\s+(.*)'

### Analyzing file A 
fh = open(strFileA, 'r')
strRaw = fh.read()
fh.close()
for strRow in strRaw.split("\n"):
	if strRow.strip() != '':
		listResults = re.findall(strRegex, strRow)
		if listResults != []:
			strHash, strPath =  listResults[0]
			if not dictData.has_key(strPath):
				dictData[strPath] = {'a': strHash, 'b': None}
			else:
				dictData[strPath]['a'] = strHash

#print "BEFORE: "
#pprint(dictData)

### Analyzing file B
fh = open(strFileB, 'r')
strRaw = fh.read()
fh.close()
for strRow in strRaw.split("\n"):
	if strRow.strip() != '':
		listResults = re.findall(strRegex, strRow)
		if listResults != []:
			strHash, strPath =  listResults[0]
			if not dictData.has_key(strPath):
				dictData[strPath] = {'a': None, 'b': strHash}
			else:
				dictData[strPath]['b'] = strHash

#print "AFTER: "
#pprint(dictData)


fh = open('all-data.pkl', 'wb')
cPickle.dump(dictData, fh)
fh.close()

dictDifferent = {}
for strPath,  dictDiff in dictData.items():
	if dictDiff['a'] != dictDiff['b']:
		#print "DIFFERENT: "
		#print strPath
		#print dictDiff
		dictDifferent[strPath] = dictDiff


fh = open('different.pkl', 'wb')
cPickle.dump(dictDifferent, fh)
fh.close()



