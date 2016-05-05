#!/bin/sh

export PATH=/afs/nd.edu/user15/pbui/pub/bin:$PATH

cowsay -f tux "What do you want?"
n=0

while [ $n -lt 10 ]; do
	trap "cowsay -f moose 'You have pressed the special button.'; exit 0" SIGHUP
	trap "cowsay -f vader 'You tried to destroy me, now I will destroy you!'; exit 0" SIGINT
	trap "cowsay -f koala 'You just killed a koala. Nice'; exit 0" SIGTERM
	sleep 1
	n=$((n+1))
done


cowsay -f skeleton "Too late! Try again later."
exit 0
