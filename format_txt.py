#!/usr/bin/env python
##########################################
#  This script removes the first line of #
#  a TXT file. 				 #
##########################################

import os

dirname = "testdir/"
filename = ""
lines = ""

for thisfile in os.listdir(dirname):
	# If the filename ends with '.txt'
	if thisfile.endswith(".txt"):
		# Create the full relative path (of the form 'testdir/lorem.txt')
		filename = os.path.join(dirname, thisfile)
		# Open each file and read its contents into 'lines', which is a LIST variable
		with open (filename, 'r') as incsvfile:
			lines = incsvfile.read().splitlines()
		# Remove the first item (at index 0) from the LIST called 'lines' - this will be the first line of the file.
		lines.pop(0)
		# Write the lines back to the file.
		with open (filename, 'w') as outcsvfile:
			for line in lines:
				# Note the use of \n, becayse .write() and .read() and .readline() does not consider newline characters
				outcsvfile.write("%s\n" % line)
