#!/bin/sh

#experiment.sh

./roll_dice.sh -r 1000 | awk '
// {rolls[$1]=rolls[$1]+1;}
END {
for( num in rolls ){
		print num" " rolls[num];
}
}
' | sort  > results.dat
