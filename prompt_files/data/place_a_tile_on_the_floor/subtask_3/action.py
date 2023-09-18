import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Place the ceramic tile on the floor
    ceramic_tile_275 = registry(env,"ceramic_tile_275")
    put_ontop(robot, ceramic_tile_275, "floor")
    donothing(env)
