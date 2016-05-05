#!/usr/bin/env python2.7

import os
import sys
import tempfile

# Global variables
PROGNAME   = sys.argv[0]
FILES      = sys.argv[1:]
# see if user has an editor set already,
# if not use vim
try:
	env = {"EDITOR":os.environ['EDITOR']}
except KeyError as e:
	env = {"EDITOR":'vim'}
EDITOR = env["EDITOR"]
# open tempfile
TEMP = tempfile.NamedTemporaryFile(delete=False)

def usage(status=0):
	print '''usage: {} FILES
	renames FILES using the editor of your choice
	'''.format(os.path.basename(PROGNAME))
	sys.exit(status)

if len(FILES) == 0:
	usage(1)

# Write files to be changed to the tempfile
for FILE in FILES:
	TEMP.write(FILE + "\n")
TEMP.flush()
TEMP.seek(0)

# Open the filenames in the specified editor
NAME = TEMP.name
COMMAND = EDITOR + " " + NAME
exit_status = os.system(COMMAND)

if exit_status == 1:
	usage(1)

# Read in each line of the file, and change
# the files to their new names
filenum=0
while filenum < len(FILES):
	line = TEMP.readline()
	try:
		os.rename(FILES[filenum].rstrip(),line.rstrip())
	except OSError as e:
		print "Error, couldn't rename " + FILES[filenum]
	filenum+=1

# Delete tempfile
TEMP.close()
os.unlink(TEMP.name)
