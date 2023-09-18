import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the cooked potato from the oven.
    potato = registry(env, "potato_89")
    EasyGrasp(robot, potato)
    donothing(env)
