import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Grasp the meatball from the plate
    meatball_188 = registry(env,"meatball_188")
    EasyGrasp(robot, meatball_188)
    donothing(env)
