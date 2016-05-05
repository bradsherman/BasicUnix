#!/bin/sh

# Collect Statistics about demographics.csv

cat demographics.csv | awk -v FS="," '
	// {
		if(NR==1)
			for( i = 1; i < NF; i+=2 ){
				year[i]=$i;
				male[i]=0;
				female[i]=0;
				caucasian[i]=0;
				oriental[i]=0;
				hispanic[i]=0;
				aa[i]=0;
				na[i]=0;
				multiple[i]=0;
				undeclared[i]=0;	
		}
		else
			for( i = 1; i < NF; i+=2 ){
				j=i+1;
				if($i=="M") male[i]++;
				else if($i=="F") female[i]++;
				if($j=="C") caucasian[i]++;
				else if($j=="O") oriental[i]++;
				else if($j=="S") hispanic[i]++;
				else if($j=="B") aa[i]++;
				else if($j=="N") na[i]++;
				else if($j=="T") multiple[i]++;
				else if($j=="U") undeclared[i]++;
			}
	}
	END {
		for( i = 1; i < NF; i+= 2 )
			print year[i] "," male[i] "," female[i] "," caucasian[i] "," oriental[i] "," hispanic[i] "," aa[i] "," na[i] "," multiple[i] "," undeclared[i];
	}
' > demog.dat

