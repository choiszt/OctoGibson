import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the book (hardback_188)
    hardback_188 = registry(env,"hardback_188")
    EasyGrasp(robot, hardback_188)
    donothing(env)
