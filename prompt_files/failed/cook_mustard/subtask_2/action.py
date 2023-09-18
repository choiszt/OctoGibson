import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the mixing bowl from the countertop
    mixing_bowl_204 = registry(env,"mixing_bowl_204")
    EasyGrasp(robot, mixing_bowl_204)
    donothing(env)
