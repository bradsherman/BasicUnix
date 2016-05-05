#!/usr/bin/env python2.7

import sys
import sets
import os
import getopt

DELIM = '\t'

# Usage function

def usage(status=0):
	print '''usage: {} [-d DELIM -f FIELDS] files...
	
	-d uses DELIM as a delimiter
	-f only prints the specified FIELDS'''.format(os.path.basename(sys.argv[0]))
	sys.exit(status)

# Parse command line options

try:
	opts, args = getopt.getopt(sys.argv[1:], "d:f:")
except getopt.GetoptError as e:
	print e
	usage(1)

for o, a in opts:
	if o == "-d":
		DELIM = a
	elif o == "-f":
		FIELDS = set(a.split(','))
		fieldflag = True
	else:
		usage(1)

if len(args) == 0:
	args.append('-')

if  not fieldflag:
	usage(1)

# Main 

for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)
	
	for line in stream:
		fields = list()
		line = line.rstrip()
		line = line.split(DELIM)
		for field in FIELDS:
			field = int(field)-1  # zero index
			fields.append(line[field])
		newline = DELIM.join(fields)
		print newline
