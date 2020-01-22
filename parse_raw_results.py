import csv
from collections import defaultdict
import statistics
from scipy.stats.mstats import gmean


filename = "raw_mt_new.csv"
baseline_configs=['icaps2018.log']

problems = defaultdict(set)
configs = set()


# Pass 1: get coverage
coverage = defaultdict(lambda: defaultdict(lambda: 0))
total_coverage = defaultdict(lambda: 0)
best_prob_coverage = defaultdict(set)

with open(filename, newline='') as csvfile:
    spamreader  = csv.reader(csvfile)
    for row in spamreader:
        dpc = row[0].split("/")
        dom = dpc[1]
        prob = dpc[2]
        conf = dpc[3]

        problems[dom].add(prob)
        configs.add(conf)
        solved = "Found" in row[1]
        unsolvable = "Unsolvable" in row[2]
        timeout = not solved and not unsolvable


        if solved:
            coverage[dom][conf] = coverage[dom][conf] + 1
            total_coverage[conf] = total_coverage[conf] + 1
            if conf not in baseline_configs:
                best_prob_coverage[dom].add(prob)

# Compute best coverage
best = max(total_coverage.values())
best_configs = []
for conf in configs:
    if total_coverage[conf] == best:
        best_configs.append(conf)

# Pass 2: Find problems solved by all best_configs and baselines
problems_unsolved_by_at_least_one = defaultdict(set)
relevant_configs = baseline_configs + best_configs

with open(filename, newline='') as csvfile:
    spamreader  = csv.reader(csvfile)
    for row in spamreader:
        dpc = row[0].split("/")
        dom = dpc[1]
        prob = dpc[2]
        conf = dpc[3]

        if conf not in relevant_configs:
            continue

        solved = "Found" in row[1]
        unsolvable = "Unsolvable" in row[2]
        timeout = not solved and not unsolvable
        
        if not solved:
            problems_unsolved_by_at_least_one[dom].add(prob)

# Pass 3: Collect Data for commonly solved problems

mr_ratio_avg = defaultdict(lambda: defaultdict(list))
expanded = defaultdict(lambda: defaultdict(list))

with open(filename, newline='') as csvfile:
    spamreader  = csv.reader(csvfile)
    for row in spamreader:
        dpc = row[0].split("/")
        dom = dpc[1]
        prob = dpc[2]
        conf = dpc[3]

        #print(dom, prob, conf)

        #print(prob, problems_unsolved_by_at_least_one[dom], prob in problems_unsolved_by_at_least_one[dom])

        if conf not in relevant_configs:
            continue

        if  prob not in problems_unsolved_by_at_least_one[dom]:
            mr_time = float("0" + row[8])
            total_time = float(row[9])
            mr_ratio = mr_time / total_time
            mr_ratio_avg[dom][conf].append(mr_ratio)

            exp = int(row[5])
            expanded[dom][conf].append(exp)

        #print(dom, prob, conf, mr_time / total_time)



first_config = relevant_configs[0]


print("Coverage")
print("Domain", end=", ")
for conf in relevant_configs:
    print(conf, end=", ")
print("best_d, best_p")
total_best_d = 0
total_best_p = 0
for dom in coverage.keys():
    print(dom, end=", ")
    for conf in relevant_configs:
        print(coverage[dom][conf], end=", ")
    
    best_d = 0
    for conf in configs:
        if conf not in baseline_configs:
            best_d = max(best_d, coverage[dom][conf])
    print(best_d, end=", ")
    total_best_d = total_best_d + best_d

    best_p = len(best_prob_coverage[dom])
    print(best_p, end=", ")
    total_best_p = total_best_p + best_p
    print("")



    
print("TOTAL", end=", ")
for conf in relevant_configs:
    print(total_coverage[conf], end="," )
print(total_best_d, end=", ")
print(total_best_p, end=", ")
print("")



print("")
print("Metareasoning Ratio (average)")
print("Domain", end=", ")
for conf in relevant_configs:
    print(conf, end=", ")
print("")
for dom in mr_ratio_avg.keys():
    print(dom,"(",str(len(mr_ratio_avg[dom][first_config])),")" , end=", ")
    for conf in relevant_configs:
        print(statistics.mean(mr_ratio_avg[dom][conf]), end=", ")
    print("")

l = []
for dom in mr_ratio_avg.keys():
    l = l + mr_ratio_avg[dom][first_config]
    
print("TOTAL (" + str(len(l)) + ")", end=", ")
for conf in relevant_configs:
    l = []
    for dom in mr_ratio_avg.keys():
        l = l + mr_ratio_avg[dom][conf]
    print(statistics.mean(l), end="," )
print("")



print("")
print("Expansions (geometric mean)")
print("Domain", end=", ")
for conf in relevant_configs:
    print(conf, end=", ")
print("")
for dom in expanded.keys():
    print(dom,"(",str(len(expanded[dom][first_config])),")" , end=", ")
    for conf in relevant_configs:
        print(gmean(expanded[dom][conf]), end=", ")
    print("")

l = []
for dom in expanded.keys():
    l = l + expanded[dom][first_config]
    
print("TOTAL (" + str(len(l)) + ")", end=", ")
for conf in relevant_configs:
    l = []
    for dom in expanded.keys():
        l = l + expanded[dom][conf]
    print(gmean(l), end="," )
print("")