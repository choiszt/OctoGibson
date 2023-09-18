import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the tupperware
    tupperware_91 = registry(env,"tupperware_91")
    MoveBot(env, robot, tupperware_91, camera)
    donothing(env)
    # Subtask 4: Put the kabob inside the tupperware
    kabob_85 = registry(env,"kabob_85")
    put_inside(robot, kabob_85, tupperware_91)
    donothing(env)
