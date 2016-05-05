TLDR - strace
=====

Overview
--------

Records and displays all the system calls called by a process and the signals it receives while it is running

Examples
--------

- Outputs all "open" system commands performed by ls

    $strace -e trace=open ls

Resources
---------

- [TutorialsPoint](www.tutorialspoint.com/unix_commands/strace.htm)
