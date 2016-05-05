Homework 04
===========

Activity 01
-----------

1. a) In order to set the default values for variables I used parameter expansion.
   b) To iterate over all the files that contains SUFFIXES, I used a wildcard with
	$SUFFIXES --> *$SUFFIXES to get all files that end in SUFFIXES.
   c) For the VERBOSE variable, I used an if statement to see if it was 1 or not,
	and I have the same block of code in both cases except if it is one I echo
	the command i used to compile.
   d) After I try to compile, I used $? to see the exit status of gcc, if it is not 
	0, meaning there was some type of error, then I display an error message and 
	exit 1 so that the program terminates early.

2. I think the advantages of using make over bake is that it is easier to learn and 
	more structured. The advantages of using bake are that it is much more 
	customizable, and I think depending on how well you know your scripting language
	it could be much more powerful than make. I think for now I will continue 
	using make until I feel that my scripting skills are strong enough to try 
	and make my own bake with customized features.

Activity 02
-----------

1. a) To parse the command line arguments, I used getopts to capture all of the flags
	and their arguments. After I checked to see if there were flags set, I used a
	for loop to go through all of the directories listed.
   b) I used an if statement after using getopts to take care of the case 
	there are no directories listed. It just checks to see if the number of arguments
	is equal to 0 and if so it displays an error and exits 1.
   c) I used a for loop with $@, to process each directory argument. For each directory, 
	it checks to see if $nopt is empty or not. If it is, it prints the defualt 10 
	files. If it's not empty, then it uses $nopt to print the specified number of 
	files. In each branch, it checks to see if $aopt is 1 or not, and adds the 
	-a flag accordingly.
   d) I used multiple if statements to check and see if the command line arguements were
	used or not. Using getopts I set variables to certain values and then tested
	for those values in my if statements. 

2. The part of the program that took the most amount of code was actually using the du
	command. This is partly surprising because I thought it would take a lot of code
	to parse through all the command line arguments, but it also doesn't surprise me
	because since there are different options there are many different variations of 
	du that need to be carried out.

Activity 03
-----------

1. a) I handled different signals using trap. I had three trap commands that all output
	different sayings based on what signal is received.
   b) I didn't have any long messages, but if I did I would have used a here document by
	using 'echo << EOF' and then typing my message and typing EOF to end it.
   c) I handled the timeout by using a while loop with a counter. Once the counter reaches
	10 it leaves the while loop so after the while loop I have a message for the 
	timeout.

2. I think that once I get used to the syntax of shell scripting they will be much easier
	to write than C programs. I like them because I do not need to compile, and they
	can be used to manipulate files very easily whereas in C, file I/O is syntactically
	pretty difficult. Because of this I would use shell scripts for anything having
	to do with my filesystem or just sending commands to my system, and C programs 
	for most other things.
