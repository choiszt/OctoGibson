import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the mug from the bottom cabinet
    mug_188 = registry(env,"mug_188")
    EasyGrasp(robot, mug_188)
    donothing(env)
