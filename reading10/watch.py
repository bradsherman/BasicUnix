#!/usr/bin/env python2.7

import os
import sys
import time

# Global variables
PROGNAME  = sys.argv[0]
WATCH     = 'watch'
ARGS      = sys.argv[1:]
COMMAND   = WATCH + ' ' + ' '.join(ARGS)
UPDATE    = 2
NEWINT    = 0

def usage(status=0):
		print '''usage: {} [-n INTERVAL] COMMAND
-n Updates the output of COMMAND every INTERVAL seconds
		'''.format(os.path.basename(PROGNAME))
		sys.exit(status)

# Parse Options
for arg in range(0,len(ARGS)):
	if ARGS[arg] == '-n':
		UPDATE = ARGS[arg+1]
		NEWINT = 1

if len(ARGS) == 0 and NEWINT == 0:
	usage(1)
if NEWINT == 1 and len(ARGS) <= 2:
	usage(1)
# Perform watch
while True:
	try:
		os.system('clear')
		os.system(COMMAND)
		time.sleep(int(UPDATE))
	except KeyboardInterrupt as e:
		break
