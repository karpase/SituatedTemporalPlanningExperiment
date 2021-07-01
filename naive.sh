#!/bin/sh
# Parameters: <til_adjustment> <domain> <problem> <basename_for_files>
# Implements the naive approach: takes as input a PDDL domain and file, and
# 1. Adjusts the timestamps of the TILs by til_adjustment
# 2. Calls a planner on the new problem
# 3. Adjusts the timestamps on the resultsing plan
# 4. Calls VAL to check the new plan
# Returns 0 if this works, non-zero otherwise

DIR=$HOME/SituatedTemporalPlanningExperiment
PLANNER="$DIR/rewrite-no-lp --html --real-to-plan-time-multiplier 0"
VAL=$DIR/val

if [ $# -lt 4 ] 
  then
    echo "Usage: naive.sh <til_adjustment> <domain> <problem> <basename_for_files>"
    exit
fi


# Adjust PDDL problem
python3 $DIR/adjust_til.py $2 $3 $1 $4.adj_$1


# Call Planner
$PLANNER $2 $4.adj_$1 > $4.adj_$1.planner.out

# Extract Planning Time
stime=`grep "; Time [0-9]*" $4.adj_$1.planner.out | awk '{print $3;}' `


# Extract solution and adjust it
gawk --assign=ta=$stime 'BEGIN {found=0;} {if (($2 == "Solution") && ($3 == "Found")) {found=1;} if ((found == 1) && (substr($1,1,1) != ";")) {printf("%f: %s\n", $1+ta, substr($0, index($0,":")+1)) }}'  $4.adj_$1.planner.out > $4.adj_$1.planner.out.adjusted

# Validate adjusted solution against original problem
$VAL -t 0.001 $2 $3 $4.adj_$1.planner.out.adjusted > $4.adj_$1.val

echo $?
