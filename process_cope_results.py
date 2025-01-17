import csv
from collections import defaultdict
import sys

data = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0)))
filename = "results.cope.csv"

eps_vals = set()
confs = set()

config_name = {
"mcts_False_addweightedfvaluetoQ_-0.00001_disp_false.log": "old_nodisp",
"mcts_False_addweightedfvaluetoQ_-0.00001_disp_true_dispThreshold_0.025.log": "old_disp_0.025",
"mcts_False_addweightedfvaluetoQ_-0.00001_disp_true_dispThreshold_0.1.log": "old_disp_0.1",
"mcts_False_addweightedfvaluetoQ_-0.00001_disp_true_dispThreshold_0.25.log": "old_disp_0.25",
"mcts_False_addweightedfvaluetoQ_-0.000001-0_valuetypes_Q-NegativeLPF_disp_true_dispThreshold_0.025_subtree_focus_threshold_1.log": "Q_LPF_0.025",
"mcts_False_addweightedfvaluetoQ_-0.000001-0_valuetypes_Q-NegativeLPF_disp_true_dispThreshold_0.1_subtree_focus_threshold_1.log": "Q_LPF_0.1",
"mcts_False_addweightedfvaluetoQ_-0.000001-0_valuetypes_Q-NegativeLPF_disp_true_dispThreshold_0.25_subtree_focus_threshold_1.log": "Q_LPF_0.25",
"mcts_False_addweightedfvaluetoQ_-0.00001--0.00001_valuetypes_Q-Q_disp_true_dispThreshold_0.025_subtree_focus_threshold_1.log": "Q_Q_0.025",
"mcts_False_addweightedfvaluetoQ_-0.00001--0.00001_valuetypes_Q-Q_disp_true_dispThreshold_0.1_subtree_focus_threshold_1.log": "Q_Q_0.1",
"mcts_False_addweightedfvaluetoQ_-0.00001--0.00001_valuetypes_Q-Q_disp_true_dispThreshold_0.25_subtree_focus_threshold_1.log": "Q_Q_0.25",
"mcts_False_addweightedfvaluetoQ_-0.00001_valuetypes_Q_disp_true_dispThreshold_0.025_subtree_focus_threshold_1.log": "Q_0.025",
"mcts_False_addweightedfvaluetoQ_-0.00001_valuetypes_Q_disp_true_dispThreshold_0.1_subtree_focus_threshold_1.log": "Q_0.1",
"mcts_False_addweightedfvaluetoQ_-0.00001_valuetypes_Q_disp_true_dispThreshold_0.25_subtree_focus_threshold_1.log": "Q_0.25",
"mcts_False_addweightedfvaluetoQ_0-0_valuetypes_FValue-NegativeLPF_disp_true_dispThreshold_0.025_subtree_focus_threshold_1.log": "F_LPF_0.025",
"mcts_False_addweightedfvaluetoQ_0-0_valuetypes_FValue-NegativeLPF_disp_true_dispThreshold_0.1_subtree_focus_threshold_1.log": "F_LPF_0.1",
"mcts_False_addweightedfvaluetoQ_0-0_valuetypes_FValue-NegativeLPF_disp_true_dispThreshold_0.25_subtree_focus_threshold_1.log": "F_LPF_0.25",
"mcts_False_addweightedfvaluetoQ_0_valuetypes_FValue_disp_true_dispThreshold_0.025_subtree_focus_threshold_1.log": "F_0.025",
"mcts_False_addweightedfvaluetoQ_0_valuetypes_FValue_disp_true_dispThreshold_0.1_subtree_focus_threshold_1.log": "F_0.1",
"mcts_False_addweightedfvaluetoQ_0_valuetypes_FValue_disp_true_dispThreshold_0.25_subtree_focus_threshold_1.log": "F_0.25",
"mcts_False_addweightedfvaluetoQ_0_valuetypes_NegativeLPF_disp_true_dispThreshold_0.025_subtree_focus_threshold_1.log": "LPF_0.025",
"mcts_False_addweightedfvaluetoQ_0_valuetypes_NegativeLPF_disp_true_dispThreshold_0.1_subtree_focus_threshold_1.log": "LPF_0.1",
"mcts_False_addweightedfvaluetoQ_0_valuetypes_NegativeLPF_disp_true_dispThreshold_0.25_subtree_focus_threshold_1.log": "LPF_0.25"
}

with open(filename, newline='') as csvfile:
    spamreader  = csv.reader(csvfile)
    for row in spamreader:
        #print(row)
        dpc = row[0].split("/")
        dom = dpc[-3]
        prob = int(dpc[-2])
        conf = dpc[-1]
        conf_args = conf.split("__")
        conf_args_dict = {}
        for arg in conf_args[1:]:
            kv = arg.split("_")
            conf_args_dict[kv[0]] = kv[1]
        eps = float(conf_args_dict['eps'])
        eps_vals.add(eps)
        conf_only = "_".join(conf_args[2:])
        confs.add(conf_only)
        solved = "Found" in row[1] or "Plan valid" in row[1]
        # if solved:
        #     makespan = float("0" + row[7])
        #     mr_time = float("0" + row[8])            
        #     total_time = float("0" + row[9])       
        #print(dom, eps, conf, prob, solved)
        if solved:
            data[dom][eps][conf_only] = data[dom][eps][conf_only] + 1

print("conf", "\t", end="")
for eps in sorted(list(eps_vals)):
    print(eps, "\t", end="")
print("")    
for dom in data.keys():
    print(dom)
    for conf in sorted(list(confs)):
        print(config_name.get(conf, conf), end="\t")
        for eps in sorted(list(eps_vals)):
            print(data[dom][eps][conf], end="\t")
        print("")
        
# print(data)