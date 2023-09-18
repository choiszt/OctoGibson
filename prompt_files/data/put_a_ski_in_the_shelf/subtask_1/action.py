import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the ski
    ski_88 = registry(env,"ski_88")
    EasyGrasp(robot, ski_88)
    donothing(env)
