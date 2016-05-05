#!/bin/sh

while getopts ":an:" arg
do
	case $arg in
		a)aopt=1;;
		n)nopt=$OPTARG;;
		*)echo usage: $0 [ -a -n N ] directory...;;
	esac
done

shift $((OPTIND -1))

if [ $# -eq 0 ]; then
	echo usage: $0 [ -a -n N  ] directory...
	exit 1
fi

for arg in $@; do
	if [ -z $nopt ]; then
		if [ "$aopt" = 1 ]; then
			du -ah $arg 2>/dev/null | sort -rh | head 
			exit 0
		else
			du -h $arg 2>/dev/null | sort -rh | head
			exit 0
		fi
	else
		if [ "$aopt" = 1 ]; then
			du -ah $arg 2>/dev/null | sort -rh | head -$nopt
			exit 0
		else
			du -h $arg 2>/dev/null | sort -rh | head -$nopt
			exit 0
		fi
	fi
done
