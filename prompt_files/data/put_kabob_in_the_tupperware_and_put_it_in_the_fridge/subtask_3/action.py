import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the kabob
    kabob_85 = registry(env,"kabob_85")
    EasyGrasp(robot, kabob_85)
    donothing(env)
