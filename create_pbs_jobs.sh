#!/bin/bash
# $1 - file with list of commands to run

rm $1.com.*

shuf $1 > $1.shuf
split -l 280 $1.shuf $1.com.

for x in $1.com.*; do
    echo '#!/bin/bash' > $x.pbs;
    echo '#PBS -N' $x >> $x.pbs;
    echo '#PBS' -q zeus_all_q >> $x.pbs;
    echo '#PBS' -l select=1:ncpus=1 >> $x.pbs;
    echo '#PBS' -l walltime=23:30:00  >> $x.pbs;
    echo '#PBS' -m abe >> $x.pbs;
    echo '#PBS' -M  karpase@technion.ac.il >> $x.pbs;

    echo PBS_O_WORKDIR=`pwd`  >> $x.pbs;
    echo cd $PBS_O_WORKDIR  >> $x.pbs;

    cat $x >> $x.pbs;

done
