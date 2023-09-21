import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Take out the platter
    platter = registry(env,"platter_92")
    EasyGrasp(robot, platter)
    donothing(env)
