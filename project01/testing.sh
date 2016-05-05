#!/bin/sh

printf "Enter the hostname of your unforked server (example: student02.cse.nd.edu): \n"
read host

printf "Enter the port number: \n"
read port

##################################################
#####    Latency Testing
##################################################
printf "Testing Latency\n\n"
static=''
directory=''
cgi=''
# Test static file 
printf "Testing static file\n"

staticave=$(./thor.py -v -r 10 $host:$port/www/hello.html 2>&1 > /dev/null | grep Average | awk -v FS=":" '
	BEGIN {sum=0;count=0;}
	// {sum = sum + $4
		count = count + 1}
		END {print sum/NR}') 
# Test Directory Listing
printf "Testing directory listing\n"
directoryave=$(./thor.py -v -r 10 $host:$port/www 2>&1 > /dev/null | grep Average | awk -v FS=":" '
	BEGIN {sum=0;count=0;}
	// {sum = sum + $4
		count = count + 1}
		END {print sum/NR}')
# Test cgi scripts
printf "Testing cgi scripts\n"
cgiave=$(./thor.py -v -r 10 $host:$port/www/cgi-bin/hello.sh 2>&1 > /dev/null | grep Average | awk -v FS=":" '
	BEGIN {sum=0;count=0;}
	// {sum = sum + $4
		count = count + 1}
		END {print sum/NR}')

echo -e "Latency\t$staticave\t$directoryave\t$cgiave" > latency.txt

printf '\n'

##################################################
#####     Throughput Testing
##################################################
printf "Testing throughput\n\n"
# Test 1KB file
printf "Testing 1KB file\n"
kb=$(./thor.py -v -r 10 $host:$port/www/1KB.txt 2>&1 > /dev/null | grep Average | awk -v FS=":" '
	BEGIN {sum=0;count=0;}
	// {sum = sum + $4
		count = count + 1}
		END {sum = sum/NR
		# for when time is basically 0
		if(sum == 0)
			sum = .001;
		print 1024/sum}')
# Test 1MB file
printf "Testing 1MB file\n"
mb=$(./thor.py -v -r 10 $host:$port/www/1MB.txt 2>&1 > /dev/null | grep Average | awk -v FS=":" '
	BEGIN {sum=0;count=0;}
	// {sum = sum + $4
		count = count + 1}
		END {sum = sum/NR
		# for when time is basically 0
		if(sum == 0) 
			sum = .001;
		print 1048576/sum}')
# Test 1GB file
printf "Testing 1GB file\n"
gb=$(./thor.py -v -r 5 $host:$port/www/1GB.txt 2>&1 > /dev/null | grep Average | awk -v FS=":" '
	BEGIN {sum=0;count=0;}
	// {sum = sum + $4
		count = count + 1}
		END {sum = sum/NR
		# for when time is basically 0
		if(sum == 0)
			sum = .001;
		print 1073741824/sum}')
echo -e "Throughput\t$kb\t$mb\t$gb" > throughput.txt


# Forked Server Testing

printf "Enter the hostname of your forked server (example: student02.cse.nd.edu): \n"
read host

printf "Enter the port number: \n"
read port

# Test Static File
printf "Testing static file\n"
staticave=$(./thor.py -v -r 8 $host:$port/www/hello.html 2>&1 > /dev/null | grep Average | awk -v FS=":" '
	BEGIN {sum=0;count=0;}
	// {sum = sum + $4
		count = count + 1}
		END {print sum/NR}') 
# Test Directory Listing
printf "Testing directory listing\n"
directoryave=$(./thor.py -v -r 8 $host:$port/www 2>&1 > /dev/null | grep Average | awk -v FS=":" '
	BEGIN {sum=0;count=0;}
	// {sum = sum + $4
		count = count + 1}
		END {print sum/NR}')
# Test cgi scripts
printf "Testing cgi scripts\n"
cgiave=$(./thor.py -v -r 8 $host:$port/www/cgi-bin/hello.sh 2>&1 > /dev/null | grep Average | awk -v FS=":" '
	BEGIN {sum=0;count=0;}
	// {sum = sum + $4
		count = count + 1}
		END {print sum/NR}')

echo -e "Latency\t$staticave\t$directoryave\t$cgiave" > latencyforked.txt


##################################################
#####     Throughput Testing
##################################################
printf "Testing throughput\n\n"
# Test 1KB file
printf "Testing 1KB file\n"
kb=$(./thor.py -v -r 8 $host:$port/www/1KB.txt 2>&1 > /dev/null | grep Average | awk -v FS=":" '
	BEGIN {sum=0;count=0;}
	// {sum = sum + $4
		count = count + 1}
		END { sum = sum/count
		print 1024/sum}')
# Test 1MB file
printf "Testing 1MB file\n"
mb=$(./thor.py -v -r 8 $host:$port/www/1MB.txt 2>&1 > /dev/null | grep Average | awk -v FS=":" '
	BEGIN {sum=0;count=0;}
	// {sum = sum + $4
		count = count + 1}
		END {sum = sum/count
		print 1048576/sum}')
# Test 1GB file
printf "Testing 1GB file\n"
gb=$(./thor.py -v -r 8 $host:$port/www/1GB.txt 2>&1 > /dev/null | grep Average | awk -v FS=":" '
	BEGIN {sum=0;count=0;}
	// {sum = sum + $4
		count = count + 1}
		END {sum = sum/count
		print 1073741824/sum}')
echo -e "Throughput\t$kb\t$mb\t$gb" > throughputforked.txt

exit 0
