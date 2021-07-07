#!/bin/sh

./collect_naive_results.sh
./collect_results.sh | grep -v naive
