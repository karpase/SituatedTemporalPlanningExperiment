import logging
import warnings
from collections import defaultdict
import numpy as np
from ConfigSpace.hyperparameters import CategoricalHyperparameter, UniformFloatHyperparameter, UniformIntegerHyperparameter
from smac.configspace import ConfigurationSpace
from smac.facade.hyperband_facade import HB4AC
from smac.facade.smac_hpo_facade import SMAC4HPO
from smac.facade.smac_bohb_facade import BOHB4HPO
from smac.facade.smac_ac_facade import SMAC4AC
from smac.scenario.scenario import Scenario
import sys

import subprocess
from sklearn.model_selection import KFold 
from multiprocessing import Pool


logger = logging.getLogger("situated-temporal-planning-smac")
logging.basicConfig(level=logging.INFO)


GAT_UNSOLVED = 2000
#GAT_UNSOLVED = 1000000000

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


	#domains = defaultdict(list)

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
test_folds = []
def read_folds():
	for d in domains:
		#kf = KFold(n_splits=10, shuffle=True)

		for i in range(2):
#		for i, (train_index, test_index) in enumerate(kf.split(domains[d])):
			train_filename = "folds/" + d + "_fold_" + str(i) + "_train.txt"		
			#f = open(train_filename,"w")
			#for t in train_index:
			#	f.write(domains[d][np.asscalar(t)][1] + "\n")
			#f.close()
			train_folds.append(train_filename)

			test_filename = "folds/" + d + "_fold_" + str(i) + "_test.txt"
			#f = open(test_filename,"w")
			#for t in test_index:
			#	f.write(domains[d][np.asscalar(t)][1] + "\n")
			#f.close()
			test_folds.append(test_filename)


def generate_zipper_folds():
        for d in domains:
                split = [domains[d][0::2], domains[d][1::2]]

                for i in range(2):
                        train_filename = "folds/" + d + "_fold_" + str(i) + "_train.txt"
                        f = open(train_filename,"w")
                        for t in split[i]:
                                f.write(t[1] + "\n")
                        f.close()
                        train_folds.append(train_filename)

                        test_filename = "folds/" + d + "_fold_" + str(i) + "_test.txt"
                        f = open(test_filename,"w")
                        for t in split[1-i]:
                                f.write(t[1] + "\n")
                        f.close()
                        test_folds.append(test_filename)

#generate_zipper_folds()
read_folds()






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


    if cfg == "baseline":
        l = ["../rewrite-no-lp", "--forbid-self-overlapping-actions", "--deadline-aware-open-list", "Focal", "--slack-from-heuristic", domfile_by_probfile[instance], instance]
    else:   
        l = ["../rewrite-no-lp", 
                    "--include-metareasoning-time",
                    "--forbid-self-overlapping-actions",
                    "--deadline-aware-open-list", "IJCAI",
                    "--calculate-Q-interval", str(cfg["r"]),
                    "--slack-from-heuristic",
                    "--ijcai-t_u", str(cfg["t_u"]),         
                    "--ijcai-gamma", str(cfg["gamma"]),        
                    "--icaps-for-n-expansions", str(cfg["nexp"]),
                    "--min-probability-failure", str(0.01),
#                    "--min-probability-failure", str(cfg["min_pf"]),
                    domfile_by_probfile[instance], instance]
    #print(l)
    sr = subprocess.check_output(l)
    str_output = sr.decode("utf-8")   
    if str_output.find("Solution Found") > -1:
        lines = str_output.split("\n")

        for line in lines:
             if line[:6] == "; Time":
                  words = line.split(" ")
                  time = float(words[2])
#                  print(line, time)
                  return time

        ##print("solved1", lines)
        #last_line = lines[-2]
        #words = last_line.split(" ")
        #start_time = words[0]
        #dur = words[-3]
        ##print("solved2", start_time, dur)
        #gat = float(start_time[:-2]) + float(dur[1:-2])
        ##print("solved, gat=",gat)
        #return gat

    #print("no solution found")
    return GAT_UNSOLVED


# Build Configuration Space which defines all parameters and their ranges.
# To illustrate different parameter types,
# we use continuous, integer and categorical parameters.
cs = ConfigurationSpace()


# Parameters for improved greedy metareasoning scheme
t_u = UniformIntegerHyperparameter("t_u", 1, 1000, default_value=100, log=True)
gamma = UniformFloatHyperparameter("gamma", 0.01, 1000, default_value=10, log=True)
r = UniformIntegerHyperparameter("r", 1, 1000, default_value=100, log=True)
#min_pf = UniformFloatHyperparameter("min_pf", 0.001, 0.1, default_value=0.01, log=True)
nexp = UniformIntegerHyperparameter("nexp", 1, 100000, default_value=1000, log=True)


#cs.add_hyperparameters([t_u, gamma, r, min_pf, nexp])
cs.add_hyperparameters([t_u, gamma, r,  nexp])






def run_fold(inp):
	instance_file = inp[0]
	test_file = inp[1]

	print("Finding best configuration for: ", instance_file," test file", test_file)
	# SMAC scenario object
	scenario = Scenario({"run_obj": "quality",  # we optimize quality (alternative to runtime)
                     "wallclock-limit": 3600*24,  # max duration to run the optimization (in seconds)
                     "cs": cs,  # configuration space
                     "deterministic": "true",
                     "limit_resources": True,  # Uses pynisher to limit memory and runtime
                     # Alternatively, you can also disable this.
                     # Then you should handle runtime and memory yourself in the TA
                     "cutoff": 200,  # runtime limit for target algorithm
                     "memory_limit": 3072,  # adat this to reasonable value for your hardware
                     #"instances": instances
                     "instance_file": instance_file,
                     #"test_insts": test_file
                     })

	# To optimize, we pass the function to the SMAC-object
	smac = BOHB4HPO(scenario=scenario, rng=np.random.RandomState(421),
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

	solved_baseline = 0
	solved_default = 0
	solved_incumbent = 0
	f = open(test_file, "r")
	for line in f.read().splitlines():
		#print(line)
		gatb = smac.get_tae_runner().run(config="baseline", seed=0, instance=line, cutoff=200)[1]
		if gatb < GAT_UNSOLVED:
			solved_baseline = solved_baseline + 1
		gatc = smac.get_tae_runner().run(config=cs.get_default_configuration(), seed=0, instance=line, cutoff=200)[1]
		if gatc < GAT_UNSOLVED:
			solved_default = solved_default + 1
		gatc = smac.get_tae_runner().run(config=incumbent, seed=0, instance=line, cutoff=200)[1]
		if gatc < GAT_UNSOLVED:
			solved_incumbent = solved_incumbent + 1
	f.close()

	print("***", instance_file + ", " + str(solved_baseline) + ", "+  str(solved_default) + ", " + str(solved_incumbent) + "\n")


	results_f = open("results.summary.txt", "a")
	results_f.write(instance_file + ", " + str(solved_baseline) + ", "+  str(solved_default) + ", " + str(solved_incumbent) + "\n")
	results_f.flush()
	#sys.exit(0)
	results_f.close()


#with Pool(32,daemon=False) as p:
#	p.map(run_fold, zip(train_folds, test_folds))

#for instance_file, test_file in zip(train_folds, test_folds):
#	print("python3 smac_situated_temporal_planning.py", instance_file, test_file)

	#run_fold((instance_file, test_file))

if __name__ == "__main__":
	run_fold( (sys.argv[1], sys.argv[2]) )
