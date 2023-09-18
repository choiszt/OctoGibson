import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the pottable daffodil in the plant pot
    plant_pot_278 = registry(env,"plant_pot_278")
    pottable_daffodil_276 = registry(env,"pottable_daffodil_276")
    put_inside(robot, pottable_daffodil_276, plant_pot_278)
    donothing(env)
