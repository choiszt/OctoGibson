import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the cheese
    swiss_cheese_100 = registry(env,"swiss_cheese_100")
    EasyGrasp(robot, swiss_cheese_100)
    donothing(env)
