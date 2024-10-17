#!/bin/sh
# $1 - log file

solved=`grep "Solution Found" $1`
unsolvable=`grep "Problem Unsolvable" $1`
timeout=`grep "TIMEOUT" $1`
stime=`grep "; Time [0-9]*" $1 | awk '{print $3;}' `
generated=`grep "Nodes Generated: [0-9]*" $1 | awk '{print $4;}'`
expanded=`grep "Nodes Expanded: [0-9]*" $1 | awk '{print $4;}'`
evaluated=`grep  "Nodes Evaluated: [0-9]*" $1 | awk '{print $4;}'`
makespan=`tail -1 $1 | awk '{print $1 + substr($(NF-2),2);}'`
metareasoning_time=`grep "Metareasoning time (not discounted): [0-9]*" $1 | awk '{print $6;}'`
disc_time=`grep "Discounted time: [0-9]*" $1 | awk '{print $4;}'`



echo $1,$solved,$unsolvable,$stime,$generated,$expanded,$evaluated,$makespan,$metareasoning_time,$disc_time,$timeout


