import logging
import warnings
from collections import defaultdict
import numpy as np
from ConfigSpace.hyperparameters import CategoricalHyperparameter, UniformFloatHyperparameter, UniformIntegerHyperparameter
from smac.configspace import ConfigurationSpace
from smac.facade.hyperband_facade import HB4AC
from smac.facade.smac_ac_facade import SMAC4AC
from smac.scenario.scenario import Scenario

import subprocess
from sklearn.model_selection import KFold 

logger = logging.getLogger("situated-temporal-planning-smac")
logging.basicConfig(level=logging.INFO)




def generate_instances():
	domains = defaultdict(list)

	name = "airport-time-windows"
	for x in range(1,51): 
		domain = "../pddl-instances/ipc-2004/domains/airport-temporal-time-windows-strips/domains/domain-" + str(x) + ".pddl" 
		problem = "../pddl-instances/ipc-2004/domains/airport-temporal-time-windows-strips/instances/instance-" + str(x) + ".pddl"
		domains[name].append((domain,problem))

	name = "pipesworld-no-tankage-temporal-deadlines"	
	for x in range(1,31): 
		domain = "../pddl-instances/ipc-2004/domains/pipesworld-no-tankage-temporal-deadlines-strips/domain.pddl" 
		problem = "../pddl-instances/ipc-2004/domains/pipesworld-no-tankage-temporal-deadlines-strips/instances/instance-" + str(x) + ".pddl"
		domains[name].append((domain,problem))

	name = "satellite-complex-time-windows"
	for x in range(1,37): 
		domain = "../pddl-instances/ipc-2004/domains/satellite-complex-time-windows-strips/domain.pddl"
		problem = "../pddl-instances/ipc-2004/domains/satellite-complex-time-windows-strips/instances/instance-" + str(x) + ".pddl"
		domains[name].append((domain,problem))

	name = "satellite-time-time-windows"	
	for x in range(1,37): 
		domain = "../pddl-instances/ipc-2004/domains/satellite-time-time-windows-strips/domain.pddl"
		problem = "../pddl-instances/ipc-2004/domains/satellite-time-time-windows-strips/instances/instance-" + str(x) + ".pddl"
		domains[name].append((domain,problem))

	name = "umts-flaw-temporal-time-windows"	
	for x in range(1,51): 
		domain = "../pddl-instances/ipc-2004/domains/umts-flaw-temporal-time-windows-strips/domain.pddl"
		problem = "../pddl-instances/ipc-2004/domains/umts-flaw-temporal-time-windows-strips/instances/instance-" + str(x) + ".pddl"
		domains[name].append((domain,problem))

	name = "umts-temporal-time-windows"		
	for x in range(1,51): 
		domain = "../pddl-instances/ipc-2004/domains/umts-temporal-time-windows-strips/domain.pddl"
		problem = "../pddl-instances/ipc-2004/domains/umts-temporal-time-windows-strips/instances/instance-" + str(x) + ".pddl"
		domains[name].append((domain,problem))

	name = "trucks-time-constraints-timed-initial-literals"	
	for x in range(1,21): 
		domain = "../pddl-instances/ipc-2006/domains/trucks-time-constraints-timed-initial-literals/domain.pddl"
		problem = "../pddl-instances/ipc-2006/domains/trucks-time-constraints-timed-initial-literals/instances/instance-" + str(x) + ".pddl"
		domains[name].append((domain,problem))	

	for r in range(1,3):
		name = "rcll-" + str(r) + "-robots"
		for o in range(1,101):		
			domain = "../pddl-instances/rcll/rcll_domain_production_durations_time_windows.pddl"
			problem = "../pddl-instances/rcll/problem-" + "{0:0=3d}".format(o) + "-r" + str(r) + "-o1-durations.pddl"
			domains[name].append((domain,problem))
	return domains

domains = generate_instances()

domfile_by_probfile = {}
for d in domains:
	for domfile,probfile in domains[d]:
		domfile_by_probfile[probfile] = domfile


train_folds = []
def generate_folds():
	for d in domains:
		kf = KFold(n_splits=10, shuffle=True)

		for i, (train_index, test_index) in enumerate(kf.split(domains[d])):
			train_filename = "folds/" + d + "_fold_" + str(i) + "_train.txt"		
			f = open(train_filename,"w")
			for t in train_index:
				f.write(domains[d][np.asscalar(t)][1] + "\n")
			f.close()
			train_folds.append(train_filename)

			test_filename = "folds/" + d + "_fold_" + str(i) + "_test.txt"
			f = open(test_filename,"w")
			for t in test_index:
				f.write(domains[d][np.asscalar(t)][1] + "\n")
			f.close()

