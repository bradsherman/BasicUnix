#!/bin/sh

# Get -h flag for help or an invalid flag
while getopts ":h" arg
do
	case $arg in
		h)echo usage: $0 keyValue
			exit 0;;
		*)echo usage: $0 keyValue
			exit 1;;
	esac
done

# shift to other options
shift $((OPTIND-1))

# Grab key paramter and set the key variable
if [ ! -z $1 ]; then
	num=$(echo $1 | grep -P "^[0-9]+$")
	if [ ! -z $num ]; then
		key=$(($num%26))
	else
		echo Please enter a number as a parameter
		exit 1
	fi
else
	key=13
fi

# Set the source sets
IFS=''
ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet='abcdefghijklmnopqrstuvwxyz' 

# if key = 0 there is not shift, so output the same string
if [ $key -eq 0 ]; then
	new=$(tr 'A-Za-z' 'A-Za-z')
# Use the key to cut our source sets and change them into our 
# destination sets, then use the tr command to translate our string
else
	RANGE=$(echo $ALPHABET | cut -b 1-$key)
	RANGE2=$(echo $ALPHABET | cut -b $(($key+1))-${#ALPHABET})
	range=$(echo $alphabet | cut -b 1-$key)
	range2=$(echo $alphabet | cut -b $(($key+1))-${#alphabet})
	tr 'A-Za-z' $RANGE2$RANGE$range2$range
fi
exit 0
