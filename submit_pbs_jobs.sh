#!/bin/bash
# $1 - run.txt file

for x in $1.*.pbs; do
        qsub $x;
done

