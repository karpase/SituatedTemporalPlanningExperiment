import csv
from collections import defaultdict
import statistics
from scipy.stats.mstats import gmean
import random
import scipy.stats
import re

#filename = "raw.jair.combined.csv"
#filename = "raw.rcll-fixed-dl.csv"
#filename = "res.raw.csv"
#filename = "res.raw.cogrob-srv1.csv"
#filename = "res.raw.tah.csv"
filename = "res.zeus.csv"

problems = defaultdict(set)
configs = set()


# Pass 1: get problems
coverage = defaultdict(lambda: defaultdict(lambda: 0))
total_coverage = defaultdict(lambda: 0)

min_coverage = defaultdict(lambda: defaultdict(lambda: 0))
max_coverage = defaultdict(lambda: defaultdict(lambda: 0))
min_total_coverage = defaultdict(lambda: 0)
max_total_coverage = defaultdict(lambda: 0)

expansions = defaultdict(lambda: defaultdict(lambda: 0))

stdata = defaultdict(lambda: defaultdict(lambda: list()))



best_prob_coverage = defaultdict(set)


problems_unsolved_by_at_least_one = defaultdict(set)

data = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: list())))

config_args = defaultdict(lambda: {})


unsolved_f = open("unsolved.txt", "w")


with open(filename, newline='') as csvfile:
    spamreader  = csv.reader(csvfile)
    for row in spamreader:
        dpc = row[0].split("/")
        dom = dpc[1]
        prob = int(dpc[2])
        conf = dpc[3]


        ind = conf.find("__")      
        confname_pre = conf[:ind]
        conf_post = conf[ind+2:]        
        ind2 = conf_post.find("__")        
        confname_post = conf_post[ind2+2:]
        confr = conf_post[:ind2]
        confname = confname_pre + "__" + confname_post

        #print(conf, ",", confname, ",", confr)

        args = confname.split("__")
        for arg in args:
            nv = arg.split("_")
            if len(nv) > 1:
                config_args[confname]["_".join(nv[0:-1])] = nv[-1].split(".log")[0]

        problems[dom].add(prob)       
        configs.add(confname)

        
        solved = "Found" in row[1] or "Plan valid" in row[1]
        unsolvable = "Unsolvable" in row[2]
        timeout = not solved and not unsolvable

        if solved:
            makespan = float("0" + row[7])
            mr_time = float("0" + row[8])            
            total_time = float("0" + row[9])
            if total_time == 0 and "naive" in confname:
                total_time = float("0" + row[3])

            mr_ratio = 0
            if total_time > 0:
                mr_ratio = mr_time / total_time
            exp = int(row[5])


            exp_per_sec = exp / (total_time + 0.01)

            

            data[confname][dom][prob].append( [1, exp, total_time, mr_time,  mr_ratio, makespan, total_time + makespan, exp_per_sec] )
            if total_time > 200:
                print(row)

        if not solved:
            problems_unsolved_by_at_least_one[dom].add(prob)
            unsolved_f.write(str(row) + "\n")
            data[confname][dom][prob].append( [0, "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A" ] )

        #print(dom, prob, confname, data[confname][dom][prob])


unsolved_f.close()
print(sorted(configs))
for confname in sorted(configs):
    print(confname, config_args[confname])

agg_expansions = defaultdict(lambda: defaultdict(lambda: list()))
total_agg_expansions = defaultdict(lambda: list())

agg_time = defaultdict(lambda: defaultdict(lambda: list()))
total_agg_time = defaultdict(lambda: list())

agg_mr_ratio = defaultdict(lambda: defaultdict(lambda: list()))
total_agg_mr_ratio = defaultdict(lambda: list())

cnt_win = defaultdict(lambda: defaultdict(lambda: 0))
cnt_lose = defaultdict(lambda: defaultdict(lambda: 0))
cnt_tie = defaultdict(lambda: defaultdict(lambda: 0))

total_cnt_win = defaultdict(lambda: 0)
total_cnt_lose = defaultdict(lambda: 0)
total_cnt_tie = defaultdict(lambda: 0)

