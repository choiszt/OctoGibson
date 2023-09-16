import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Take a tissue from the toilet paper
    toilet_paper_88 = registry(env,"toilet_paper_88")
    EasyGrasp(robot, toilet_paper_88)
    donothing(env)
