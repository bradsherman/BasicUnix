#!/usr/bin/env python2.7

import sys
import getopt
import os

# Global Variables

PROGNAME  = os.path.basename(sys.argv[0])
infile    = 0
outfile   = 1
count     = sys.maxint
bs        = 512
seeknum   = 0
skipnum   = 0

# Functions

def error(message,status=1):
	print  >>sys.stderr, message
	sys.exit(status)

def usage(status=0):
	error('''usage: {} [-if=FILE -of=FILE -count=N -bs=BYTES -seek=N -skip=N] files...
	      if=FILE     Read from FILE instead of stdin
	      of=FILE     Write to FILE instead of stdout

	      count=N     Copy only N input blocks
	      bs=BYTES    Read and write up to BYTES bytes at a time

	      seek=N      Skip N obs-sized blocks at start of output
	      skip=N      Skip N ibs-sized blocks at start of input'''
	      .format(PROGNAME), status)

def open_fd(path,mode):
	try:
		return os.open(path,mode)
	except OSError as e:
		error('Could not open {}: {}'.format(str(path),e))

def read_fd(fd,n):
	try:
		return os.read(fd,n)
	except OSError as e:
		error('Could not read {} bytes from FD {}: {}'.format(n,fd,e))

def write_fd(fd,data):
	try:
		return os.write(fd,data)
	except OSError as e:
		error('Could not write {} bytes to FD {}: {}'.format(len(data),fd,e))

# Parse command line options

args = sys.argv

for path in args[1:]:
	newarg = path.split('=')
	if newarg[0] == 'if':
		infile = newarg[1]
	elif newarg[0] == 'of':
		outfile = newarg[1]
	elif newarg[0] == 'count':
		count = newarg[1]
	elif newarg[0] == 'bs':
		bs = newarg[1]
	elif newarg[0] == 'seek':
		seeknum = newarg[1]
	elif newarg[0] == 'skip':
		skipnum = newarg[1]
	else:
		error('Not a valid argument')

count = int(count)
bs = int(bs)
seeknum = int(seeknum)
skipnum = int(skipnum)

# Main execution
if infile != 0:
	source = open_fd(infile,os.O_RDONLY)
	os.lseek(source,skipnum*bs,os.SEEK_SET)
else:
	source = infile 
if outfile != 1:
	target = open_fd(outfile,os.O_WRONLY|os.O_CREAT)
	os.lseek(target,seeknum*bs,os.SEEK_SET)
else:
	target = outfile

data = read_fd(source,bs)

datablocks_written = 0
while data and datablocks_written < count:
	write_fd(target,data)
	data = read_fd(source,bs)
	datablocks_written+=1

os.close(source)
os.close(target)
