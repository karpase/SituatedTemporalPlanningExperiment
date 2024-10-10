#!/bin/bash
# $1 - file with list of commands to run

rm $1.com.*

shuf $1 > $1.shuf
split -l 1000 $1.shuf $1.com.

for x in $1.com.*; do
    echo '#!/bin/bash' > $x.pbs;
    echo '#PBS -N' $x >> $x.pbs;
    echo '#PBS' -q zeus_all_q >> $x.pbs;
    echo '#PBS' -l select=1:ncpus=20 >> $x.pbs;
    echo '#PBS' -l walltime=23:55:00  >> $x.pbs;
    echo '#PBS' -m abe >> $x.pbs;
    echo '#PBS' -M  karpase@technion.ac.il >> $x.pbs;

    PBS_O_WORKDIR=`pwd`
    echo cd $PBS_O_WORKDIR  >> $x.pbs;

    echo python $PBS_O_WORKDIR/parallel.py --filename $PBS_O_WORKDIR/$x --num_processes 20 --timeout 600 >> $x.pbs

done
