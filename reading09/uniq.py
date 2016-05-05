#!/usr/bin/env python2.7

import sys
import getopt
import os

appearances = False
entries = {}

# Usage function

def usage(status=0):
	print '''usage: {} [-c] files...
	
	-c print number of occurences in front of each line'''.format(os.path.basename(sys.argv[0]))
	sys.exit(status)

# Parse command line options

try:
	opts, args = getopt.getopt(sys.argv[1:], "c")
except getopt.GetoptError as e:
	print e
	usage(1)

for o, a in opts:
	if o == "-c":
		appearances = True
	else:
		usage(1)

if len(args) == 0:
	args.append('-')


# Main 

for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)
	
	for line in stream:
		line = line.rstrip()
		if line in entries:
			entries[line]+=1	
		else:
			entries[line]=1

for k,v in sorted(entries.items()):
	if(appearances):
		print '{:>7} {}'.format(v, k)
	else:
		print k


