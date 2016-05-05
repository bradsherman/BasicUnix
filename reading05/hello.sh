#!/bin/sh

#print hello, {command} for each command line argument

while [ "$1" != "" ]; do
	echo "Hello, $1"
	# Shift parameters
	shift
done

exit 0
