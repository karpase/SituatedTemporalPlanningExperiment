from collections import defaultdict
import os
import platform

hostname = platform.node()

domains = defaultdict(list)

cwd = os.getcwd()


name = "airport-time-windows"
for x in range(1,51): 
	domain = "pddl-instances/ipc-2004/domains/airport-temporal-time-windows-strips/domains/domain-" + str(x) + ".pddl" 
	problem = "pddl-instances/ipc-2004/domains/airport-temporal-time-windows-strips/instances/instance-" + str(x) + ".pddl"
	domains[name].append((domain,problem))

name = "pipesworld-no-tankage-temporal-deadlines"	
for x in range(1,31): 
	domain = "pddl-instances/ipc-2004/domains/pipesworld-no-tankage-temporal-deadlines-strips/domain.pddl" 
	problem = "pddl-instances/ipc-2004/domains/pipesworld-no-tankage-temporal-deadlines-strips/instances/instance-" + str(x) + ".pddl"
	domains[name].append((domain,problem))

name = "satellite-complex-time-windows"
for x in range(1,37): 
	domain = "pddl-instances/ipc-2004/domains/satellite-complex-time-windows-strips/domain.pddl"
	problem = "pddl-instances/ipc-2004/domains/satellite-complex-time-windows-strips/instances/instance-" + str(x) + ".pddl"
	domains[name].append((domain,problem))

name = "satellite-time-time-windows"	
for x in range(1,37): 
	domain = "pddl-instances/ipc-2004/domains/satellite-time-time-windows-strips/domain.pddl"
	problem = "pddl-instances/ipc-2004/domains/satellite-time-time-windows-strips/instances/instance-" + str(x) + ".pddl"
	domains[name].append((domain,problem))

name = "umts-flaw-temporal-time-windows"	
for x in range(1,51): 
	domain = "pddl-instances/ipc-2004/domains/umts-flaw-temporal-time-windows-strips/domain.pddl"
	problem = "pddl-instances/ipc-2004/domains/umts-flaw-temporal-time-windows-strips/instances/instance-" + str(x) + ".pddl"
	domains[name].append((domain,problem))

name = "umts-temporal-time-windows"		
for x in range(1,51): 
	domain = "pddl-instances/ipc-2004/domains/umts-temporal-time-windows-strips/domain.pddl"
	problem = "pddl-instances/ipc-2004/domains/umts-temporal-time-windows-strips/instances/instance-" + str(x) + ".pddl"
	domains[name].append((domain,problem))

name = "trucks-time-constraints-timed-initial-literals"	
for x in range(1,21): 
	domain = "pddl-instances/ipc-2006/domains/trucks-time-constraints-timed-initial-literals/domain.pddl"
	problem = "pddl-instances/ipc-2006/domains/trucks-time-constraints-timed-initial-literals/instances/instance-" + str(x) + ".pddl"
	domains[name].append((domain,problem))	

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

name = "turtlebot"
for y in range(1,9):
	domain = "pddl-instances/turtlebot/bailout1/domain_turtlebot_bailout.pddl"
	problem = "pddl-instances/turtlebot/bailout1/problem_turtlebot_4_bailout_" + str(y) + ".pddl"
	domains[name].append((domain,problem))

for y in range(1,7):
	domain = "pddl-instances/turtlebot/bailout2/domain_turtlebot_bailout.pddl"
	problem = "pddl-instances/turtlebot/bailout2/problem_turtlebot_5_bailout_" + str(y) + ".pddl"
	domains[name].append((domain,problem))


planner = os.path.join(cwd,"rewrite-no-lp")
configurations = []
#configurations.append( ("ijcai","--deadline-aware-open-list IJCAI --forbid-self-overlapping-actions") )


def add_dda_config(configurations, rep, allocate_tu_expansions=True, gamma=1, min_pf=0.001, t_u=100, r=100, nexp=100, fweight=-0.000001, rt_multiplier=1, tilmult=1, time_aware_heuristic=0):
	name = 	"dda__r" + str(rep) + "__allocatetuexpansions_" + str(allocate_tu_expansions) + "__gamma_" + str(gamma) + "__minpf_" + str(min_pf) + "__tu_" + str(t_u) + "__r_" + str(r) + "__nexp_" + str(nexp) + "__fweight_" + str(fweight) + "__rtmultiplier_" + str(rt_multiplier) + "__tilmult_" + str(tilmult) + "__time_aware_heuristic_" + str(time_aware_heuristic)
	cmd_params = "--include-metareasoning-time --multiply-TILs-by " + str(tilmult) + " --real-to-plan-time-multiplier " + str(rt_multiplier) + " --calculate-Q-interval " + str(r) + " --add-weighted-f-value-to-Q "  + str(fweight) + " --min-probability-failure " + str(min_pf) + "  --slack-from-heuristic  --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --ijcai-gamma " + str(gamma) + " --ijcai-t_u " + str(t_u) + " --icaps-for-n-expansions " + str(nexp)  + " --time-aware-heuristic " + str(time_aware_heuristic)
	if allocate_tu_expansions:
		cmd = planner + " --allocate-t_u-expansions " + cmd_params
	else:
		cmd = planner + "  " + cmd_params

	configurations.append( (name, cmd) )

for rep in range(20):
	for tilmult in [1]:
		for planning_time_naive in [0, 0.1, 1, 10, 100]:
			configurations.append( ("naive__r" + str(rep) + "__pt_" + str(planning_time_naive),
				os.path.join(cwd, "naive.sh") + " " + str(planning_time_naive)  ))

		configurations.append( ("icaps2018__r" + str(rep) + "__tilmult_" + str(tilmult),
			planner + " --multiply-TILs-by " + str(tilmult) + " --forbid-self-overlapping-actions --deadline-aware-open-list Focal --slack-from-heuristic") )
		add_dda_config(configurations, rep, time_aware_heuristic=0)
		add_dda_config(configurations, rep, time_aware_heuristic=1)

#		add_dda_config(configurations, rep, allocate_tu_expansions=False)

#		for gamma in [-10, -1, 0, 0.5, 0.75, 1.5, 5, 10]:
#			add_dda_config(configurations, rep, gamma=gamma)
#		for tu in [1, 10, 1000, 10000]:
#			add_dda_config(configurations, rep, t_u=tu, r=tu)
#		for nexp in [1, 10, 1000, 10000]:
#			add_dda_config(configurations, rep, nexp=nexp)

#		for fweight in [-0.000001, -1, -1000000]:
#			add_dda_config(configurations, rep, fweight=fweight)
		


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


