from collections import defaultdict
import os
import platform

hostname = platform.node()

domains = defaultdict(list)


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

for r in range(1,3):
	name = "rcll-" + str(r) + "-robots"
	for o in range(1,101):		
		domain = "pddl-instances/rcll/rcll_domain_production_durations_time_windows.pddl"
		problem = "pddl-instances/rcll/problem-" + "{0:0=3d}".format(o) + "-r" + str(r) + "-o1-durations.pddl"
		domains[name].append((domain,problem))



planner = "./rewrite-no-lp"
configurations = []
#configurations.append( ("ijcai","--deadline-aware-open-list IJCAI --forbid-self-overlapping-actions") )

#configurations.append( ("icaps2018","./rewrite-no-lp --forbid-self-overlapping-actions --deadline-aware-open-list Focal --slack-from-heuristic") )


for gamma in [1,2,5,10,20,50,100]:
	for min_pf in [0.0001, 0.001, 0.01, 0.1]:
		for t_u in [100, "ETD"]:
#		configurations.append( ("improved_greedy_gamma_" + str(gamma) + "_tu_" + str(t_u), 
#			"./rewrite-no-lp --slack-from-heuristic  --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --ijcai-gamma " + str(gamma) + " --ijcai-t_u " + str(t_u)) )
			configurations.append( ("mt_improved_greedy__r_1000_gamma_" + str(gamma) + "_tu_" + str(t_u) + "_min_pf_" + str(min_pf), 
				"./rewrite-no-lp --include-metareasoning-time --calculate-Q-interval 1000 --min-probability-failure " + str(min_pf) + "  --slack-from-heuristic  --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --ijcai-gamma " + str(gamma) + " --ijcai-t_u " + str(t_u)) )




#for alpha in [-10000,-1,0,0.1,1,10000]:
#	configurations.append(("crude_greedy_alpha_" + str(alpha), "./rewrite-no-lp-crude-greedy --forbid-self-overlapping-actions --use-q-hat-with-alpha " + str(alpha)))

for d in domains:
	for (i,(dom,prob)) in enumerate(domains[d]):
		assert(os.path.isfile(dom))
		assert(os.path.isfile(prob))
                os.makedirs("res/" + d + "/" + str(i))
		for cname,c in configurations:  
			print("(ulimit -t 200; " + c + " " + dom + " " + prob + " >& res/" + d + "/" + str(i) + "/" + cname + ".log)")


