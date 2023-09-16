import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the bottle of perfume
    bottle_of_perfume_85 = registry(env,"bottle_of_perfume_85")
    EasyGrasp(robot, bottle_of_perfume_85)
    donothing(env)
