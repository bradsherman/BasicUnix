TLDR - scp
==========

Overview
--------

[scp] is a UNIX command that copies files over an encrypted network.

Examples
--------

- You could use the following command to transfer a file called text.txt
	from your home directory to my home on the afs file space:
	$ scp ~/text.txt bsherma1@student00.cse.nd.edu:~

- If you want to transfer all of the contents of your home directory you
	would use the following command:
	$ scp -r ~ bsherma1@student00.cse.nd.edu:~

Resources
---------

- [Computer Hope](www.computerhope.com/unix/scp.htm)
