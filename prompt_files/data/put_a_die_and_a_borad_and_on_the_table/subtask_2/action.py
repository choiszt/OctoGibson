import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take the die out of the bottom cabinet.
    dice_102 = registry(env,"dice_102")
    EasyGrasp(robot, dice_102)
    donothing(env)
