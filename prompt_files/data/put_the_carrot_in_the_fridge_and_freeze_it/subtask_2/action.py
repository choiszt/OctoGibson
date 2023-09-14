import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp a carrot
    carrot_177 = registry(env,"carrot_177")
    EasyGrasp(robot, carrot_177)
    donothing(env)
