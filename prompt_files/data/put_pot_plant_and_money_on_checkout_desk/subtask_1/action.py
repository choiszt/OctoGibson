import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the pot plant
    pot_plant_152 = registry(env,"pot_plant_152")
    checkout_counter_sckdal_0 = registry(env,"checkout_counter_sckdal_0")
    MoveBot(env, robot, pot_plant_152, camera)
    donothing(env)