generate_folds()







# Target Algorithm
# The signature of the function determines what arguments are passed to it
# i.e., budget is passed to the target algorithm if it is present in the signature
def run_situated_temporal_planner(cfg, seed, instance, **kwargs):
    """
        Creates a MLP classifier from sklearn and fits the given data on it.
        This is the function-call we try to optimize. Chosen values are stored in
        the configuration (cfg).
        Parameters
        ----------
        cfg: Configuration
            configuration chosen by smac
        seed: int or RandomState
            used to initialize the rf's random generator
        instance: str
            used to represent the instance to use (just a placeholder for this example)
        Returns
        -------
        float
    """
   
    #print("inst", instance)

    l = ["../rewrite-no-lp", 
                    "--include-metareasoning-time",
                    "--forbid-self-overlapping-actions",
                    "--deadline-aware-open-list", "IJCAI",
                    "--calculate-Q-interval", str(cfg["r"]),
                    "--slack-from-heuristic",
                    "--ijcai-t_u", str(cfg["t_u"]),         
                    "--ijcai-gamma", str(cfg["gamma"]),        
                    "--min-probability-failure", str(cfg["min_pf"]),
                    domfile_by_probfile[instance], instance]
    print(l)
    sr = subprocess.check_output(l)
    str_output = sr.decode("utf-8")   
    if str_output.find("Solution Found") > -1:
        lines = str_output.split("\n")
        #print("solved1", lines)
        last_line = lines[-2]
        words = last_line.split(" ")
        start_time = words[0]
        dur = words[-3]
        #print("solved2", start_time, dur)
        gat = float(start_time[:-2]) + float(dur[1:-2])
        print("solved, gat=",gat)
        return gat

    print("no solution found")
    return 10000


# Build Configuration Space which defines all parameters and their ranges.
# To illustrate different parameter types,
# we use continuous, integer and categorical parameters.
cs = ConfigurationSpace()


# Parameters for improved greedy metareasoning scheme
t_u = UniformFloatHyperparameter("t_u", 10, 1000, default_value=100, log=True)
gamma = UniformFloatHyperparameter("gamma", 0.01, 100, default_value=1, log=True)
r = UniformFloatHyperparameter("r", 10, 1000, default_value=100, log=True)
min_pf = UniformFloatHyperparameter("min_pf", 0.0001, 0.1, default_value=0.01, log=True)


cs.add_hyperparameters([t_u, gamma, r, min_pf])


for instance_file in train_folds:
	print("Finding best configuration for: ", instance_file)
	# SMAC scenario object
	scenario = Scenario({"run_obj": "quality",  # we optimize quality (alternative to runtime)
                     "wallclock-limit": 300,  # max duration to run the optimization (in seconds)
                     "cs": cs,  # configuration space
                     "deterministic": "true",
                     "limit_resources": True,  # Uses pynisher to limit memory and runtime
                     # Alternatively, you can also disable this.
                     # Then you should handle runtime and memory yourself in the TA
                     "cutoff": 30,  # runtime limit for target algorithm
                     "memory_limit": 3072,  # adat this to reasonable value for your hardware
                     #"instances": instances
                     "instance_file": instance_file
                     #"test_insts": "test-instances-rcll-r1.txt"
                     })

	# To optimize, we pass the function to the SMAC-object
	smac = SMAC4AC(scenario=scenario, rng=np.random.RandomState(421),
             tae_runner=run_situated_temporal_planner)#,
             #intensifier_kwargs=intensifier_kwargs)  # all arguments related to intensifier can be passed like this

	# Example call of the function with default values
	# It returns: Status, Cost, Runtime, Additional Infos
	#def_value = smac.get_tae_runner().run(config=cs.get_default_configuration(),
	#                                       seed=0)[1]
	#print("Value for default configuration: %.4f" % def_value)

	# Start optimization
	try:
	    incumbent = smac.optimize()
	finally:
	    incumbent = smac.solver.incumbent

	#inc_value = smac.get_tae_runner().run(config=incumbent, seed=0)[1]
	#print("Optimized Value: %.4f" % inc_value)



