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
		domain = "pddl-instances/rcll/csdomain.pddl"
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




default_cmd_params = "--include-metareasoning-time --multiply-TILs-by 1 --real-to-plan-time-multiplier 1 --min-probability-failure 0.001 --slack-from-heuristic --forbid-self-overlapping-actions --ijcai-gamma 1 --ijcai-t_u 100 --time-aware-heuristic 1"

def add_config(configurations, expansions_per_second, dispatch : bool, 
			   mcts : bool, dispatch_threshold=None, mcts_c=None, mcts_fo='Mean', mcts_so='Mean', mcts_random_walk_length=0, 
			   mcts_best_open_list=False, q_alternation=False, subtree_focus_threshold=None,
			   value_types=None, add_weighted_f_value_to_Q = "-0.00001",
			   allocate_tu_expansions = True, time_shift_second_value = False):
	cmd_params = default_cmd_params + " --time-based-on-expansions-per-second " + str(expansions_per_second) + " --calculate-Q-interval " + str(expansions_per_second) + " --icaps-for-n-expansions " + str(expansions_per_second) + " --add-weighted-f-value-to-Q " + str(add_weighted_f_value_to_Q) + " "
	name = "copeqrel__eps_" + str(expansions_per_second) + "__mcts_" + str(mcts) + "__addweightedfvaluetoQ_" + add_weighted_f_value_to_Q.replace(",","-") + "__allocate_tu_expansions_" + str(allocate_tu_expansions) +  "__time_shift_second_value_" + str(time_shift_second_value)

	if allocate_tu_expansions:
		cmd_params = cmd_params + " --allocate-t_u-expansions"

	if time_shift_second_value:
		cmd_params = cmd_params + " --time-shift-second-value NextInterestingTime"


	if value_types is not None:
		name = name + "__valuetypes_" + value_types.replace(",","-")
		cmd_params = cmd_params + " --value-types " + value_types

	if q_alternation:
		name = name + "__Qalternation_" + str(q_alternation)
		cmd_params = cmd_params + " --Q-alternation "



	if mcts:
		cmd_params = cmd_params + " --deadline-aware-open-list MCTS --mcts-C " + str(mcts_c) + " --mcts-sd-weight 0 --mcts-value-for-pruned disappear --random-walk-length-cap " + str(mcts_random_walk_length)
		if mcts_best_open_list:
			cmd_params = cmd_params + " --mcts-best-on-open-list"
			name = name + "__mcts_best_open_list"
		name = name + "__c_" + str(mcts_c) + "__fo_" + mcts_fo + "__rw_" + str(mcts_random_walk_length)
	else:
		cmd_params = cmd_params + " --deadline-aware-open-list IJCAI"		

	if not dispatch:
		name = name + "__disp_false"
		if mcts:
			cmd_params = cmd_params + " --mcts-configuration 'value=FinishProbability(0,now),aggregator=" + mcts_fo + "'"
	else:
		name = name + "__disp_true__dispThreshold_" + str(dispatch_threshold)
		if mcts:
			name = name + "__so_" + mcts_so
			cmd_params = cmd_params + " --mcts-configuration 'value=[FinishProbability(0,now),FinishProbability(0,later)],aggregator=[" + mcts_fo + "," + mcts_so + "]' --use-dispatcher LPFThreshold --dispatch-threshold " + str(dispatch_threshold)
		else:			
			if subtree_focus_threshold is not None:
				name = name + "__subtree_focus_threshold_" + str(subtree_focus_threshold)
				cmd_params = cmd_params + " --dispatch-frontier-size 10 --subtree-focus-threshold " + str(subtree_focus_threshold) + " --optimistic-lst-for-dispatch-reasoning --use-dispatcher LPFThreshold --dispatch-threshold " + str(dispatch_threshold)
			else:
				cmd_params = cmd_params + " --dispatch-frontier-size 10 --subtree-focus-threshold " + str(dispatch_threshold / 2) + " --optimistic-lst-for-dispatch-reasoning --use-dispatcher LPFThreshold --dispatch-threshold " + str(dispatch_threshold)
	
	cmd = planner + "  " + cmd_params
	configurations.append( (name, cmd) )

