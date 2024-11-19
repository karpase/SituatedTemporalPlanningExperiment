#!/bin/sh

for x in res/*/*/*.log.csv; do
    cat $x;
done
