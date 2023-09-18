import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the colored pencil from the suitcase
    colored_pencil_277 = registry(env,"colored_pencil_277")
    EasyGrasp(robot, colored_pencil_277)
    donothing(env)
