#!/bin/sh

gawk 'BEGIN {FS=",";} {split($1,a, "/"); domain=a[2]; instance=a[3]; timelimit=a[4]; method=a[5]; solved=($2 ~ /Solution Found/); domains[domain]=0; methods[method]=0; tls[timelimit]=0; solcount[domain,method,timelimit] = solcount[domain,method,timelimit] + solved;} END {for (met in methods) {for (timelimit in tls) {printf(",%s_%s", met,timelimit);}} print ""; for (dom in domains) {printf("%s ", dom); for (met in methods) {for (timelimit in tls) {printf(",%s",solcount[dom,met,timelimit]); }} print "";  }}' $1
