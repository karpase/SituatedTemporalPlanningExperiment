\#!/bin/sh
# Parameters: <domain> <problem> <til_adjustment>
# Implements the naive approach: takes as input a PDDL domain and file, and
# 1. Adjusts the timestamps of the TILs by til_adjustment
# 2. Calls a planner on the new problem
# 3. Adjusts the timestamps on the resultsing plan
# 4. Calls VAL to check the new plan
# Returns 0 if this works, non-zero otherwise


PLANNER="$HOME/SituatedTemporalPlanningExperiment/rewrite-no-lp --real-to-plan-time-multiplier 0"
VAL=$HOME/SituatedTemporalPlanningExperiment/validate

if [ $# -lt 3 ] 
  then
    echo "Usage: naive.sh <domain> <problem> <til_adjustment>"
    exit
fi

probname=`basename $2`

# Adjust PDDL problem
python3 adjust_til.py $1 $2 $3 $2.adj_$3


# Call Planner
$PLANNER $1 $2.adj_$3 > $2.adj_$3.planner.out

# Extract solution and adjust it
gawk --assign=ta=$3 'BEGIN {found=0;} {if (($2 == "Solution") && ($3 == "Found")) {found=1;} if ((found == 1) && (substr($1,1,1) != ";")) {printf("%f: %s\n", $1+ta, substr($0, index($0,":")+1)) }}'  $2.adj_$3.planner.out > $2.adj_$3.planner.out.adjusted

# Validate adjusted solution against original problem
$VAL -t 0.001 $1 $2 $2.adj_$3.planner.out.adjusted > $2.adj_$3.val

echo $?
