import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Grasp the pencil
    colored_pencil_277 = registry(env,"colored_pencil_277")
    EasyGrasp(robot, colored_pencil_277)
    donothing(env)
