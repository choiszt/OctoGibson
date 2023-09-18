import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the egg
    egg_92 = registry(env,"egg_92")
    EasyGrasp(robot, egg_92)
    donothing(env)
