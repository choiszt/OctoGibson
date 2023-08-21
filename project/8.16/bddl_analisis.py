from bddl.parsing import parse_problem
import os
path="/shared/liushuai/OmniGibson/bddl/bddl/activity_definitions"
for ele in sorted(list(os.listdir(path))):
    if(ele.endswith(".bddl")):
        continue
    goals=parse_problem(ele,0, "omnigibson")[-1]
    
    for goal in goals:
        cnt=0
        lenth=0
        for obj in goal:
            if("?"in obj):
                cnt+=1
            if cnt==2:
                lenth+=1
        print(ele)
        print(len(goal),lenth)