#!/bin/sh
sort $1 | gawk 'BEGIN {FS=",";} {split($1,a, "/"); split(a[2], b, "_"); domain=b[1]; sb[domain] = sb[domain] + $2;   sd[domain] = sd[domain] + $3; st[domain] = st[domain] + $4; } END {print "domain, baseline, DDA-default, DDA-tuned"; for (d in sb) {printf(",%s,%d,%d,%d\n", d,sb[d],sd[d],st[d]);}  }' 
