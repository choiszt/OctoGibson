import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the granola bar
    granola_bar_86 = registry(env,"granola_bar_86")
    EasyGrasp(robot, granola_bar_86)
    donothing(env)
