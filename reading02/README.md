Reading 02
==========

1. uname > uname.txt
2. ip addr show
3. host *domainname*
4. ping "machine_name" 
5. If I wanted to transfer a file from my home directory called text.txt I 
	would use the following command:
	scp ~/text.txt username@destination.com:~/new
	This would transfer my file to the destination computer (destination.com)
	with the username "username" in the new folder in the home directory.
6. tmux new -s sessionName would create a new session, and in order to 
	detach from it I would use tmux detach, and in order to reattach
	I would use tmux a -t sessionName.
7. I would use the command wget "fileURL"
8. I would use the command netcat -z hostName startPort-endPort
