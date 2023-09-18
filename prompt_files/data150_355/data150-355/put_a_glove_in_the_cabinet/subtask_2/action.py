import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the glove
    kid_glove_122 = registry(env,"kid_glove_122")
    EasyGrasp(robot, kid_glove_122)
    donothing(env)
