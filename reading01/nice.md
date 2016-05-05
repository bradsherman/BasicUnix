TLDR - nice
===========

Overview
--------

[nice] is a UNIX command that runs a command with an adjusted niceness
based on how much CPU power the command requires, with values ranging from -20
(most favorable to the process) to 19 (least favorable). 

Examples
--------

- **Adding niceness**:

	- $ nice -n10 more myfile.txt  // This runs the more command on myfile.txt and adds 
				       // 10 to its niceness, giving it a total of 10. Then 
				       // more can use CPU resources with niceness greater 
				       // than 11, but not less than 11.

Resources
---------

- [Computer Hope] (www.computerhope.com/unix/unice.htm)