dda_default_config = 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log'


def add_vbs(vbs_config, configs):
    for dom in problems.keys():
        for prob in problems[dom]:
                bs_config = configs[0]
                pbest_cov = 0
                for conf in configs:
                    pcoverage = sum(map(lambda x: x[0], data[conf][dom][prob]))
                    #print(dom, prob, conf, coverage)
                    if pcoverage > pbest_cov:
                        pbest_cov =  pcoverage
                        bs_config = conf
                    
                data[vbs_config][dom][prob] = data[bs_config][dom][prob]


naive_configs = ['naive__pt_0.adj_0','naive__pt_0.1.adj_0.1', 'naive__pt_1.adj_1', 'naive__pt_10.adj_10', 'naive__pt_100.adj_100']
naive_vbs_config = 'naive__pt_VBS.adj_VBS'
add_vbs(naive_vbs_config, naive_configs)
config_args[naive_vbs_config]['pt']='VBS'


for dom in problems.keys():
    for prob in problems[dom]:
        best_gat = float('inf')
        for conf in data.keys():
            for trial in data[conf][dom][prob]:
                gat = trial[6]
                if gat != "N/A" and gat < best_gat:
                    best_gat = gat
        
        for conf in data.keys():
            for trial in data[conf][dom][prob]:
                gat = trial[6]
                if gat != "N/A":
                    trial.append(best_gat / gat)
                else:
                    trial.append(0)
         


for confname in data.keys():
    for dom in problems.keys():
        for prob in problems[dom]:            
            pcov = list(map(lambda x: x[0], data[confname][dom][prob]))
            if len(pcov) > 0:
                cov = statistics.mean(pcov)
            else:
                cov = 0
            coverage[dom][confname] = coverage[dom][confname] + cov
            total_coverage[confname] = total_coverage[confname] + cov


            mylist = list(map(lambda x: x[0], data[confname][dom][prob]))
            complist = list(map(lambda x: x[0], data[dda_default_config][dom][prob]))

            if mylist != complist:                
                res = scipy.stats.mannwhitneyu(mylist, complist)
                if res.pvalue < 0.05:
                    if cov > statistics.mean(complist):
                        cnt_win[dom][confname] = cnt_win[dom][confname] + 1
                        total_cnt_win[confname] = total_cnt_win[confname] + 1
                    else:
                        cnt_lose[dom][confname] = cnt_lose[dom][confname] + 1
                        total_cnt_lose[confname] = total_cnt_lose[confname] + 1
                else:
                    cnt_tie[dom][confname] = cnt_tie[dom][confname] + 1
                    total_cnt_tie[confname] = total_cnt_tie[confname] + 1
            else:
                cnt_tie[dom][confname] = cnt_tie[dom][confname] + 1
                total_cnt_tie[confname] = total_cnt_tie[confname] + 1
            

            if cov == 1:
                min_coverage[dom][confname] = min_coverage[dom][confname] + 1
                min_total_coverage[confname] = min_total_coverage[confname] + 1
            if cov > 0:
                max_coverage[dom][confname] = max_coverage[dom][confname] + 1
                max_total_coverage[confname] = max_total_coverage[confname]  + 1


##            if prob not in problems_unsolved_by_at_least_one[dom]:
##                mean_expansions_prob = statistics.mean(map(lambda x: x[1], data[confname][dom][prob]))
##                agg_expansions[dom][confname].append(mean_expansions_prob)
##                total_agg_expansions[confname].append(mean_expansions_prob)
##
##                mean_time_prob = statistics.mean(map(lambda x: x[2], data[confname][dom][prob]))
##                agg_time[dom][confname].append(mean_time_prob)
##                total_agg_time[confname].append(mean_time_prob)
##
##                mean_mr_ratio_prob = statistics.mean(map(lambda x: x[4], data[confname][dom][prob]))
##                agg_mr_ratio[dom][confname].append(mean_mr_ratio_prob)
##                total_agg_mr_ratio[confname].append(mean_mr_ratio_prob)


