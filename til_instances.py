from collections import defaultdict
import os
import platform

hostname = platform.node()

domains = defaultdict(list)


#if hostname == "cogrob-lab-01.iem.technion.ac.il":
#	name = "airport-time-windows"
#	for x in range(1,51): 
#		domain = "pddl-instances/ipc-2004/domains/airport-temporal-time-windows-strips/domains/domain-" + str(x) + ".pddl" 
#		problem = "pddl-instances/ipc-2004/domains/airport-temporal-time-windows-strips/instances/instance-" + str(x) + ".pddl"
#		domains[name].append((domain,problem))

#if hostname == "cogrob-lab-03.iem.technion.ac.il":	
#	name = "pipesworld-no-tankage-temporal-deadlines"	
#	for x in range(1,31): 
#		domain = "pddl-instances/ipc-2004/domains/pipesworld-no-tankage-temporal-deadlines-strips/domain.pddl" 
#		problem = "pddl-instances/ipc-2004/domains/pipesworld-no-tankage-temporal-deadlines-strips/instances/instance-" + str(x) + ".pddl"
#		domains[name].append((domain,problem))

#if hostname == "cogrob-lab-04.iem.technion.ac.il":	
#	name = "satellite-complex-time-windows"
#	for x in range(1,37): 
#		domain = "pddl-instances/ipc-2004/domains/satellite-complex-time-windows-strips/domain.pddl"
#		problem = "pddl-instances/ipc-2004/domains/satellite-complex-time-windows-strips/instances/instance-" + str(x) + ".pddl"
#		domains[name].append((domain,problem))

#if hostname == "cogrob-lab-05.iem.technion.ac.il":		
#	name = "satellite-time-time-windows"	
#	for x in range(1,37): 
#		domain = "pddl-instances/ipc-2004/domains/satellite-time-time-windows-strips/domain.pddl"
#		problem = "pddl-instances/ipc-2004/domains/satellite-time-time-windows-strips/instances/instance-" + str(x) + ".pddl"
#		domains[name].append((domain,problem))

#if hostname == "cogrob-lab-06.iem.technion.ac.il":		
#	name = "umts-flaw-temporal-time-windows"	
#	for x in range(1,51): 
#		domain = "pddl-instances/ipc-2004/domains/umts-flaw-temporal-time-windows-strips/domain.pddl"
#		problem = "pddl-instances/ipc-2004/domains/umts-flaw-temporal-time-windows-strips/instances/instance-" + str(x) + ".pddl"
#		domains[name].append((domain,problem))

#if hostname == "cogrob-lab-07.iem.technion.ac.il":		
#	name = "umts-temporal-time-windows"		
#	for x in range(1,51): 
#		domain = "pddl-instances/ipc-2004/domains/umts-temporal-time-windows-strips/domain.pddl"
#		problem = "pddl-instances/ipc-2004/domains/umts-temporal-time-windows-strips/instances/instance-" + str(x) + ".pddl"
#		domains[name].append((domain,problem))

#if hostname == "cogrob-lab-08.iem.technion.ac.il":	
#	name = "trucks-time-constraints-timed-initial-literals"	
#	for x in range(1,21): 
#		domain = "pddl-instances/ipc-2006/domains/trucks-time-constraints-timed-initial-literals/domain.pddl"
#		problem = "pddl-instances/ipc-2006/domains/trucks-time-constraints-timed-initial-literals/instances/instance-" + str(x) + ".pddl"
#		domains[name].append((domain,problem))	
	
if hostname == "cogrob-lab-08.iem.technion.ac.il":	
	r = 1
	name = "rcll-" + str(r) + "-robots"
	for o in range(1,101):		
		domain = "pddl-instances/rcll/rcll_domain_production_durations_time_windows.pddl"
		problem = "pddl-instances/rcll/problem-" + "{0:0=3d}".format(o) + "-r" + str(r) + "-o1-durations.pddl"
		domains[name].append((domain,problem))

if hostname == "cogrob-lab-03.iem.technion.ac.il":	
	r = 2
	name = "rcll-" + str(r) + "-robots"
	for o in range(1,101):		
		domain = "pddl-instances/rcll/rcll_domain_production_durations_time_windows.pddl"
		problem = "pddl-instances/rcll/problem-" + "{0:0=3d}".format(o) + "-r" + str(r) + "-o1-durations.pddl"
		domains[name].append((domain,problem))	

if hostname == "cogrob-lab-01.iem.technion.ac.il":	
	r = 3
	name = "rcll-" + str(r) + "-robots"
	for o in range(1,101):		
		domain = "pddl-instances/rcll/rcll_domain_production_durations_time_windows.pddl"
		problem = "pddl-instances/rcll/problem-" + "{0:0=3d}".format(o) + "-r" + str(r) + "-o1-durations.pddl"
		domains[name].append((domain,problem))		




planner = "./rewrite-no-lp"
configurations = []
configurations.append( ("h","--slack-from-heuristic") )
configurations.append( ("h_ms","--slack-from-heuristic --deadline-aware-open-list MaxSlack") )
configurations.append( ("h_fs","--slack-from-heuristic --deadline-aware-open-list Focal") )

for alpha in [-10000,-1,0,0.1,1,10000]:
	configurations.append(("alpha_" + str(alpha), "--slack-from-heuristic --use-q-hat-with-alpha " + str(alpha)))
	configurations.append(("alpha_ms_" + str(alpha), "--deadline-aware-open-list MaxSlack --slack-from-heuristic --use-q-hat-with-alpha " + str(alpha)))
	configurations.append(("alpha_f_" + str(alpha), "--deadline-aware-open-list Focal --slack-from-heuristic --use-q-hat-with-alpha " + str(alpha)))

for d in domains:
	for (i,(dom,prob)) in enumerate(domains[d]):
		assert(os.path.isfile(dom))
		assert(os.path.isfile(prob))
                os.makedirs("res/" + d + "/" + str(i))
		for cname,c in configurations:  
			print("(ulimit -t 200; ./rewrite-no-lp " + c + " " + dom + " " + prob + " >& res/" + d + "/" + str(i) + "/" + cname + ".log)")


