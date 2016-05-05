#!/bin/sh

URL='curl -s http://catalog.cse.nd.edu:9097/query.text'
if [ $# -gt 0 ]; then
		url=$1;
		URL='curl -s '$url;
fi
$URL | awk '
BEGIN {c=0;m=0;p=none;max=0} 
$1 ~ /^cpus/ { c=c+$2; }
/name/ { names[$2]=names[$2]+1; }
/type/ { types[$2]=types[$2]+1; }

END {print "Total CPUs: "c; 
	for(name in names) m++; 
	print "Total Machines: "m;
	for(type in types){ 
   		if(types[type] > max) p=type
		max = types[type]
	}
	print "Most Prolific Type: " p;
	}
'

