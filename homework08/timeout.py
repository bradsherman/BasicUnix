#!/usr/bin/env python2.7

import os
import sys
import getopt
import signal
import errno
import time

# Global Variables
SECONDS = 10
VERBOSE = 0

# Functions
def usage(status=0):
	print >>sys.stderr, '''usage: {} [-t SECONDS -v -h] command...
	-t SECONDS Timeout duration before killing command (default is 10)
	-v         Display verbose debugging output'''.format(os.path.basename(sys.argv[0]))
	sys.exit(status)

def debug(message,*args):
	if VERBOSE == 1:
		print >>sys.stderr, message.format(*args)

def sigalrm_handler(signum,frame):
	debug("Alarm triggered after {} seconds!",SECONDS)
	debug("Killing PID {}",pid)
	os.kill(pid,signal.SIGTERM)


# Parse arguments
try: 
	opts, args = getopt.getopt(sys.argv[1:], "hvt:")
except getopt.GetoptError as e:
	print e
	usage(1)

for o, a in opts:
	if o == "-h":
		usage()
	elif o == "-v":
		VERBOSE = 1
	elif o == "-t":
		SECONDS = a
	else:
		usage(1)

# Main execution
COMMAND = " ".join(args)
debug("Executing \"{}\" for at most {} seconds...", COMMAND, SECONDS)
try:
	debug("Forking...")
	pid = os.fork()
	if pid == 0:
		try:
			debug("Execing...")
			os.execvp(args[0],args)

		except OSError as e:
			print 'Could not exec: {}'.format(e)
			usage(1)
	else:
		debug("Enabling alarm...")
		signal.signal(signal.SIGALRM,sigalrm_handler)
		signal.alarm(int(SECONDS))
		debug("Waiting...")
		try:
			pid,status = os.wait()
		except OSError as e:
			if e.errno == errno.EINTR:
				pid,status = os.wait()
			else:
				print e
				usage(1)
		debug("Disabling alarm...")
		signal.alarm(0)
		debug("Process {} terminated with exit status {}",pid,status)
		sys.exit(status)
except OSError as e:
	print e
	usage(1)
