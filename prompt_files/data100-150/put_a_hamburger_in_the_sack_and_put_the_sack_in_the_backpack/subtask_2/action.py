import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the hamburger.
    hamburger_188 = registry(env,"hamburger_188")
    EasyGrasp(robot, hamburger_188)
    donothing(env)
