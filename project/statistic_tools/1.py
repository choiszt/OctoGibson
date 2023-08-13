import os
import json
from collections import OrderedDict
path="/shared/liushuai/OmniGibson/omnigibson/data/og_dataset/scenes"
result=OrderedDict()

names=os.listdir(path)
for name in names:
    files=os.listdir(os.path.join(path,name,"json"))
    for file in files:
        temppath=os.path.join(path,name,"json",file)
        with open(temppath,"r") as f:
            a=json.load(f)
            templist=list(a['objects_info']['init_info'].keys())
            for ele in templist:
                thing=ele.split("_")[0]
                if thing in result.keys():
                    result[thing]+=1
                else:
                    result[thing]=0

final_dict=sorted(result.items(), key=lambda t: t[1],reverse=True)