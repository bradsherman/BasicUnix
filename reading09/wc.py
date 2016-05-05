#!/usr/bin/env python2.7

import sys
import getopt
import os

total = 0
lastflag = 'none'

# Usage function

def usage(status=0):
	print '''usage: {} [-c -l -w] files...
	
	-c print byte/character counts
	-l print newline counts
	-w print word counts'''.format(os.path.basename(sys.argv[0]))
	sys.exit(status)

# Parse command line options

try:
	opts, args = getopt.getopt(sys.argv[1:], "clw")
except getopt.GetoptError as e:
	print e
	usage(1)

for o, a in opts:
	if o == "-c":
		lastflag = 'c'
	elif o == "-l":
		lastflag = 'l'
	elif o == "-w":
		lastflag = 'w'
	else:
		usage(1)

IMPLICIT = False

if len(args) == 0:
	args.append('-')
	IMPLICIT = True


# Main 


for path in args:
	count = 0
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)
	
	for line in stream:
		if lastflag == "c":
			for char in line:
				count +=1
		elif lastflag == "l":
			count+=1
		elif lastflag == "w":
			count = count + len(line.split())
		else:
			usage(1)
	if path == '-' and IMPLICIT:
		print count
	else: 
		print count, path
	total = total + count

# This line makes the script fail but the real wc keeps a total count of all the files
#print total, " Total"
