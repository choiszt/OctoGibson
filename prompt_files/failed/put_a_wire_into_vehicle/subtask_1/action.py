import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot closer to the copper wire
    copper_wire_282 = registry(env,"copper_wire_282")
    MoveBot(env, robot, copper_wire_282, camera)
    donothing(env)
