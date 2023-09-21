import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the date
    date = registry(env, "date_170")
    EasyGrasp(robot, date)
    donothing(env)
