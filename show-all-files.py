#!/usr/bin/python
"""
import glob

for strFile in glob.iglob('/*'):
	print strFile
"""

import os
import sys
from os.path import join, getsize

listUnwanted = ['/proc', '/sys', '/dev', '/media' ,'/mnt' , '/cdrom' , '/boot' , '/var/www']

if len(sys.argv) == 1:
	print "Error: Which directory do you wish to compare?"
	sys.exit(1)

for root, dirs, files in os.walk(sys.argv[1]):
	bExit = False
	for x in listUnwanted:
		if root.startswith(x):
			bExit = True
			break
	if bExit:
		continue
	#print root
	for name in files:
		#print join(root, name)
		os.system("md5sum %s" % (join(root, name)) )
		
		

