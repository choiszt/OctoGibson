import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the pot plant
    pot_plant_152 = registry(env,"pot_plant_152")
    EasyGrasp(robot, pot_plant_152)
    donothing(env)
