import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the teacup
    teacup_191 = registry(env,"teacup_191")
    EasyGrasp(robot, teacup_191)
    donothing(env)
