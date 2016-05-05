TLDR - sed
=====

Overview
--------

filters and manipulates text from files or standard input

Examples
--------

- replaces all instances of 'abc' with 'xyz' in myfile

    $sed -i -e 's/abc/xyz/g' myfile

- ark all instances of 'homework' in myfile

    $sed -i -e 's/homework/(&)/g' myfile

Resources
---------

- [Computer Hope](www.computerhope.com/unix/used.htm)
- [ech Tutorials](http://arkit.co.in/linux/sed-command-20-practical-examples/)
