#!/bin/sh

gawk 'BEGIN {FS=",";} {split($1,a, "/"); domain=a[2]; instance=a[3]; method=a[4]; solved=($2 ~ /Solution Found/); domains[domain]=0; methods[method]=0; solcount[domain,method] = solcount[domain,method] + solved;} END {for (met in methods) {printf(",%s", met);} print ""; for (dom in domains) {printf("%s ", dom); for (met in methods) {printf(",%s",solcount[dom,met]); } print "";  }}' $1