columnsep = " & "
lineend = "\\\\"

config_order = sorted(configs)
#print(config_order)
#['baseline', 'dda_',   'dda__nexp1_', 'dda__gamma0_', 'dda__hs_', 'dtuned']




order_baseline = [
    #'naive__pt_0.adj_0','naive__pt_0.1.adj_0.1', 'naive__pt_1.adj_1', 'naive__pt_10.adj_10', 'naive__pt_100.adj_100',
    naive_vbs_config, 
    #'icaps2018__tilmult_1.log',
    'icaps2018_tah__tilmult_1.log',
    dda_default_config
    ]

order_baseline_t = [
    naive_vbs_config, 'icaps2018_tah__tilmult_1.log'
    ]

order_dda = [
    naive_vbs_config,
    'icaps2018_tah__tilmult_1.log',
    dda_default_config
    #,'dda__time_4hrs__tuned_domain__eval_test.log'
    ]

order_tah = [
    'icaps2018__tilmult_1.log',
    'icaps2018_tah__tilmult_1.log',
    'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_0.log',
    'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log']

order_gamma = [
 'dda__allocatetuexpansions_True__gamma_-10__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_-1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_0__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_0.5__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_0.75__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_1.5__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log', 
 'dda__allocatetuexpansions_True__gamma_5__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_10__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log'
 ]

order_tu = [
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_1__r_1__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_10__r_10__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_1000__r_1000__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_10000__r_10000__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log'
]

order_nexp = [
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_1__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_10__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_1000__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_10000__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log'
 ]

order_allocatetuexpansions = [
 'dda__allocatetuexpansions_False__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log']

order_fweight = [
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_0__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1000000__rtmultiplier_1__tilmult_1__time_aware_heuristic_1.log' 
 ]



order_smac_train = [
'dda__tuned_all__eval_train__traintime_4hrs.log',
'dda__tuned_all__eval_train__traintime_7days.log',
'dda__tuned_domain__eval_train__traintime_4hrs.log',
'dda__tuned_domain__eval_train__traintime_7days.log'
]

order_smac_test = [
'dda__tuned_all__eval_test__traintime_4hrs.log',
'dda__tuned_all__eval_test__traintime_7days.log',
'dda__tuned_domain__eval_test__traintime_4hrs.log',
'dda__tuned_domain__eval_test__traintime_7days.log'
]

order_overall = [  
    naive_vbs_config, 
    'icaps2018_tah__tilmult_1.log',
    dda_default_config,
    'dda__tuned_domain__eval_test__traintime_4hrs.log'
    ]

 

domain_short_names = {
'airport-time-windows': 'airport',
'pipesworld-no-tankage-temporal-deadlines': 'pw-nt',
'rcll-1-robots': 'rcll-1',
'rcll-2-robots': 'rcll-2',
'rcll-3-robots': 'rcll-3',
'rcll-fixed-dl1-robots': 'rcll-fixed-dl-1',
'rcll-fixed-dl2-robots': 'rcll-fixed-dl-2',
'orig-rcll-1-robots': 'o-rcll-1',
'orig-rcll-2-robots': 'o-rcll-2',
'satellite-complex-time-windows': 'sat-cmplx',
'satellite-time-time-windows': 'sat-tw',
'trucks-time-constraints-timed-initial-literals': 'trucks',
'turtlebot': 'turtlebot',
'umts-flaw-temporal-time-windows': 'umts-flaw',
'umts-temporal-time-windows': 'umts'
}

print(problems.keys())

domain_groups = [
    ('IPC',['airport-time-windows',
     'pipesworld-no-tankage-temporal-deadlines',
     'satellite-complex-time-windows',
     'satellite-time-time-windows',
     'trucks-time-constraints-timed-initial-literals',
     'umts-flaw-temporal-time-windows',
     'umts-temporal-time-windows']),
    ('ROB',['rcll-1-robots',
     'rcll-2-robots',
     'rcll-3-robots',
     #'rcll-fixed-dl1-robots',
     #'rcll-fixed-dl2-robots',
     #'orig-rcll-1-robots',
     #'orig-rcll-2-robots',
     'turtlebot'])
    ]


