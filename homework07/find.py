#!/usr/bin/env python2.7



import sys
import getopt
import os
import stat
import fnmatch
import re

# Global Variables

PROGNAME       = os.path.basename(sys.argv[0])
FILES          = 0
DIRECTORY      = 0
EXE            = 0
READ           = 0
WRIT           = 0
EMPTY          = 0
FILENAMEFLAG   = 0
PATHFLAG       = 0
REGEXFLAG      = 0
PERMFLAG       = 0
FILENEWERFLAG  = 0
UIDFLAG        = 0
GIDFLAG        = 0

# Functions

def error(message,status=1):
	print  >>sys.stderr, message
	sys.exit(status)

def usage(status=0):
	error('''usage: {} directory [-type [f|d] -executable -readable -writable -empty -name pattern -path pattern -regex pattern -perm mode -newer file -uid n -gid n] 
		    -type [f|d]     File is of type f for regular file or d for directory

		    -executable     File is executable and directories are searchable to user
		    -readable       File readable to user
		    -writable       File is writable to user
		    
		    -empty          File or directory is empty
		    
		    -name  pattern  Base of file name matches shell pattern
		    -path  pattern  Path of file matches shell pattern
		    -regex pattern  Path of file matches regular expression
		    
		    -perm  mode     File's permission bits are exactly mode (octal)
		    -newer file     File was modified more recently than file
		    
		    -uid   n        File's numeric user ID is n
		    -gid   n        File's numeric group ID is n'''
			.format(PROGNAME), status)

def include(path):
	# Tells whether an item should be included in output or not
	try:
		stats = os.stat(path)
	except OSError as e:
		stats = os.lstat(path)
	if FILES == 1 and not os.path.isfile(path):
		return False
	if DIRECTORY == 1 and not os.path.isdir(path):
		return False
	if EXE == 1 and not os.access(path,os.X_OK):
		return False
	if READ == 1 and not os.access(path,os.R_OK):
		return False
	if WRIT == 1 and not os.access(path,os.W_OK):
		return False
	if EMPTY == 1:
		if os.path.islink(path):
			try:
				if os.stat(path):
					return False
			except OSError as e:
				return False
		elif os.path.isfile(path):
			if not os.path.getsize(path) == 0:
				return False
		elif os.path.isdir(path):
			try:
				if not os.listdir(path) == []:
					return False
			except OSError as e:
				return False
		else: 
			return False
	if FILENAMEFLAG == 1 and not fnmatch.fnmatch(os.path.basename(path),os.path.basename(FILENAME)):
		return False
	if PATHFLAG == 1 and not fnmatch.fnmatch(path,PATHNAME):
		return False
	if REGEXFLAG == 1: 
		reg = re.compile(REGEX)
		if not reg.match(path):
			return False
	if PERMFLAG == 1:
		permissions = oct(stat.S_IMODE(stats.st_mode))
		permissions = str(permissions)
		permissions = permissions[1:]
		if MODE != permissions:
			return False
	if FILENEWERFLAG == 1:
		timenewer = os.path.getmtime(FILENEWER)
		if os.path.isfile(path) or os.path.isdir(path):
			filetime = os.path.getmtime(path)
			if filetime <= timenewer:
				return False
		else:
			return False
	if UIDFLAG == 1:
		uid = stats.st_uid
		if uid != int(UID):
			return False
	if GIDFLAG == 1:
		gid = stats.st_gid 
		if gid != int(GID):
			return False
	return True
		

# Parse command line options

args = sys.argv[2:]
dname = sys.argv[1]
for arg in range(0,len(args)):
	o = args[arg]
	if o[0] != '-':
		continue
	if o == '-type':
		if args[arg+1] == 'f':
			FILES = 1
		elif args[arg+1] == 'd':
			DIRECTORY = 1
	elif o == '-executable':
		EXE = 1
	elif o == '-readable':
		READ = 1
	elif o == '-writable':
		WRIT = 1
	elif o == '-empty':
		EMPTY = 1
	elif o == '-name':
		FILENAME = args[arg+1]
		FILENAMEFLAG = 1
	elif o == '-path':
		PATHNAME = args[arg+1]
		PATHFLAG = 1
	elif o == '-regex':
		REGEX = args[arg+1]
		REGEXFLAG = 1
	elif o == '-perm':
		MODE = args[arg+1]
		PERMFLAG = 1
	elif o == '-newer':
		FILENEWER = args[arg+1]
		FILENEWERFLAG = 1
	elif o == '-uid':
		UID = args[arg+1]
		UIDFLAG = 1
	elif o == '-gid':
		GID = args[arg+1]
		GIDFLAG = 1
	else:
		error('Not a valid argument')

# Main execution
if include(dname):
	print dname
for root, dirs, files in sorted(os.walk(dname,topdown=True,onerror=None,followlinks=True)):
	for name in dirs + files:
		fullpath = os.path.join(root,name)
		if include(fullpath):
			print fullpath
