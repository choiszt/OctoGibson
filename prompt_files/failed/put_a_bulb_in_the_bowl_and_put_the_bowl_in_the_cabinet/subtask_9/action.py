import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp the mixing bowl
    mixing_bowl_173 = registry(env,"mixing_bowl_173")
    EasyGrasp(robot, mixing_bowl_173)
    donothing(env)
