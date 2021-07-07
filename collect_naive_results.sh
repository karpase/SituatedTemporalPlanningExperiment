#!/bin/sh

for x in res/*/*/naive*.log; do
	y=${x%.log}
	pt=`echo $y | gawk 'BEGIN {FS="_";} {print $NF;}'`
	./parse_naive_output.sh $y.adj_$pt; 
done
