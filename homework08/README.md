Homework 08
===========

Activity 01
-----------
1. The role of the child process was to become another process, a.k.a. the process
	that the user wants to be completed before a timeout. The role of the parent process
	is to set the alarm so that we know if the timeout has occurred, and to wait on the
	child process until the alarm is done or the child process is done. Then, no matter
	what, the parent process cleans up the child process and exits.

2. The timeout mechanism worked by using signal.alarm. The flow was that before the parent
	waits on the child, it sets the alarm for the specified number of seconds. Then, if 
	the alarm goes off before the child process is complete, The alarm handler function
	is called, which kills the child process using os.kill. Other system calls include
	os.wait, and the use of the signal module to start and keep track of the alarm.

3. The test script verifies the correctness of my program by first checking if timeout.py
	is executable by doing "if [ ! -x $file ]" where file is timeout.py. If not it exits.
	Then it checks if the she-bang is correct with "cat $file | head -1 | grep -q python2.7".
	Next, it checks for a reasonable help message and reasonable verbose messages by 
	grepping their output for keywords like "usage" and "process" and "enabling". Lastly,
	I check to make sure the program exits with a successful exit status when I give 
	arguments in a way that allows the child process to complete before the alarm goes off,
	and I check to make sure I get a non-successful exit status code when I give arguments 
	that cause the alarm to go off and kill the child process before it is finished. If 
	the script makes it all the way to the end, the program was successful.

4. I created a script that looked like this.
	#!/bin/sh
	count=0
	for i in $(seq 300); do
		./timeout.py -t 2 sleep 2 && count=$((count+1))
	done
	echo $count
	When it finally finished executing, it output 0, meaning the program never succeeded 
	and the alarm always went off before the sleep finished. I was very surprised that it
	happened this way because I thought that it would switch a lot. I do not think it is 
	reasonable to assume we will get the same output every time even though I did, because
	I think it is a matter of milliseconds. I think that on different computers these 
	results could easily be much different.

Activity 02
-----------
1. To ensure I checked every directory, after I parse the command line options I set the 
	DIRECTORIES variable to the rest of the args. Then in my main while loop I pass each
	directory in DIRECTORIES to the check_directory function. In that function I use 
	os.walk to get every file in the directory. Then just to double check I check if each
	file is a file using os.path.isfile and if it is I pass it to check_file.

2. To load the rules, I use open to open the RULESFILE as f, and then I set the RULES 
	variable equal to the result of yaml.load(f). This is then a list of dictionaries
	where each dictionary is a separate pattern and action rule. To check each file against
	the rules in the check_file function, I go through every entry in RULES, and set the
	PATTERN equal to the value of the 'pattern' key for the current dictionary, and I set
	the ACTION equal to the value of the 'action' key for the current dictionary. Then I
	get the last modification time of the current file using os.path.getmtime. I have a 
	helper function called find_match that tries to fnmatch the full path or find a match
	on the regular expression using re.match. If it does, it returns true, otherwise it
	returns false. Back in check_file, if find_match returns True and if the last 
	modification time of the current file is greater than STARTTIME (which is set when 
	the program starts), then I call execute action, and set STARTTIME to the current time
	so that we only see files that have been modified once. 

3. I did not use a data structure to keep track of modification times, I just used the 
	STARTTIME variable mentioned above. Every time the program starts, STARTTIME is set 
	to the result of the time.time(). Then instead of keeping track of each file time I
	just use getmtime on each file and compare that to STARTTIME. If a file's last 
	modification time is greater than STARTTIME, that means it has been modified since
	the start of the program. If so, I pass that file to execute action and I update 
	STARTTIME to the current time. That way, any file modified since the start of the 
	program is only printed once when it is updated, and not every while loop. This 
	works because STARTTIME and getmtime are both in seconds since the epoch, so each
	a larger value means a more recent time. 

4. To execute each action, I pass the path of the file and the action specified from the 
	rules for the matched pattern to the execute_action function. In there I use 
	action.format(path=name,name=os.path.basename(name)) because the action contains either
	{path} or {name} so I want to set the path equal to the full path (which is name) and 
	name equal to the basename of the file. Then I use shlex.split to split the action
	string into a list so that I can pass it to execvp. Before that, I fork, and if the 
	pid is equal to 0 (child) then I try to execvp, otherwise (parent) I use os.wait to 
	wait until the child process is finished.

5. Busy waiting in the context of rorschach.py is the time.sleep in each while loop 
	which is time that is spent doing nothing when the processor could spend that time
	doing something much more productive. Cache invalidation is relevant for this program
	if one would have used a dictionary for the file modification times for example. 
	It happens when a file is deleted for example. In this implementation of rorschach,
	we only check for files that exist, and add to the dictionary, we never get rid of
	entries that are deleted because the way we check does not detect files that no 
	longer exist. So our dictionary would only ever grow, not shrink. These would cause
	efficiency issues if we have a lot of files that are constantly being created and
	deleted, we would eventually get a humongous data structure with many useless values.
	Busy waiting would cause ineffiencies if we have a lot of processes trying to run 
	along with rorschach because we would always consume SECONDS seconds of the processor's
	time with doing nothing. One way we can alleviate cache invalidation would be to use
	the method I used in my implementation. My method is probably slower when there are 
	not a lot of files since I always look up the mtime's every loop. As far as busy 
	waiting, we could maybe mitigate it by just running a while loop and not waiting, the
	program would constantly be checking for updates to files, but the computer can swap
	out processes if it needs to because it is not consumed by the sleep function.
