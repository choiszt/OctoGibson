import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Grasp the bowl
    mixing_bowl_173 = registry(env,"mixing_bowl_173")
    EasyGrasp(robot, mixing_bowl_173)
    donothing(env)
