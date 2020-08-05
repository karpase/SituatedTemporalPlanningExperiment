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
#configurations.append( ("best_g", "./rewrite-no-lp --include-metareasoning-time --real-to-plan-time-multiplier " + str(1) + " --calculate-Q-interval " + str(100) + "  --min-probability-failure " + str(0.01) + "  --slack-from-heuristic  --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --ijcai-gamma " + str(10) + " --ijcai-t_u " + str(100)) )
#configurations.append( ("best_g__new_gamma", "./rewrite-no-lp --include-metareasoning-time --real-to-plan-time-multiplier " + str(1) + " --calculate-Q-interval " + str(100) + "  --min-probability-failure " + str(0.01) + "  --slack-from-heuristic  --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --new-gamma " + str(1.1111) + " --ijcai-t_u " + str(100) + " --icaps-for-n-expansions " + str(1) ) )
#configurations.append( ("best_g__nexp_100", "./rewrite-no-lp --include-metareasoning-time --real-to-plan-time-multiplier " + str(1) + " --calculate-Q-interval " + str(100) + "  --min-probability-failure " + str(0.01) + "  --slack-from-heuristic  --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --ijcai-gamma " + str(10) + " --ijcai-t_u " + str(100) + " --icaps-for-n-expansions " + str(100) ) )
configurations.append( ("best_g__nexp_1000", "./rewrite-no-lp --include-metareasoning-time --real-to-plan-time-multiplier " + str(1) + " --calculate-Q-interval " + str(100) + "  --min-probability-failure " + str(0.01) + "  --slack-from-heuristic  --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --ijcai-gamma " + str(10) + " --ijcai-t_u " + str(100) + " --icaps-for-n-expansions " + str(1000) ) )

#for gamma in [-1000000, -10, -1, -0.1, 0, 0.1,  1, 10]:
#for gamma in [-2, -0.5]:
#	for min_pf in [0.001, 0.01]:
#		for t_u in [100, 1000, "ETD"]:
#			for r in [100, 1000]:
#				for nexp in [1, 10, 100, 1000]:
#					for real_time_multiplier in [1]:
#						configurations.append( ("mt_improved_greedy__r_" + str(r) + "__gamma_" + str(gamma) + "__nexp_" + str(nexp) + "__tu_" + str(t_u) + "__min_pf_" + str(min_pf) + "__rtm_" + str(real_time_multiplier), 
#							"./rewrite-no-lp --include-metareasoning-time --real-to-plan-time-multiplier " + str(real_time_multiplier) + " --calculate-Q-interval " + str(r) + "  --min-probability-failure " + str(min_pf) + "  --slack-from-heuristic  --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --new-gamma " + str(gamma) + " --ijcai-t_u " + str(t_u) + " --icaps-for-n-expansions " + str(nexp) ) )
#						if gamma == 0:
#							configurations.append( ("mt_improved_greedy_sanity__r_" + str(r) + "__gamma_" + str(gamma) + "__nexp_" + str(nexp) + "__tu_" + str(t_u) + "__min_pf_" + str(min_pf) + "__rtm_" + str(real_time_multiplier), 
#								"./rewrite-no-lp --include-metareasoning-time --real-to-plan-time-multiplier " + str(real_time_multiplier) + " --calculate-Q-interval " + str(r) + "  --min-probability-failure " + str(min_pf) + "  --slack-from-heuristic  --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --ijcai-gamma " + str(gamma) + " --ijcai-t_u " + str(t_u) + " --icaps-for-n-expansions " + str(nexp) ) )



#for alpha in [-10000,-1,0,0.1,1,10000]:
#	configurations.append(("crude_greedy_alpha_" + str(alpha), "./rewrite-no-lp-crude-greedy --forbid-self-overlapping-actions --use-q-hat-with-alpha " + str(alpha)))

for d in domains:
	for (i,(dom,prob)) in enumerate(domains[d]):
		assert(os.path.isfile(dom))
		assert(os.path.isfile(prob))
		os.makedirs("res/" + d + "/" + str(i))
		for cname,c in configurations:  
			print("(ulimit -t 200; " + c + " " + dom + " " + prob + " >& res/" + d + "/" + str(i) + "/" + cname + ".log)")


