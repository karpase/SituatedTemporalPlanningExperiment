#!/bin/sh

gawk 'BEGIN {FS=",";} {split($1,a, "/"); domain=a[5]; if ($1 ~ /rcll/) {if ($1 ~ /r1/) {domain="rcll-r1";} else {domain="rcll-r2";}} domains[domain] = 0; instance=a[7]; method=$2; if (method ~ /ALL/) {method="all-tuned";} if( (method ~ /smac.cfg/) && (method !~ /ALL/)) {method="domain-tuned"}; methods[method]=0; solved = 0; if ($3 < (3*715827882)) {solved = 0.333333333333;} if ($3 < (2*715827882)) {solved = 0.66666666666;} if ($3 < 715827882) {solved=1;}  solcount[domain,method] = solcount[domain,method] + solved;}  END {for (met in methods) {printf(",%s", met);} print ""; for (dom in domains) {printf("%s ", dom); for (met in methods) {printf(",%s",solcount[dom,met]); } print "";  }}' $1

