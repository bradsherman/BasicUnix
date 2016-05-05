Homework 07
===========

Activity 01
-----------
1. I parsed the command line options by using sys.argv[1:]. I took the program name to be
	sys.argv[0], and then for each item in sys.argv[1:] I used split with '=' as a d
	delimiter. Then I checked to see if the first item matched if, of, or any of the other
	options, and if it did, set the second item to the variable corresponding to that 
	option.

2. To open the input and output files, I wrote a function to wrap the system call of 
	os.open, and I used the mode of os.O_RDONLY for the input file and the modes of either
	os.O_WRONLY or os.O_CREAT for the output file. My wrapper function tries to open the
	files and catches any errors and gives an error message if there was an error.

3. For the seek and skip arguments, I first checked to see if the user gave an input or 
	output file. If not, then we are reading from standard in or standard out, which we
	cannot use lseek on. Therefore, if we are given an input or output file, then I open
	the file and use skipnum for input and seeknum for output. I multiply seek/skipnum by
	the blocksize as well, that way when we I use the file descriptors they are at the point
	in the file that the user specified.

4. For count, I keep track of how many datablocks have been written, and continue to write
	data as long as datablocks_written is less than count. Before the while loop starts,
	I read data from source, which is the file descriptor for the input file, with the
	appropriate blocksize. The while loop runs while there is still data and while
	datablocks_written is less than count. Then the data is written to the target with 
	the appropriate blocksize, and more data is read in from source. This continues while
	the while loop continues to run and then both file descriptors are closed.

Activity 02
-----------
1. I parsed the command line options by going from 0 to the length of the command line 
	options (sys.argv[2:]). I go from 2 to the end because sys.argv[0] is the program
	name and sys.argv[1] is the directory we are searching. If the item matches an option
	that has an argument, I check the next argument in the list to set it equal to the 
	corresponding variable.

2. I walked the directory by using os.walk. I take root, dirs, and files from the sorted
	walk output. I made sure to set the followlinks option for os.walk to true so we
	follow symbolic links. Then I have another for loop in the list of dirs + files, and 
	loop through that list to check each item.

3. To determine whether or not to print a file object, I used an include function. In that,
	I have multiple if statements to check to see if flags for the command line options
	are 1, which means the user added that option. If an option is passed, in its if 
	statement I check to see if the desired traits are NOT present. If so, I return false.
	That way, if the file makes it through all of the specified if statements and has all
	the desired traits, it will make it to the end of the function where I return True,
	meaning print the file object.

4. I used the pipeline:
	$ strace -c find(.py) /etc 
	To figure out how many calls to stat and lstat were made by find.py and find. Results:
	find.py stat calls: 41606
	find.py lstat calls: 21
	find stat calls: 24
	find lstat calls: 0
	One thing that I noticed is that the regular find has zero lstat calls and much less
	stat calls than my find.py script. The regular find uses calls to newfstat and fstat
	instead of stat and lstat. In my opinion, it seems that those two calls are what the 
	regular find uses to get file information.
