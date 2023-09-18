import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the plant pot
    plant_pot_278 = registry(env,"plant_pot_278")
    MoveBot(env, robot, plant_pot_278, camera)
    donothing(env)
