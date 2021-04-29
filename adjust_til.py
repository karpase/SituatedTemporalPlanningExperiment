#!/usr/bin/env python3

import sys
from pythonpddl import pddl

def adjust_pddl_til(problem, time_adjustment):
    for el in problem.initialstate:
        if isinstance(el, pddl.TimedFormula):
            el.timespecifier = max(0, el.timespecifier - time_adjustment)            


def adjust_til(domain_path, problem_path, adjustment, adjusted_problem_path):
    (_,problem) = pddl.parseDomainAndProblem(domain_path, problem_path)
    adjust_pddl_til(problem, adjustment)
    
    with open(adjusted_problem_path, 'w') as adjusted_problem:
        adjusted_problem.write(problem.asPDDL())
    

def main():
    if len(sys.argv) < 4:
        print("Usage: pddl.py <domain> <problem> <til_adjustment> <new_problem>")
        return

    domain_path = sys.argv[1]
    problem_path = sys.argv[2]
    adjustment = float(sys.argv[3])
    adjusted_problem_path = sys.argv[4]

    adjust_til(domain_path, problem_path, adjustment, adjusted_problem_path)
    
    #for a in dom.actions:
    #    for b in [False, True]:
    #        print(a.name, "c", b, list(map(lambda x: x.asPDDL(), a.get_pre(b))))
    #    for b in [False, True]:
    #        print(a.name, "e", b, list(map(lambda x: x.asPDDL(), a.get_eff(b))))

    #for da in dom.durative_actions:
    #    for t in ["start","all","end"]:
    #        for b in [False, True]:
    #            print(da.name, "c", t, b, list(map(lambda x: x.asPDDL(), da.get_cond(t, b))))
    #    for t in ["start","all","end"]:
    #        for b in [False, True]:
    #            print(da.name, "e", t, b, list(map(lambda x: x.asPDDL(), da.get_eff(t, b))))


if __name__ == "__main__":
    main()
