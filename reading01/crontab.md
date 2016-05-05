TLDR - crontab
==============

Overview
--------

[crontab] is the name of a UNIX command used to manage a list of commands 
you desire to be performed according to a schedule. This list of commands
is also called the crontab.

Examples
--------

- **An Everyday Task**:
	
	- Open the crontab in a text editor with crontab -e
	- Add a command to be done 
	- The format is:
		1) a number for minute of the hour
		2) a number for hour of the day
		3) a number for day of the month
		4) a number for month of the year
		5) a number for the day of the week
		6) the command you want to be run, exactly as it would appear on the command line
	- So if you wanted to run a script everyday at 12 pm, it would look like this:
		0 12 * * * (path to script)

Resources
---------

- [Computer Hope] (www.computerhope.com/unix/ucrontab.htm)

