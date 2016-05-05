#!/usr/bin/env python2.7

import os
import sys
import yaml
import getopt
import re
import fnmatch
import shlex
import time

# Global variables
RULESFILE = '.rorschach.yml'
SECONDS = 2
VERBOSE = 0
DIRECTORIES = '.'
RULES = {}
STARTTIME = time.time()

# Functions
def usage(status=0):
	print '''usage: {} [-r RULES -t SECONDS] DIRECTORIES...
	-r RULES      Path to rules file (default is .rorschach.yml)
	-t SECONDS    Time between scans (default is 2 seconds)
	-v            Display verbose debugging output
	-h            Show this help message'''.format(os.path.basename(sys.argv[0]))
	sys.exit(status)

def debug(message,*args):
	if VERBOSE == 1:
		print message.format(*args)

def check_directory(path):
	for root, dirs, files in sorted(os.walk(path)):
		for name in files:
			fullpath = os.path.join(root,name)
			if os.path.isfile(fullpath):
				check_file(fullpath)

def find_match(name,pattern):
	try:
		if fnmatch.fnmatch(name,pattern) or re.match(pattern,os.path.basename(name)):
			return True
	except re.error as e:
		return False

def check_file(name):
	global STARTTIME
	for rule in range(0,len(RULES)):
		PATTERN = RULES[rule]['pattern']
		ACTION = RULES[rule]['action']
		filetime = os.path.getmtime(name)

		if find_match(name,PATTERN) and filetime > STARTTIME:
			STARTTIME = time.time()
			execute_action(name,ACTION)

def execute_action(name,action):
	newaction = action.format(path=name,name=os.path.basename(name))
	command = shlex.split(newaction)

	try:
		debug("Forking...")
		pid = os.fork()
		if pid == 0:
			try:
				debug("Execing...")
				os.execvp(command[0],command)
			except OSError as e:
				print 'Could not exec: {}'.format(e)
				usage(1)
		else:
			debug("Waiting...")
			pid,status = os.wait()
	except OSError as e:
		print e
		usage(1)

# Parse arguments
try:
	opts, args = getopt.getopt(sys.argv[1:], "r:t:vh")
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
	elif o == "-r":
		RULESFILE = a
	else:
		usage(1)
if len(args) > 0:
	DIRECTORIES = args

# Main execution
with open( RULESFILE,'r' ) as f:
	RULES = yaml.load(f)

while True:
	for directory in DIRECTORIES:
		check_directory(directory)
	try:
		time.sleep(SECONDS)
	except KeyboardInterrupt as e:
		print "\nProgram ended by user."
		sys.exit(0)
