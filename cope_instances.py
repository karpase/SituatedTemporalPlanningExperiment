from collections import defaultdict
import os
import platform

hostname = platform.node()

domains = defaultdict(list)

cwd = os.getcwd()


# name = "airport-time-windows"
# for x in range(1,51): 
# 	domain = "pddl-instances/ipc-2004/domains/airport-temporal-time-windows-strips/domains/domain-" + str(x) + ".pddl" 
# 	problem = "pddl-instances/ipc-2004/domains/airport-temporal-time-windows-strips/instances/instance-" + str(x) + ".pddl"
# 	domains[name].append((domain,problem))

# name = "pipesworld-no-tankage-temporal-deadlines"	
# for x in range(1,31): 
# 	domain = "pddl-instances/ipc-2004/domains/pipesworld-no-tankage-temporal-deadlines-strips/domain.pddl" 
# 	problem = "pddl-instances/ipc-2004/domains/pipesworld-no-tankage-temporal-deadlines-strips/instances/instance-" + str(x) + ".pddl"
# 	domains[name].append((domain,problem))

# name = "satellite-complex-time-windows"
# for x in range(1,37): 
# 	domain = "pddl-instances/ipc-2004/domains/satellite-complex-time-windows-strips/domain.pddl"
# 	problem = "pddl-instances/ipc-2004/domains/satellite-complex-time-windows-strips/instances/instance-" + str(x) + ".pddl"
# 	domains[name].append((domain,problem))

# name = "satellite-time-time-windows"	
# for x in range(1,37): 
# 	domain = "pddl-instances/ipc-2004/domains/satellite-time-time-windows-strips/domain.pddl"
# 	problem = "pddl-instances/ipc-2004/domains/satellite-time-time-windows-strips/instances/instance-" + str(x) + ".pddl"
# 	domains[name].append((domain,problem))

# name = "umts-flaw-temporal-time-windows"	
# for x in range(1,51): 
# 	domain = "pddl-instances/ipc-2004/domains/umts-flaw-temporal-time-windows-strips/domain.pddl"
# 	problem = "pddl-instances/ipc-2004/domains/umts-flaw-temporal-time-windows-strips/instances/instance-" + str(x) + ".pddl"
# 	domains[name].append((domain,problem))

# name = "umts-temporal-time-windows"		
# for x in range(1,51): 
# 	domain = "pddl-instances/ipc-2004/domains/umts-temporal-time-windows-strips/domain.pddl"
# 	problem = "pddl-instances/ipc-2004/domains/umts-temporal-time-windows-strips/instances/instance-" + str(x) + ".pddl"
# 	domains[name].append((domain,problem))

# name = "trucks-time-constraints-timed-initial-literals"	
# for x in range(1,21): 
# 	domain = "pddl-instances/ipc-2006/domains/trucks-time-constraints-timed-initial-literals/domain.pddl"
# 	problem = "pddl-instances/ipc-2006/domains/trucks-time-constraints-timed-initial-literals/instances/instance-" + str(x) + ".pddl"
# 	domains[name].append((domain,problem))	

for r in range(1,4):
	name = "rcll-" + str(r) + "-robots"
	for o in range(1,101):		
		domain = "pddl-instances/rcll/rcll_domain_production_durations_time_windows.pddl"
		problem = "pddl-instances/rcll/problem-" + "{0:0=3d}".format(o) + "-r" + str(r) + "-o1-durations.pddl"
		domains[name].append((domain,problem))

#for r in range(1,3):
#	name = "orig-rcll-" + str(r) + "-robots"
#	for o in range(1,101):		
#		domain = "pddl-instances/orig-rcll/rcll_domain_production_durations.pddl"
#		problem = "pddl-instances/orig-rcll/problem-" + "{0:0=3d}".format(o) + "-r" + str(r) + "-o1-durations.pddl"
#		domains[name].append((domain,problem))

