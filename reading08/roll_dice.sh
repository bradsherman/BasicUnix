#!/bin/sh

numrolls=10
numsides=6

while getopts ":r:s:" arg
do
		case $arg in
				r)numrolls=$OPTARG;;
				s)numsides=$OPTARG;;
				*)echo usage: $0 [-r ROLLS -s sides ]
					exit 1;;
		esac
done

shift $((OPTIND-1))

for roll in $(seq $numrolls); do
	shuf -e $(seq $numsides) -n 1
done

