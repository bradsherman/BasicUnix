#!/usr/bin/env python2.7

import os
import string
import sys
import random
import hashlib
import itertools
import getopt

# Constants
PROGNAME = sys.argv[0]
ALPHABET = string.ascii_lowercase + string.digits
LENGTH   = 8
HASHES   = 'hashes.txt'
PREFIX   = ''

# Utility Functions

def usage(status=0):
	print >>sys.stderr, '''Usage: {program} [-a ALPHABET -l LENGTH -s HASHES -p PREFIX]
	Options:
		-h				Show this help message
		-a ALPHABET		Alphabet used for passwords
		-l LENGTH		Length for passwords
		-s HASHES		Path to file containing hashes
		-p PREFIX		Prefix to use for each candidate password'''.format(program=PROGNAME)
	sys.exit(status)

def md5sum(s):
	return hashlib.md5(s).hexdigest()

# Main

if __name__ == '__main__':

	try:
		options,arguments = getopt.getopt(sys.argv[1:],"ha:l:s:p:")
	except getopt.GetoptError as e:
		usage(1)
	
	for opt, arg in options:
		if opt == '-h':
			usage(0)
		elif opt == '-a':
			ALPHABET = arg
		elif opt == '-l':
			LENGTH = int(arg)
		elif opt == '-s':
			HASHES = arg
		elif opt == '-p':
			PREFIX = arg
		else:
			usage(1)

	hashes = set([l.strip() for l in open(HASHES)])
	for i in range(1,LENGTH + 1):
		for candidate in itertools.product(ALPHABET, repeat=i):
			candidate = list(candidate)
			candidate = ''.join(candidate)
			candidate = PREFIX + candidate
			checksum  = md5sum(candidate)
			if checksum in hashes:
				sys.stdout.write(candidate+"\n")