#for r in range(1,3):
#	name = "rcll-fixed-dl" + str(r) + "-robots"
#	for o in range(1,101):		
#		domain = "pddl-instances/rcll-fixed-dl/rcll_domain_production_durations_time_windows.pddl"
#		problem = "pddl-instances/rcll-fixed-dl/problem-" + "{0:0=3d}".format(o) + "-r" + str(r) + "-o1-durations.pddl"
#		domains[name].append((domain,problem))

name = "turtlebot4"
for y in range(1,9):
	domain = "pddl-instances/turtlebot/bailout1/domain_turtlebot_bailout.pddl"
	problem = "pddl-instances/turtlebot/bailout1/problem_turtlebot_4_bailout_" + str(y) + ".pddl"
	domains[name].append((domain,problem))

name = "turtlebot5"
for y in range(1,7):
	domain = "pddl-instances/turtlebot/bailout2/domain_turtlebot_bailout.pddl"
	problem = "pddl-instances/turtlebot/bailout2/problem_turtlebot_5_bailout_" + str(y) + ".pddl"
	domains[name].append((domain,problem))


planner = os.path.join(cwd,"rewrite-no-lp")
configurations = []
#configurations.append( ("ijcai","--deadline-aware-open-list IJCAI --forbid-self-overlapping-actions") )




default_cmd_params = "--include-metareasoning-time --multiply-TILs-by 1 --real-to-plan-time-multiplier 1 --calculate-Q-interval 100 --add-weighted-f-value-to-Q -0.000001 --min-probability-failure 0.001 --slack-from-heuristic --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --ijcai-gamma 1 --ijcai-t_u 100 --icaps-for-n-expansions 100 --time-aware-heuristic 1 --dispatch-frontier-size 1 --subtree-focus-threshold 1 --optimistic-lst-for-dispatch-reasoning"

def add_config(configurations, expansions_per_second, dispatch, dispatch_threshold=None):
	cmd_params = default_cmd_params + " --time-based-on-expansions-per-second " + str(expansions_per_second)
	if not dispatch:
		name = "nodisp"
	else:
		name = "disp_" + str(dispatch_threshold)
		cmd_params = cmd_params + " --use-dispatcher LPFThreshold --dispatch-threshold " + str(dispatch_threshold)
	
	cmd = planner + "  " + cmd_params
	configurations.append( (name, cmd) )

for expansions_per_second in [10, 20, 50, 100, 200, 300, 500, 100]:
	add_config(configurations, expansions_per_second, dispatch=False)		
	for dispatch_threshold in [0.025, 0.1, 0.25]:
		add_config(configurations, expansions_per_second, dispatch=True, dispatch_threshold=dispatch_threshold)		
	


for d in domains:
	for (i,(dom,prob)) in enumerate(domains[d]):
		assert(os.path.isfile(dom))
		assert(os.path.isfile(prob))
		os.makedirs("res/" + d + "/" + str(i))
		for cname,c in configurations:  
			if cname[:5] == "naive":
				#print("(ulimit -t 200; " + c + " " + os.path.join(cwd,dom) + " " + os.path.join(cwd,prob) + " " + os.path.join(cwd,"res",d,str(i),cname) + " >& " + os.path.join(cwd,"res",d,str(i),cname + ".log)"))
				print(c + " " + os.path.join(cwd,dom) + " " + os.path.join(cwd,prob) + " " + os.path.join(cwd,"res",d,str(i),cname) + " " + os.path.join(cwd,"res",d,str(i),cname + ".log"))
			else:
				#print("(ulimit -t 200; " + c + " " + os.path.join(cwd,dom) + " " + os.path.join(cwd,prob) + " >& " + os.path.join(cwd,"res",d,str(i),cname + ".log)"))
				print(c + " " + os.path.join(cwd,dom) + " " + os.path.join(cwd,prob) + " " + os.path.join(cwd,"res",d,str(i),cname + ".log"))

