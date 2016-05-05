Homework 02
===========

Activity 01
-----------

1. 
# Create workspace on source machine (logged in on student00)
$ mkdir /tmp/bsherma1-workspace

# Generate 10MB file full of data
$ dd if=/dev/urandom of=sample.txt bs=10M count=1

# Create 10 hard links to 10MB file (changing the number after data each time)
$ ln sample.txt data0

# Create workspace on target machine (logged in on student01)
$ mkdir/tmp/bsherma1-workspace

2. The total disk usage is 11M which is not surprising because the sample.txt 
	file takes up 10M and the links do not use much disk space.

3. The total disk usage is 101M which is suprising because the links in the 
	source folder did not take up much space but now in the target folder
	they are taking up 10M each (equivalent to the original file). This
	is because when the hard links are transfered, they are basically
	transfered as the original file, so in the target folder it makes sense
	that if we have 10 instances of the original 10MB file, the disk
	usage would be around 100M.
4.
# Transfer data files using scp
$ scp ./data\* bsherma1@student01.cse.nd.edu:/tmp/bsherma1-workspace

# Transfer data files using sftp
$ sftp bsherma1@student01.cse.nd.edu < sftpfile.txt

# 	Contents of sftpfile.txt
	put /tmp/bsherma1-workspace/data* /tmp/bsherma1-workspace

# Transfer data files using rsync
$ rsync /tmp/bsherma1-workspace/data\* bsherma1@student01.cse.nd.edu:/tmp/bsherma1-workspace

5. When using scp and sftp each data file is only transferred once.
	However, rsync checks to see if a file has been modified since the
	last copy, and does not	copy it if it has not been modified. This 
	is useful because you can use rsync to regularly copy large 
	directories and it will only copy the files you have modified 
	since the last time it copied them.

6. Because of the reasons stated above, I prefer rsync because I think the
	syntax is simple and the feature mentioned above will save time 
	if I want to use it on large directories.

Activity 02
-----------

1. Scan for http port:
	$ nc -z xavier.h4x0r.space 9000-10000
	Output:
	Connection to xavier.h4x0r.space 9097 port [tcp/*] succeeded!
	Connection to xavier.h4x0r.space 9111 port [tcp/*] succeeded!
	Connection to xavier.h4x0r.space 9876 port [tcp/sd] succeeded!

2. Next I typed all of the addresses into my browser to see if they were HTTP
	ports. I found that port 9876 gives a clue to finding the ORACLE.

3. Then, I got my code and decoded it using the command:
	$ base64 -d code

4. Then, I queried the doorman by appending my netid and passcode to the 
	end of the url I was on.

5. The DOORMAN told me where to find the SLEEPER, so when I found him
	I had to enter the following three lines of code to get him 
	to give me my message to the ORACLE:
	$ ./SLEEPER &
	$ ps
	$ kill -HUP *pid*

6. After that I used the following command to deliver my message to the ORACLE:
	$ telnet xavier.h4x0r.space 9111

7. Then I entered my netid and my message from the SLEEPER, and my reason 
	for taking so long. Then I finished the journey!   
