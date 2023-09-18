import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the chard
    chard_276 = registry(env,"chard_276")
    EasyGrasp(robot, chard_276)
    donothing(env)