for expansions_per_second in [10, 20, 50, 100, 200, 300, 500, 1000]:
#for expansions_per_second in [50, 100, 500]:
	for allocate_tu_expansions in [False, True]:
	# Baseline
		#add_config(configurations, expansions_per_second, dispatch=False, mcts=False, allocate_tu_expansions=allocate_tu_expansions)
		for dispatch_threshold in [0.1, 0.25]: #[0.025, 0.1, 0.25]:
			# Baseline
			#add_config(configurations, expansions_per_second, dispatch=True, mcts=False, dispatch_threshold=dispatch_threshold, allocate_tu_expansions=allocate_tu_expansions)
			# New single
			#add_config(configurations, expansions_per_second, dispatch=True, mcts=False, value_types="FValue", add_weighted_f_value_to_Q="0", dispatch_threshold=dispatch_threshold, subtree_focus_threshold=1, allocate_tu_expansions=allocate_tu_expansions)
			#add_config(configurations, expansions_per_second, dispatch=True, mcts=False, value_types="NegativeLPF", add_weighted_f_value_to_Q="0", dispatch_threshold=dispatch_threshold, subtree_focus_threshold=1, allocate_tu_expansions=allocate_tu_expansions)
			#add_config(configurations, expansions_per_second, dispatch=True, mcts=False, value_types="Q", add_weighted_f_value_to_Q="-0.00001", dispatch_threshold=dispatch_threshold, subtree_focus_threshold=1, allocate_tu_expansions=allocate_tu_expansions)
			# New double
			add_config(configurations, expansions_per_second, dispatch=True, mcts=False, value_types="FValue,NegativeLPF", add_weighted_f_value_to_Q="0,0", dispatch_threshold=dispatch_threshold, subtree_focus_threshold=1, allocate_tu_expansions=allocate_tu_expansions, q_alternation=True, time_shift_second_value=True)
			# add_config(configurations, expansions_per_second, dispatch=True, mcts=False, value_types="Q,NegativeLPF", add_weighted_f_value_to_Q="-0.000001,0", dispatch_threshold=dispatch_threshold, subtree_focus_threshold=1, allocate_tu_expansions=allocate_tu_expansions, q_alternation=True)
			# add_config(configurations, expansions_per_second, dispatch=True, mcts=False, value_types="Q,Q", add_weighted_f_value_to_Q="-0.00001,-0.00001", dispatch_threshold=dispatch_threshold, subtree_focus_threshold=1, allocate_tu_expansions=allocate_tu_expansions, q_alternation=True)
			# add_config(configurations, expansions_per_second, dispatch=True, mcts=False, value_types="NegativeLPF,NegativeLPF", add_weighted_f_value_to_Q="0,0", dispatch_threshold=dispatch_threshold, subtree_focus_threshold=1, allocate_tu_expansions=allocate_tu_expansions, q_alternation=True)
			# add_config(configurations, expansions_per_second, dispatch=True, mcts=False, value_types="NegativeLPF,FValue", add_weighted_f_value_to_Q="0,0", dispatch_threshold=dispatch_threshold, subtree_focus_threshold=1, allocate_tu_expansions=allocate_tu_expansions, q_alternation=True)

	# # MCTS
	# for mcts_fo in ['Mean', 'Max', 'PowerMean(4)']:
	# 	for mcts_so in ['Mean', 'Max', 'PowerMean(4)']:
	# 		for mcts_c in [0, 0.1, 1]:
	# 			for mcts_random_walk_length in [0, 5]:
	# 				for mcts_best_open_list in [False, True]:
	# 					#add_config(configurations, expansions_per_second, dispatch=False, mcts=True, mcts_c=mcts_c, mcts_fo=mcts_fo, mcts_random_walk_length=mcts_random_walk_length, mcts_best_open_list=mcts_best_open_list)
	# 					for dispatch_threshold in [0.001, 0.01, 0.1]:
	# 						add_config(configurations, expansions_per_second, dispatch=True, dispatch_threshold=dispatch_threshold, mcts=True, mcts_c=mcts_c, mcts_fo=mcts_fo, mcts_so=mcts_so, mcts_random_walk_length=mcts_random_walk_length, mcts_best_open_list=mcts_best_open_list)
	# 	# 	add_config(configurations, expansions_per_second, dispatch=True, mcts=True, dispatch_threshold=dispatch_threshold, mcts_c=mcts_c, mcts_fo='Mean', mcts_so='Mean')		
	# 	# 	add_config(configurations, expansions_per_second, dispatch=True, mcts=True, dispatch_threshold=dispatch_threshold, mcts_c=mcts_c, mcts_fo='Mean', mcts_so='Max')		
	# 	# 	add_config(configurations, expansions_per_second, dispatch=True, mcts=True, dispatch_threshold=dispatch_threshold, mcts_c=mcts_c, mcts_fo='Max', mcts_so='Mean')		
	# 	# 	add_config(configurations, expansions_per_second, dispatch=True, mcts=True, dispatch_threshold=dispatch_threshold, mcts_c=mcts_c, mcts_fo='Max', mcts_so='Max')		
	


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
				print(c + " " + os.path.join(cwd,dom) + " " + os.path.join(cwd,prob) + " " + os.path.join(cwd,"res",d,str(i),cname + ".log") + " " + os.path.join(cwd, "parse_rewrite_output.sh"))


