import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the saucer
    saucer_192 = registry(env,"saucer_192")
    EasyGrasp(robot, saucer_192)
    donothing(env)
