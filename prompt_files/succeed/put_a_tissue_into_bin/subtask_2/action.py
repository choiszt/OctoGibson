import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the tissue
    toilet_paper_278 = registry(env,"toilet_paper_278")
    EasyGrasp(robot, toilet_paper_278)
    donothing(env)
