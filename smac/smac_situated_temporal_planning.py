import logging
import warnings

import numpy as np
from ConfigSpace.hyperparameters import CategoricalHyperparameter, UniformFloatHyperparameter, UniformIntegerHyperparameter
from smac.configspace import ConfigurationSpace
from smac.facade.hyperband_facade import HB4AC
from smac.facade.smac_ac_facade import SMAC4AC
from smac.scenario.scenario import Scenario

import subprocess
from subprocess import PIPE

logger = logging.getLogger("situated-temporal-planning-smac")
logging.basicConfig(level=logging.INFO)

# Build Configuration Space which defines all parameters and their ranges.
# To illustrate different parameter types,
# we use continuous, integer and categorical parameters.
cs = ConfigurationSpace()


# Parameters for improved greedy metareasoning scheme
t_u = UniformFloatHyperparameter("t_u", 10, 1000, default_value=100, log=True)
gamma = UniformFloatHyperparameter("gamma", 0.01, 1000, default_value=10, log=True)
r = UniformFloatHyperparameter("r", 10, 1000, default_value=100, log=True)
min_pf = UniformFloatHyperparameter("min_pf", 0.0001, 0.1, default_value=0.01, log=True)


cs.add_hyperparameters([t_u, gamma, r, min_pf])





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
        budget: float
            used to set max iterations for the MLP
        Returns
        -------
        float
    """
   
    l = ["../rewrite-no-lp", 
                    "--deadline-aware-open-list", "IJCAI",
                    "--calculate-Q-interval", str(cfg["r"]),
                    "--slack-from-heuristic",
                    "--ijcai-t_u", str(cfg["t_u"]),         
                    "--ijcai-gamma", str(cfg["gamma"]),        
                    "--min-probability-failure", str(cfg["min_pf"]),
                    "../pddl-instances/rcll/rcll_domain_production_durations_time_windows.pddl", instance]
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
        #print("solved, gat=",gat)
        return gat

    #print("no solution found")
    return 2000






# SMAC scenario object
scenario = Scenario({"run_obj": "quality",  # we optimize quality (alternative to runtime)
                     "wallclock-limit": 7200,  # max duration to run the optimization (in seconds)
                     "cs": cs,  # configuration space
                     "deterministic": "true",
                     "limit_resources": True,  # Uses pynisher to limit memory and runtime
                     # Alternatively, you can also disable this.
                     # Then you should handle runtime and memory yourself in the TA
                     "cutoff": 30,  # runtime limit for target algorithm
                     "memory_limit": 3072,  # adat this to reasonable value for your hardware
                     "instance_file": "instances-rcll-r1.txt",
                     "test_insts": "test-instances-rcll-r1.txt"
                     })

# max budget for hyperband can be anything. Here, we set it to maximum no. of epochs to train the MLP for
max_iters = 50
# intensifier parameters
#intensifier_kwargs = {'initial_budget': 5, 'max_budget': max_iters, 'eta': 3}
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



