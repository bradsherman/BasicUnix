Homework 03
===========

Activity 01
-----------

1. a.) libgcd.a is smaller than libgcd.so because libgcd.so is an executable so it contains
	much more binary information than the static libgcd.a file which just has object code.

1. b.) gcd-static is larger because once again, it contains all of the code needed to run
	from other libraries. gcd-dynamic just has references to the code and finds
	what it needs when it is run.

2. gcd-static does not depend on any libraries. gcd-dynamic depends on four libraries
	1. linux-vdso.so.1
	2. libgcd.so
	3. libc.so.6
	4. /lib64/ld-linux-x86-64.so.2
	I found this out by using the command:
		$ ldd gcd-dynamic

3. When I first tried to run the gcd-dynamic application it did not work because 
	our libgcd.so library is not in our LD_LIBRARY_PATH variable. I used the command:
		$ setenv LD_LIBRARY_PATH $LD_LIBRARY_PATH\:*path to gcd folder* 
	to set our path to find my libgcd.so library.

4. Some of the advantages of static linking is that you don't have to worry about the
	program finding the library, everything you need to run the program is already in
	the executable. However, it makes the file much, much larger and it isn't always 
	necessary. Also, if a library is updated, that file won't have the updated library
	unless you recompile it. Dynamic linking certainly makes for smaller files, but 
	you have to make sure all your libraries can be found in your path. The benefits 
	are that everytime you run the program you know you have the most up to date 
	version of the libraries. If I was building an application I would want to produce
	a dynamic executable because it takes up less space and I wouldn't have to worry
	about recompiling my program frequently to make sure it is updated.

Activity 02
-----------

1. To download the is_palindrome.tar.gz archive I first copied the link adress then used:
	$wget *link address*
	Then in order to extract the file I used the command:
	$tar -xvzf is_palindrome.tar.gz

2. I used the -g flag to force gcc to include debugging symbols in the executable. This 
	increases the file size from 8MB to 11MB. I found this out by first compiling 
	without -g, and using the du command on the executable, then by doing the same 
	thing except with the -g flag included the second time.

3. The first error I found using gdb. There was a segfault in line 41 in the fgets function
	that caused the program to crash. I fixed it by changing the size of the buffer 
	string to BUFSIZE so that the size of the input did not exceed the size of buffer.
   The second error I found using valgrind. The error was that on line 26 of is_palindrome.c
	the back variable was set to unallocated memory so I had to add a -1. 
   The third error I also found using valgrind. The sanitized string was allocated memory
	but it was never freed. I freed it at the end of the main function to fix this. There
	also was not a null character at the end of the sanitized string so I added that in
	to complete the string.
4. The hardest bug for me was the third one about adding the null character at the end of 
	the string. This was the hardest bug for me because I did not enjoy valgrind and I 
	thought that the errors it gave were very unhelpful. I think the only way to prevent
	this from happening in the future is to become more familiar with the valgrind commands.
	I should also keep my eyes open for this type of bug so that I can spot it in my code
	earlier.

Activity 03
-----------

1. First I went to the directory and ran the courier:
	$ cd /afs/nd.edu/user15/pbui/pub/bin
	$ ./COURIER
   He said "Woah are you sure you put the package in the right place?"

2. Then I used strings to find out more information:
	$ strings COURIER
   I noticed the line "/tmp/%s.deaddrop" so I moved to that directory, noticed other 
   students' usernames.deaddrop so I made my own directory.
	$ mkdir /tmp/bsherma1.deaddrop

3. When I ran the COURIER again he told me to lock down the package:
	$ chmod 700 /tmp/bsherma1.deaddrop

4. I ran the COURIER again and he said the package is the wrong size so I removed my
   directory and made a file.
	$ rm -r /tmp/bsherma1.deaddrop
	$ touch /tmp/bsherma1.deaddrop

5. The COURIER again said that the package is the wrong size so I put some text in my
   file so that it would change the size. Then when I ran the COURIER he said that 
   everything looks good. 
 
