import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the mug
    mug_201 = registry(env,"mug_201")
    EasyGrasp(robot, mug_201)
    donothing(env)
