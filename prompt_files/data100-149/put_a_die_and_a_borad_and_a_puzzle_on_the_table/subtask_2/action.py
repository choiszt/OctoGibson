import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the die from the cabinet
    dice = registry(env, "dice_102")
    EasyGrasp(robot, dice)
    donothing(env)