def get_confname(conf, params):
    conftype = conf.split("__")[0]
    valid_params = [x for x in filter(lambda param: param in config_args[conf].keys(), params)]
    if len(valid_params) > 0:
        confname = conf.split("__")[0] + " (" + ",".join(map(lambda param: param + " = " + config_args[conf][param], valid_params)) + ")"
    else:
        confname = conftype
    return confname


mrplot = open("mrplot.txt","w")
for confname in order_tu:
    for dom in problems.keys():
        for prob in problems[dom]:
            for res in data[confname][dom][prob]:
                if res[4] != "N/A":
                    print(config_args[confname]["tu"], res[4], file=mrplot)
mrplot.close()                    

for params, config_order in [(['pt'], order_baseline),
                             (['pt'], order_baseline_t),
                             (['pt'], order_dda),                             
                             (['gamma'], order_gamma), (['tu'], order_tu), (['nexp'], order_nexp),(['allocatetuexpansions'], order_allocatetuexpansions),
                             (['time_aware_heuristic'], order_tah),
                             (['fweight'], order_fweight),
                             (['tuned','traintime','eval'], order_smac_train),(['tuned','traintime','eval'], order_smac_test),
                             (['pt', 'tuned'], order_overall)
                             ]:
    #print("*********************************")
    #print("Results for changing ", param)
    #print("*********************************")
    
    print("Coverage (", ",".join(params), ")")
    print("")
    print("\\resizebox{\\textwidth}{!}{\\begin{tabular}{|l" + "|rr" * len(config_order) + "|}")
    print("\\hline")
    print("Domain", end=columnsep)
    for i, conf in enumerate(config_order):
        confname = get_confname(conf, params)
        if i < len(config_order) - 1:
            endc = columnsep
        else:
            endc = ""
        print("\\multicolumn{2}{|c|}{" + confname + "}",  end=endc)    
    print(lineend)
    print("\\hline")
    for grp_name, dom_group in domain_groups:
        group_total = defaultdict(lambda: 0)
        group_total_min = defaultdict(lambda: 0)
        group_total_max = defaultdict(lambda: 0)
        for dom in dom_group:
            print(domain_short_names[dom], end=columnsep)
            best_cov = max(map(lambda conf: coverage[dom][conf], config_order))            
            for i, conf in enumerate(config_order):
                if i < len(config_order) - 1:
                    endc = columnsep
                else:
                    endc = ""
                if coverage[dom][conf] == best_cov:
                    print("{\\bf %.1f}" % coverage[dom][conf] + "& (" + str(min_coverage[dom][conf]) + "--" + str(max_coverage[dom][conf]) +  ")", end=endc)
                else:
                    print("%.1f" % coverage[dom][conf] + "& (" + str(min_coverage[dom][conf]) + "--" + str(max_coverage[dom][conf]) +  ")", end=endc)
                group_total[conf] = group_total[conf] + coverage[dom][conf]
                group_total_min[conf] = group_total_min[conf] + min_coverage[dom][conf]
                group_total_max[conf] = group_total_max[conf] + max_coverage[dom][conf]
            print(lineend)
        print("\\hline")
        print("subtotal (" + grp_name + ")", end=columnsep)
        best_st_cov = max(map(lambda conf: group_total[conf], config_order))            
        for i, conf in enumerate(config_order):
            if i < len(config_order) - 1:
                endc = columnsep
            else:
                endc = ""
            if group_total[conf] == best_st_cov:
                print("{\\bf %.1f}" % group_total[conf], "& (" + str(group_total_min[conf]) +  "--"  + str(group_total_max[conf]) +  ")",end=endc )
            else:
                print("%.1f" % group_total[conf], "& (" + str(group_total_min[conf]) +  "--"  + str(group_total_max[conf]) +  ")",end=endc )
        print(lineend)
        print("\\hline")
    print("TOTAL", end=columnsep)
    best_t_cov = max(map(lambda conf: total_coverage[conf], config_order))            
    for i, conf in enumerate(config_order):
        if i < len(config_order) - 1:
            endc = columnsep
        else:
            endc = ""
        if total_coverage[conf] == best_t_cov:
            print("{\\bf %.1f}" % total_coverage[conf], "& (" + str(min_total_coverage[conf]) +  "--"  + str(max_total_coverage[conf]) +  ")",end=endc )
        else:
            print("%.1f" % total_coverage[conf], "& (" + str(min_total_coverage[conf]) +  "--"  + str(max_total_coverage[conf]) +  ")",end=endc )
    print(lineend)
    print("\\hline")
    print("\\end{tabular}}")

    print("")
    print("")


    print("Win/Lose (", ",".join(params), ")")
    print("")
    print("\\resizebox{\\textwidth}{!}{\\begin{tabular}{|l" + "|r" * len(config_order) + "|}")
    print("\\hline")
    
    print("Domain", end=columnsep)
    for i, conf in enumerate(config_order):
        confname = get_confname(conf, params)
        if i < len(config_order) - 1:
            endc = columnsep
        else:
            endc = ""
        print(confname, end=endc)
    print(lineend)
    print("\\hline")
    for grp_name, dom_group in domain_groups:
        group_win = defaultdict(lambda: 0)
        group_lose = defaultdict(lambda: 0)
        
        for dom in dom_group:
            print(domain_short_names[dom], end=columnsep)
            for i, conf in enumerate(config_order):
                if i < len(config_order) - 1:
                    endc = columnsep
                else:
                    endc = ""
                print(cnt_win[dom][conf], "/", cnt_lose[dom][conf], end=endc)
                group_win[conf] = group_win[conf] + cnt_win[dom][conf]
                group_lose[conf] = group_lose[conf] + cnt_lose[dom][conf]
            print(lineend)
        
        print("\\hline")
        print("subtotal (" + grp_name + ")", end=columnsep)
        for i, conf in enumerate(config_order):
            if i < len(config_order) - 1:
                endc = columnsep
            else:
                endc = ""
            print(str(group_win[conf]), "/", str(group_lose[conf]), end=endc )
        print(lineend)
        print("\\hline")
        
    print("TOTAL", end=columnsep)
    for i, conf in enumerate(config_order):
        if i < len(config_order) - 1:
            endc = columnsep
        else:
            endc = ""
        print(str(total_cnt_win[conf]), "/", str(total_cnt_lose[conf]), end=endc )
    print(lineend)
    print("\\hline")
    print("\\end{tabular}}")

    print("")
    print("")

    def my_gmean(list):
        if len(list) > 0 and 0 not in list:
            return "%.2f" % gmean(list)
        else:
            return "N/A"

    def my_mean(list):
        if len(list) > 0:
            return "%.2f" % (statistics.mean(list) * 100.0)
        else:
            return "N/A"

    def my_sum(list):        
        return "%.2f" % sum(list)


    def print_table(item, agg_func, title, only_solved_by_all, highlight=None):
        table_problems_unsolved_by_at_least_one = defaultdict(set)
        if only_solved_by_all:
            for confname in config_order:
                for dom in problems.keys():
                    for prob in problems[dom]:
                        for res in data[confname][dom][prob]:
                            if res[0] == 0:
                                table_problems_unsolved_by_at_least_one[dom].add(prob)

        agg_data = defaultdict(lambda: defaultdict(lambda: list()))
        for confname in config_order:
            for dom in problems.keys():
                for prob in problems[dom]:
                    if prob not in table_problems_unsolved_by_at_least_one[dom]:
                        mean_datum_prob = statistics.mean(map(item, data[confname][dom][prob]))
                        agg_data[dom][confname].append(mean_datum_prob)

        
        print(title)
        
        print("")
        print("\\resizebox{\\textwidth}{!}{\\begin{tabular}{|l" + "|r" * len(config_order) + "|}")
        print("\\hline")
        
        print("Domain", end=columnsep)
        for i, conf in enumerate(config_order):
            confname = get_confname(conf, params)
            if i < len(config_order) - 1:
                endc = columnsep
            else:
                endc = ""
            print(confname, end=endc)
        print(lineend)
        print("\\hline")
        total_list = defaultdict(lambda: [])
        for grp_name, dom_group in domain_groups:
            group_list = defaultdict(lambda: [])            
            
            for dom in dom_group:
                best = None
                bestf = None
                if highlight is not None:                    
                    for conf in config_order:
                        num = agg_func(agg_data[dom][conf])
                        if num == "N/A":
                            continue                        
                        numf = float(num)
                        if best is None:
                            best = num
                            bestf = numf
                        else:                            
                            if highlight == "max" and numf > bestf:
                                best = num
                                bestf = numf
                            if highlight == "min" and numf < bestf:
                                best = num
                                bestf = numf

                        
                print(domain_short_names[dom] + " (" + str(len(agg_data[dom][config_order[0]])) + ")", end=columnsep)
                for i, conf in enumerate(config_order):
                    if i < len(config_order) - 1:
                        endc = columnsep
                    else:
                        endc = ""
                    num = agg_func(agg_data[dom][conf])
                    if num == best:
                        print("{\\bf ", num, "}", end=endc)
                    else:
                        print(num, end=endc)
                    group_list[conf] = group_list[conf] + agg_data[dom][conf]
                    total_list[conf] = total_list[conf] + agg_data[dom][conf]                
                print(lineend)
            
            print("\\hline")
            print("subtotal (" + grp_name + ")", end=columnsep)

            best = None
            bestf = None
            if highlight is not None:                    
                for conf in config_order:
                    num = agg_func(group_list[conf])
                    if num == "N/A":
                        continue                        
                    numf = float(num)
                    if best is None:
                        best = num
                        bestf = numf
                    else:                            
                        if highlight == "max" and numf > bestf:
                            best = num
                            bestf = numf
                        if highlight == "min" and numf < bestf:
                            best = num
                            bestf = numf
            
            for i, conf in enumerate(config_order):
                if i < len(config_order) - 1:
                    endc = columnsep
                else:
                    endc = ""
                num = agg_func(group_list[conf])
                if num == best:                    
                    print("{\\bf", num, "}", end=endc )
                else:
                    print(num, end=endc )
            print(lineend)
            print("\\hline")
            
        print("TOTAL", end=columnsep)

        best = None
        bestf = None
        if highlight is not None:                    
            for conf in config_order:
                num = agg_func(total_list[conf])
                if num == "N/A":
                    continue                        
                numf = float(num)
                if best is None:
                    best = num
                    bestf = numf
                else:                            
                    if highlight == "max" and numf > bestf:
                        best = num
                        bestf = numf
                    if highlight == "min" and numf < bestf:
                        best = num
                        bestf = numf
                            
        for i, conf in enumerate(config_order):
            if i < len(config_order) - 1:
                endc = columnsep
            else:
                endc = ""
            num = agg_func(total_list[conf])
            if num == best:                    
                print("{\\bf", num, "}", end=endc )
            else:
                print(num, end=endc )

        print(lineend)
        print("\\hline")
        print("\\end{tabular}}")

        print("")
        print("")


    print_table(lambda x: x[2], my_gmean, "Geometric Mean Total time in seconds (" + ",".join(params) + ")", only_solved_by_all=True, highlight="min")
    print_table(lambda x: x[1], my_gmean, "Geometric Mean Expansions (" + ",".join(params) + ")", only_solved_by_all=True, highlight="min")
    print_table(lambda x: x[4], my_mean, "Mean Metareasoning Ratio in Percent (" + ",".join(params) + ")", only_solved_by_all=True)
    print_table(lambda x: x[-1], my_sum, "IPC Score of Goal Achievement Time (" + ",".join(params) + ")", only_solved_by_all=False, highlight="max")
    print_table(lambda x: x[7], my_gmean, "GMean Expansions/Second (" + ",".join(params) + ")", only_solved_by_all=True, highlight=None)
