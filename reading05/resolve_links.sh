#!/bin/sh

#print where all symbolic links resolve to in a directory

DIR=$1

for i in $DIR/*; do
	if [ -L $i ]; then
		echo $i resolves to $(readlink $i)
	fi
done

