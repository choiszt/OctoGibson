import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Pick up the straw
    straw = registry(env, "straw_92")
    EasyGrasp(robot, straw)
    donothing(env)
