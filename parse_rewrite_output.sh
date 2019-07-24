#!/bin/sh
# $1 - log file

solved=`grep "Solution Found" $1`
unsolvable=`grep "Problem Unsolvable" $1 `
stime=`grep "; Time [0-9]*" $1 | gawk '{print $3;}' `
generated=`grep "Nodes Generated: [0-9]*" $1 | gawk '{print $4;}'`
expanded=`grep "Nodes Expanded: [0-9]*" $1 | gawk '{print $4;}'`
evaluated=`grep  "Nodes Evaluated: [0-9]*" $1 | gawk '{print $4;}'`
makespan=`tail -1 $1 | gawk '{print $1 + substr($(NF-2),2);}'`

echo $solved,$unsolvable,$stime,$generated,$expanded,$evaluated,$makespan


