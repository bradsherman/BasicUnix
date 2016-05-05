#!/bin/sh

file='timeout.py'

# Check if executable
if [ ! -x $file ]
then 
	echo $file not executable! test_timeout.sh failed!
	exit 1
fi

# Check if she-bang is correct
if !(cat $file | head -1 | grep  -q python2.7); then
	echo $file does not contain correct she-bang! test_timeout failed!
	exit 1
fi

# Check for a reasonable help message
if !(./$file -h 2>&1 | grep -q usage); then
	echo $file does not display a help message. test_timeout failed!
	exit 1
elif !(./$file -h 2>&1 | grep -q verbose); then
	echo $file does not display a help message. test_timeout failed!
	exit 1
fi

# Check for a reasonable -v output
if !(./$file -v -t 3 sleep 1 2>&1 | grep -q Enabling); then
	echo $file does not contain enough verbose output. test_timeout failed!
	exit 1
elif !(./$file -v -t 3 sleep 1 2>&1 | grep -q Process); then
	echo $file does not contain enough verbose output. test_timeout failed!
	exit 1
elif !(./$file -v -t 3 sleep 1 2>&1 | grep -q Alarm); then
	echo $file does not contain enough verbose output. test_timeout failed!
	exit 1
fi

# Check for successful exit
for i in $(seq 4); do
	if !(./$file -t 5 sleep $i 2>&1 > /dev/null); then
		echo test_timeout failed on command "./$file -t 5 sleep $i"
		exit 1
	fi
done

# Check for unsuccessful exit
for i in $(seq 2 5); do
	./$file -t 1 sleep $i > /dev/null 2>&1
	if [[ $? == 0 ]]
	then 
		echo test_timeout failed on command "./$file -t 1 sleep $i"
		exit 1
	fi
done


echo test_timeout.sh successful!
exit 0
