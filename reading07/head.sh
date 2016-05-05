#!/bin/sh

lines=10

while getopts ":n:" arg
do
	case $arg in
			n)lines=$OPTARG;;
	esac
done

awk -v lines=$lines -v a=0 'BEGIN{} {a++; if (a > lines) exit;} {print $0;}'
