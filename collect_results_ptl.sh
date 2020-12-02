#!/bin/sh

for x in res/*/*/*/*.log; do 
	./parse_rewrite_output.sh $x; 
done
