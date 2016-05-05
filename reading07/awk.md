Brad Sherman
Reading07
Commands Summary Page

1. To print specific fields I would use:
	$ awk '{print $x;}' where x is the field I want to print
2. To change FS I would use the command:
	$ awk '{FS=":";}' to change the field separator to a colon
3. I would use BEGIN whenever I want something to happen before awk
	starts reading input. I would use END whenever I want something
	to happen after input is read. For example:
	$ awk 'BEGIN {x=0;} "use x to keep track of something" END {print x;}'
	Will initialize x to 0 everytime awk starts and then print x 
	after it reads all the input.
4. For pattern matching, I would use this syntax:
	$ awk '/pattern/ {action to be performed whenever pattern is matched}'
5. NF stands for number of fields in the current line and NR stands for
	the current input record number overall, which basically means the 
	number of lines read in. These are useful if you only want to perform
	an operation on a certain number of fields or lines in a file.
6. Associative arrays are just like C arrays except for the fact that each
	value is referenced by a string and not an index number. The syntax is
	"Name[index]=value" where index is a string. This is useful when counting
	up values of similar objects with different names.
