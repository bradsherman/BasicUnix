Homework 05
===========

Activity 01
-----------
1. I constructed the source by hardcoding the upper and lower case alphabet.
2. I constructed the target set by slicing my source set with the key value that the
	user inputs. I slice it from 1-keyValue and then from keyValue+1-the end of the 
	alphabet so as not to repeat the letter corresponding to the keyValue.
3. Using these sets, I used cut to slice the two source sets into two target sets. Then
	I used tr to actually map the user's string to the encoded string. For example,
	I start with A-Za-z as my source, and if the user picks a key of say 3, the target
	set will become D-ZA-Cd-za-c, which is where the four target sets come from.
	Then tr uses a one-to-one mapping to encode the string.

Activity 02
-----------
1. I filtered the URL's by writing a function called getUrl. I looked at the output of 
	the json tool and saw that it uses : as a delimiter. So, my function uses awk
	with : as a delimiter. Then I noticed that every web address contains another
	colon after http(s), so I printed the second and third fields.
2. To handle the different options, I used getopts. This is pretty straight forward 
	except for when the user puts both the -r and -s options. I used
	the shuf and sort commands to get different ordering. I also used 
	the head command to only allow a certain amount of links to show.
3. Because of the command line options, I had to use getopts to get all 
	the flags. If the -s and -r flags are passed at the same time, only
	the last one should be used. So to do this, in getopts if I see an
	r flag I set the rand variable to shuf and the order variable to cat.
	If the script finds a -s flag, it sets order to sort and rand to cat.
	That way one flag reverses the other so that only the last one passed
	actually works. Also, by default the display variable is set to head, 
	which prints out 10 links, but if the user uses a -n flag, I capture
	the argument and set display to head -$numlinks to only display the 
	specified number of links. 

Activity 03
-----------
1. I removed comments that started a line by using 'sed 's/^$delim/\n/g''.
	This looks for any line that begins with the delim variable 
	(the comment indicator) and replaces it with a blank line. If a 
	comment is at the end of a line, I get rid of it by using the 
	command 'awk -F"$delim" '{print  $1}''. This uses our comment 
	indicator as a field separator and only prints the first field.
2. I removed empty lines with the command 'sed '/^[[:blank:]]*$/d''. This
	looks for any line that only contains a type of space and removes
	them. 
3. I use getopts to get the flags, and in the case statement, if the script
	finds -d it sets the delim variable to the argument, and if it finds
	the -W flag, it sets the rmwhite variable (which previously removed
	blank lines) to cat, which makes it do nothing, therefore preserving
	blank lines. 
