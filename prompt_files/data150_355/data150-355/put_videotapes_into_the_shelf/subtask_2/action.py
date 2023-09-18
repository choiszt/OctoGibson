import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the videotape from the checkout counter
    dvd = registry(env, "dvd_143")
    EasyGrasp(robot, dvd)
    donothing(env)
