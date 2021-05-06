#!/bin/sh
# $1 - basename

planner_out=$1.planner.out
val_out=$1.val
adj_plan=$1.planner.out.adjusted


solved=`grep "Plan valid" $val_out`
unsolvable=`grep "Problem Unsolvable" $planner_out `
stime=`grep "; Time [0-9]*" $planner_out | awk '{print $3;}' `
generated=`grep "Nodes Generated: [0-9]*" $planner_out | awk '{print $4;}'`
expanded=`grep "Nodes Expanded: [0-9]*" $planner_out | awk '{print $4;}'`
evaluated=`grep  "Nodes Evaluated: [0-9]*" $planner_out | awk '{print $4;}'`
makespan=`tail -1 $adj_plan | awk '{print $1 + substr($(NF-2),2);}'`
metareasoning_time=`grep "Metareasoning time (not discounted): [0-9]*" $planner_out | awk '{print $6;}'`
disc_time=`grep "Discounted time: [0-9]*" $planner_out | awk '{print $4;}'`



echo $1,$solved,$unsolvable,$stime,$generated,$expanded,$evaluated,$makespan,$metareasoning_time,$disc_time


