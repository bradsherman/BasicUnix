#!/bin/sh

# Command to remove blank lines
rmwhite='sed '/^[[:blank:]]*$/d''
# Default delimiter
delim='#'
# Command to remove trailing whitespace
rmtrailing='sed 's/[[:blank:]]*$//''
# Get options
while getopts ":Wd:" arg
do
	case $arg in
		W)rmwhite='cat'
			;;
		d)delim=$OPTARG
			;;
		*)echo usage: cat InputFile | $0 [ -d Delimiter -W ]
			exit 1
			;;
	esac
done
#remove commented lines, remove comments at end of lines, then white space 
sed 's/^$delim/\n/g' | awk -F"$delim" '{print $1}'| $rmwhite | $rmtrailing
exit 0
