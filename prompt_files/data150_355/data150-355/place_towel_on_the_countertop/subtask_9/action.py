import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 9: Grasp the towel.
    paper_towel_193 = registry(env,"paper_towel_193")
    EasyGrasp(robot, paper_towel_193)
    donothing(env)
