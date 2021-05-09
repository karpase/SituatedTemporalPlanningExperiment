import csv
from collections import defaultdict
import statistics
from scipy.stats.mstats import gmean
import random
import scipy.stats
import re

filename = "raw.jair.csv"

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
                config_args[confname][nv[0]] = nv[1]        
        

        problems[dom].add(prob)       
        configs.add(confname)

        
        solved = "Found" in row[1] or "Plan valid" in row[1]
        unsolvable = "Unsolvable" in row[2]
        timeout = not solved and not unsolvable

        if solved:            
            mr_time = float("0" + row[8])
            total_time = float("0" + row[9])
            if total_time == 0 and "naive" in confname:
                total_time = float("0" + row[3])
                if total_time == 0:
                    print(row)
            
            mr_ratio = mr_time / total_time
            exp = int(row[5])            

            data[confname][dom][prob].append( (1, exp, total_time, mr_time,  mr_ratio) )

        if not solved:
            problems_unsolved_by_at_least_one[dom].add(prob)
            unsolved_f.write(str(row) + "\n")
            data[confname][dom][prob].append( (0, "N/A", "N/A", "N/A", "N/A" ) )

        #print(dom, prob, confname, data[confname][dom][prob])

unsolved_f.close()
print(sorted(configs))

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

dda_default_config = 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log'

for confname in data.keys():
    for dom in problems.keys():
        for prob in problems[dom]:
            pcov = map(lambda x: x[0], data[confname][dom][prob])
            cov = statistics.mean(pcov)
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


            if prob not in problems_unsolved_by_at_least_one[dom]:
                mean_expansions_prob = statistics.mean(map(lambda x: x[1], data[confname][dom][prob]))
                agg_expansions[dom][confname].append(mean_expansions_prob)
                total_agg_expansions[confname].append(mean_expansions_prob)

                mean_time_prob = statistics.mean(map(lambda x: x[2], data[confname][dom][prob]))
                agg_time[dom][confname].append(mean_time_prob)
                total_agg_time[confname].append(mean_time_prob)

                mean_mr_ratio_prob = statistics.mean(map(lambda x: x[4], data[confname][dom][prob]))
                agg_mr_ratio[dom][confname].append(mean_mr_ratio_prob)
                total_agg_mr_ratio[confname].append(mean_mr_ratio_prob)


columnsep = " & "
lineend = "\\\\"

config_order = sorted(configs)
#print(config_order)
#['baseline', 'dda_',   'dda__nexp1_', 'dda__gamma0_', 'dda__hs_', 'dtuned']

order_baseline = [
    'naive__pt_0.1.adj_0.1', 'naive__pt_1.adj_1', 'naive__pt_10.adj_10', 'naive__pt_100.adj_100',
    'icaps2018__tilmult_1.log',
    'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log'
    ]


order_gamma = [
 'dda__allocatetuexpansions_True__gamma_-10__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_-1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_0__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_0.5__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_0.75__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_1.5__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log', 
 'dda__allocatetuexpansions_True__gamma_5__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_10__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log'
 ]

order_tu = [
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_1__r_1__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_10__r_10__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_1000__r_1000__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_10000__r_10000__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log'
]

order_nexp = [
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_1__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_10__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_1000__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_10000__fweight_-1e-06__rtmultiplier_1__tilmult_1.log'
 ]

order_allocatetuexpansions = [
 'dda__allocatetuexpansions_False__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log']

order_fweight = [
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1e-06__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1__rtmultiplier_1__tilmult_1.log',
 'dda__allocatetuexpansions_True__gamma_1__minpf_0.001__tu_100__r_100__nexp_100__fweight_-1000000__rtmultiplier_1__tilmult_1.log' 
 ]

domain_short_names = {
'airport-time-windows': 'airport',
'pipesworld-no-tankage-temporal-deadlines': 'pw-nt',
'rcll-1-robots': 'rcll-1',
'rcll-2-robots': 'rcll-2',
'satellite-complex-time-windows': 'sat-cmplx',
'satellite-time-time-windows': 'sat-tw',
'trucks-time-constraints-timed-initial-literals': 'trucks',
'turtlebot': 'turtlebot',
'umts-flaw-temporal-time-windows': 'umts-flaw',
'umts-temporal-time-windows': 'umts'
}


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
     'turtlebot'])
    ]


def get_confname(conf, param):
    if conf[:3] == "dda":
        if param == "tilmult":
            confname = "DDA"
        else:
            confname = "DDA (" + param + " = " + config_args[conf][param] + ")"
    elif conf[:9] == "icaps2018":
        confname = "ICAPS 2018"
    elif conf[:5] == "naive":
        confname = "naive (" + conf.split("_")[-1] + ")"
    else:
        confname = conf
    return confname

