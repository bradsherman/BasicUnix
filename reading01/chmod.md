TLDR - chmod
============

Overview
--------

[chmod] is a UNIX command that changes file access rights for users

Examples
--------

- **User** privileges:
	
	$ chmod u=rwx myfile.txt  // Gives reading, writing, and executing priviliges to the user on myfile.txt

- **Groups** priviliges:
	
	$ chmod g=rw myfile.txt  // Gives reading and writing priviliges to the groups that own myfile.txt

- **Other** privileges:
	
	$ chmod o=x myfile       // Gives executing priviliges to any other user on myfile

Resources
---------

- [Computer Hope] (www.computerhope.com/unix/uchmod.htm)
