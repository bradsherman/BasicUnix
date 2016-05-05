#!/bin/sh

#print different output for different OSs

os=$(uname -o)

if [ "$os" = "GNU/Linux" ]; then
	echo "Tux"
elif [ "$os" = "Darwin" ]; then
	echo "Hexley"
elif [ "$os" = "FreeBSD" ]; then
	echo "Beastie"
elif [ "$os" = "NetBSD" ]; then
	echo "Beastie"
elif [ "$os" = "OpenBSD" ]; then
	echo "Beastie"
else 
	echo "No matching OS found."
fi

exit 0
