#!/bin/sh

for x in res/*/*/cope*.log; do 
	./parse_rewrite_output.sh $x; 
done
