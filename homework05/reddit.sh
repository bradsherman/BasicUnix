#!/bin/sh


# Get Reddit data
getFeed() {
	curl -s 'http://www.reddit.com/r/'$1'/.json' | python -m json.tool 
}
# Filter all lines that match "url": to get the actual web address
getUrl() {
	awk -F":" '{printf("%s:%s\n", $2,$3)}' 
}

rand='cat'
order='cat'
display='head'
numlinks=0

# Bring in flags
while getopts ":rsn:" arg
do
	case $arg in
		# order='cat' and rand='cat' is to make sure that if 
		# the r and s flag are passed then only the last one
		# is actually used
		r)
			rand='shuf'
			order='cat';;
		s)
			order='sort'
			rand='cat';;
		n)nopt=$OPTARG
			numlinks=$nopt
			display='head -'$numlinks
			;;
		*)echo 1 usage: $0 subreddit [ -r -s -n N ] 
			echo where N is number of links to show
			exit 1;;
	esac
done

shift $((OPTIND-1))

#Check to see if there is a subreddit listed
if [ -z $1 ]; then
	echo 0 usage: $0 subreddit [ -r -s -n N ]
	echo where N is number of links to show
	exit 1
fi

# for each subreddit, list it out according to the user input in a nice display
for subreddit in $@; do
	echo "Links for $subreddit:"
	echo "============================================="
	echo "$(getFeed $subreddit | grep "\"url\":" | getUrl | tr -d '"' | tr -d ',' | $rand | $order | $display)"
	echo -e "\n"
done

exit 0	
