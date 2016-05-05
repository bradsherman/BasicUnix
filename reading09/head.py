#!/usr/bin/env python2.7

import sys
import getopt
import os

numlines = 10

# Usage function

def usage(status=0):
	print '''usage: {} [-n NUM] files...
	
	-n NUM prints the first NUM lines of a file'''.format(os.path.basename(sys.argv[0]))
	sys.exit(status)

# Parse command line options

try:
	opts, args = getopt.getopt(sys.argv[1:], "n:")
except getopt.GetoptError as e:
	print e
	usage(1)

for o, a in opts:
	if o == "-n":
		numlines = int(a)
	else:
		usage(1)

if len(args) == 0:
	args.append('-')


# Main 

for path in args:
	count = 0
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)
	
	for line in stream:
		print line,
		count+=1
		if count == numlines:
			break