for param, config_order in [('tilmult', order_baseline), ('gamma', order_gamma), ('tu', order_tu), ('nexp', order_nexp), ('allocatetuexpansions', order_allocatetuexpansions), ('fweight', order_fweight)]:
    #print("*********************************")
    #print("Results for changing ", param)
    #print("*********************************")
    
    print("Coverage (", param, ")")
    print("")
    print("\\resizebox{\\textwidth}{!}{\\begin{tabular}{|l" + "|rr" * len(config_order) + "|}")
    print("\\hline")
    print("Domain", end=columnsep)
    for i, conf in enumerate(config_order):
        confname = get_confname(conf, param)
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
            for i, conf in enumerate(config_order):
                if i < len(config_order) - 1:
                    endc = columnsep
                else:
                    endc = ""
                print("%.1f" % coverage[dom][conf] + "& (" + str(min_coverage[dom][conf]) + "--" + str(max_coverage[dom][conf]) +  ")", end=endc)
                group_total[conf] = group_total[conf] + coverage[dom][conf]
                group_total_min[conf] = group_total_min[conf] + min_coverage[dom][conf]
                group_total_max[conf] = group_total_max[conf] + max_coverage[dom][conf]
            print(lineend)
        print("\\hline")
        print("subtotal (" + grp_name + ")", end=columnsep)
        for i, conf in enumerate(config_order):
            if i < len(config_order) - 1:
                endc = columnsep
            else:
                endc = ""
            print("%.1f" % group_total[conf], "& (" + str(group_total_min[conf]) +  "--"  + str(group_total_max[conf]) +  ")",end=endc )
        print(lineend)
        print("\\hline")
    print("TOTAL", end=columnsep)
    for i, conf in enumerate(config_order):
        if i < len(config_order) - 1:
            endc = columnsep
        else:
            endc = ""
        print("%.1f" % total_coverage[conf], "& (" + str(min_total_coverage[conf]) +  "--"  + str(max_total_coverage[conf]) +  ")",end=endc )
    print(lineend)
    print("\\hline")
    print("\\end{tabular}}")

    print("")
    print("")


    print("Win/Lose (", param, ")")
    print("")
    print("\\resizebox{\\textwidth}{!}{\\begin{tabular}{|l" + "|r" * len(config_order) + "|}")
    print("\\hline")
    
    print("Domain", end=columnsep)
    for i, conf in enumerate(config_order):
        confname = get_confname(conf, param)
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


    def print_table(item, agg_func, title):
        table_problems_unsolved_by_at_least_one = defaultdict(set)
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
                        mean_datum_prob = statistics.mean(map(lambda x: x[item], data[confname][dom][prob]))
                        agg_data[dom][confname].append(mean_datum_prob)

        
        print(title)
        
        print("")
        print("\\resizebox{\\textwidth}{!}{\\begin{tabular}{|l" + "|r" * len(config_order) + "|}")
        print("\\hline")
        
        print("Domain", end=columnsep)
        for i, conf in enumerate(config_order):
            confname = get_confname(conf, param)
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
                print(domain_short_names[dom] + " (" + str(len(agg_data[dom][dda_default_config])) + ")", end=columnsep)
                for i, conf in enumerate(config_order):
                    if i < len(config_order) - 1:
                        endc = columnsep
                    else:
                        endc = ""
                    print(agg_func(agg_data[dom][conf]), end=endc)
                    group_list[conf] = group_list[conf] + agg_data[dom][conf]
                    total_list[conf] = total_list[conf] + agg_data[dom][conf]                
                print(lineend)
            
            print("\\hline")
            print("subtotal (" + grp_name + ")", end=columnsep)
            for i, conf in enumerate(config_order):
                if i < len(config_order) - 1:
                    endc = columnsep
                else:
                    endc = ""            
                print(agg_func(group_list[conf]), end=endc )
            print(lineend)
            print("\\hline")
            
        print("TOTAL", end=columnsep)
        for i, conf in enumerate(config_order):
            if i < len(config_order) - 1:
                endc = columnsep
            else:
                endc = ""
            print(my_gmean(total_list[conf]), end=endc )
        print(lineend)
        print("\\hline")
        print("\\end{tabular}}")

        print("")
        print("")


    print_table(1, my_gmean, "Geometric Mean Total time in seconds (" + param + ")")
    print_table(2, my_gmean, "Geometric Mean Expansions (" + param + ")")
    print_table(4, my_mean, "Mean Metareasoning Ratio in Percent (" + param + ")")
