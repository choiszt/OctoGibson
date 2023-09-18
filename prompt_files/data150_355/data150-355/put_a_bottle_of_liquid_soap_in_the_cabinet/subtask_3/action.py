import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the bottle of liquid soap
    bottle_of_liquid_soap_121 = registry(env,"bottle_of_liquid_soap_121")
    MoveBot(env, robot, bottle_of_liquid_soap_121, camera)
    donothing(env)
