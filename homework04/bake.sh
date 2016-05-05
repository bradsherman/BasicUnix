#!/bin/sh

CC=${CC:="gcc"}
SUFFIXES=${SUFFIXES:=".c"}
CFLAGS=${CFLAGS:="-std=gnu99 -Wall"}
VERBOSE=${VERBOSE:="0"}

for file in *$SUFFIXES; do
	new=$(basename $file $SUFFIXES)
	if [ $VERBOSE -eq 1 ]; then
		$CC $file -o $new $CFLAGS
		if [ $? -ne 0 ]; then
			echo Error compiling $file.
			exit 1;
		fi
		echo $CC $file -o $new $CFLAGS
	else
		$CC $file -o $new $CFLAGS
		if [ $? -ne 0 ]; then
			echo Error compiling $file.
			exit 1;
		fi
	fi
done
exit 0;
