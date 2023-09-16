import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 9: Grasp the plum.
    plum = registry(env,"plum_1234")
    EasyGrasp(robot, plum)
    donothing(env)
