import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the cactus in the pot
    pottable_cactus_275 = registry(env,"pottable_cactus_275")
    plant_pot_278 = registry(env,"plant_pot_278")
    put_inside(robot, pottable_cactus_275, plant_pot_278)
    donothing(env)
