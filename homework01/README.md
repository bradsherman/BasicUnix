Homework 01
===========

Exercise 01
-----------
1. I would use the command cd /afs/nd.edu/user14/csesoft
2. I would use the command cd ../../user14/csesoft
3. I would use the command cd ~/../../user14/csesoft
4. I would use the command ln -s /afs/nd.edu/user14/csesoft

Exercise 02
-----------
1. I would use the command cp -R /usr/share/pixmaps ~/images
2. There are several broken symlinks, I can tell this because 
	they are highlighted red instead of the green of the 
	working symlinks I have. Also, if I try to touch the 
	link, it says that there is no such file or directory.
	They are broken because their paths are relative so 
	they probably do not go where they are supposed to.
3. I would use the command time mv images pixmaps. This command
	took .001 seconds.
4. I would use the command time mv pixmaps /tmp/bsherma1-pixmaps.
	This process took .151 seconds so it is slower because
	it has to move every file to a new location instead of
	just renaming one directory.
5. I would use the command time rm -r /tmp/bsherma1-pixmaps/pixmaps.
	This operation took .006 seconds which is faster than
	copying all of the contents.

Exercise 03
-----------
1. I would use the command ls -lh /afs/nd.edu/user37/ccl/software.
2. I would use the command ls -lt /afs/nd.edu/user37/ccl/software.
3. I would use the command find /afs/nd.edu/user37/ccl/software/cctools/x86_64
	-type f | wc -l to find that there are 1937 files in the directory.
4. I would use the command find /afs/nd.edu/user37/ccl/software/cctools/x86_64
	-name "weaver" -executable to find 4 executables named weaver.
5. I would use the command du /afs/nd.edu/user37/ccl/software/cctools/x86_64 -h | sort -h
	to find that redhat5 is the largest folder in the directory (77MB).
6. I used the same command as number 3 except in the path at the end I 
	added /redhat5 to find that there are 768 files in that directory.
7. The largest file in the directory is the chirp file which is 989 Kilobytes.
	I used the command find /afs/nd.edu/user37/ccl/software/cctools/x86_64 
	-type f | xargs ls -lh | sort -h.
8. 1937 files in that directory have not been modified in the past 30 days.
	I used the command find /afs/nd.edu/user37/ccl/software/cctools/x86_64
	-type f -ctime +30 | wc -l

Exercise 04
-----------
1. Only the user can read, write, and execute that file, but anyone in the group 
	can read and execute the file, and all others can execute it.
2. These are the commands I would use: 
	a. I would use the command chmod 600 data.txt.
	b. I would use the command chmod 770 data.txt.
	c. I would use the command chmod 444 data.txt.
	d. I would use the command chmod 000 dtat.txt.
3. Anyone who has read and write permissions on the parent directory can 
	delete a file that has no permissions.

Exercise 05
-----------
1. When I use that command in my home and Public directory the outputs are the same
	but when I use it in my Private directory the nd_campus and system authuser
	information does not appear. This means that in our Private folders authorized
	users and nd_campus do not have any permissions. However, on our Public
	and Home directories, all four users have more permissions.
2. The permissions are read only because when I tried to use the touch command
	in that directory it says read-only file system. Therefore, I can only look
	at files in that directory.
3. I could use the command fs setacl -clear -dir /afs/nd.edu/user13/bsherma1 -acl 
	bsherma1 pbui rlidkwa.

Exercise 06
-----------
1. The permissions for world1.txt are that each type of user can read and write.
	The permissions for world2.txt are that the user can read and write and
	group members and others can only read. The permissions for world3.txt are
	that the user can read and write, and group members and others can write.
	They are different because umask sets the default permission settings for
	new files. This is helpful because instead of changing the permissions after 
	creating new files, you can use a umask command to automatically have your
	new files with a certain set of permissions.
