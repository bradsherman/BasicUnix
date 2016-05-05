Brad Sherman - Reading 05
=========================

1. An example of a variable var that contains the output of ls is:
	var=$(ls)
2. An example of capturing STDOUT to find the operating system of the machine is:
	$(uname -o)
3. An example of an if statement used to see if a file is present is:
	if [ -f myFile ]; then
		echo "You have myFile"
	else 
		echo "You don't have myFile"
	fi
4. An example of a case statemnt is:
	echo -n "enter a letter"
	read letter
	case $letter in
		a ) echo "You chose a";;
		b ) echo "You chose b";;
		....
		z ) echo "You chose z";;
		* ) echo "You didn't enter a letter";;
	esac
5. An example of a for loop is: 
	echo -n "enter a path to a directory"
	read DIR
	for i in DIR/*; do
		echo $i
	done
6. An example of a while loop is:
	num=0
	while [ "$num" != 5 ]; do
		echo -n "enter 5 to quiit"
		read num
	done
7. An example of a function is: 
	#print current working directory and list contents
	pwdLs(){
		echo "Current Working Directory"
		pwd
		echo "Contents"
		ls
	} 
8. An example of a trap is: 
	STARTUP_FILES=/home/config/start.txt
	trap "rm STARTUP_FILES" SIGHUP SIGINT SIGTERM  
  This will remove the startup files if any of those three signals are received

Source: http://linuxcommand.org/lc3_writing_shell_scripts.php#contents
