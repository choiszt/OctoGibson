import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the wax paper
    wax_paper_173 = registry(env,"wax_paper_173")
    EasyGrasp(robot, wax_paper_173)
    donothing(env)
