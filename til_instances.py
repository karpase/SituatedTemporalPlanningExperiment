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

name = "turtlebot"
for y in range(1,9):
	domain = "pddl-instances/turtlebot/bailout1/domain_turtlebot_bailout.pddl"
	problem = "pddl-instances/turtlebot/bailout1/problem_turtlebot_4_bailout_" + str(y) + ".pddl"
	domains[name].append((domain,problem))

for y in range(1,7):
	domain = "pddl-instances/turtlebot/bailout2/domain_turtlebot_bailout.pddl"
	problem = "pddl-instances/turtlebot/bailout2//problem_turtlebot_5_bailout_" + str(y) + ".pddl"
	domains[name].append((domain,problem))


planner = "./rewrite-no-lp"
configurations = []
#configurations.append( ("ijcai","--deadline-aware-open-list IJCAI --forbid-self-overlapping-actions") )

for rep in range(10):
	for tilmult in [0.25, 0.5, 2, 4]:
		configurations.append( ("baseline__tilmult_" + str(tilmult) + "__r" + str(rep),"./rewrite-no-lp --multiply-TILs-by " + str(tilmult) + " --forbid-self-overlapping-actions --deadline-aware-open-list Focal --slack-from-heuristic") )

		for gamma in [1]:
			for min_pf in [0.0001]:
				for fweight in [-0.000001]:
					for t_u in [100]:
						for r in [100]:
							for nexp in [1000]:
								for real_time_multiplier in [1]:
									configurations.append( ("dda__tilmult_" + str(tilmult) + "__r" + str(rep), 
										"./rewrite-no-lp --allocate-t_u-expansions --include-metareasoning-time --multiply-TILs-by " + str(tilmult) + " --real-to-plan-time-multiplier " + str(real_time_multiplier) + " --calculate-Q-interval " + str(r) + " --add-weighted-f-value-to-Q "  + str(fweight) + " --min-probability-failure " + str(min_pf) + "  --slack-from-heuristic  --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --ijcai-gamma " + str(gamma) + " --ijcai-t_u " + str(t_u) + " --icaps-for-n-expansions " + str(nexp) ) )
									#configurations.append( ("dda__gamma0__r" + str(rep), 
									#	"./rewrite-no-lp --allocate-t_u-expansions --include-metareasoning-time --real-to-plan-time-multiplier " + str(real_time_multiplier) + " --calculate-Q-interval " + str(r) + " --add-weighted-f-value-to-Q "  + str(fweight) + " --min-probability-failure " + str(min_pf) + "  --slack-from-heuristic  --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --ijcai-gamma " + str(0) + " --ijcai-t_u " + str(t_u) + " --icaps-for-n-expansions " + str(nexp) ) )
									#configurations.append( ("dda__fweight0__r" + str(rep), 
									#	"./rewrite-no-lp --allocate-t_u-expansions --include-metareasoning-time --real-to-plan-time-multiplier " + str(real_time_multiplier) + " --calculate-Q-interval " + str(r) + " --add-weighted-f-value-to-Q "  + str(0) + " --min-probability-failure " + str(min_pf) + "  --slack-from-heuristic  --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --ijcai-gamma " + str(gamma) + " --ijcai-t_u " + str(t_u) + " --icaps-for-n-expansions " + str(nexp) ) )
									#configurations.append( ("dda__nexp1__r" + str(rep), 
									#	"./rewrite-no-lp --allocate-t_u-expansions --include-metareasoning-time --real-to-plan-time-multiplier " + str(real_time_multiplier) + " --calculate-Q-interval " + str(r) + " --add-weighted-f-value-to-Q "  + str(fweight) + " --min-probability-failure " + str(min_pf) + "  --slack-from-heuristic  --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --ijcai-gamma " + str(gamma) + " --ijcai-t_u " + str(t_u) + " --icaps-for-n-expansions " + str(1) ) )
									#configurations.append( ("dda__hs__r" + str(rep), 
									#	"./rewrite-no-lp --include-metareasoning-time --real-to-plan-time-multiplier " + str(real_time_multiplier) + " --calculate-Q-interval " + str(r) + " --add-weighted-f-value-to-Q "  + str(fweight) + " --min-probability-failure " + str(min_pf) + "  --slack-from-heuristic  --forbid-self-overlapping-actions --deadline-aware-open-list IJCAI --ijcai-gamma " + str(gamma) + " --ijcai-t_u " + str(t_u) + " --icaps-for-n-expansions " + str(nexp) ) )



#for alpha in [-10000,-1,0,0.1,1,10000]:
#	configurations.append(("crude_greedy_alpha_" + str(alpha), "./rewrite-no-lp-crude-greedy --forbid-self-overlapping-actions --use-q-hat-with-alpha " + str(alpha)))

for d in domains:
	for (i,(dom,prob)) in enumerate(domains[d]):
		assert(os.path.isfile(dom))
		assert(os.path.isfile(prob))
		os.makedirs("res/" + d + "/" + str(i))
		for cname,c in configurations:  
			print("(ulimit -t 200; " + c + " " + dom + " " + prob + " >& res/" + d + "/" + str(i) + "/" + cname + ".log)")


