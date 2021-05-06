#!/bin/sh

for x in res/*/*/*.log; do
	y=${x%.log}
	pt=`echo $y | gawk 'BEGIN {FS="_";} {print $NF;}'`
	./parse_naive_output.sh $y.adj_$pt; 
done
