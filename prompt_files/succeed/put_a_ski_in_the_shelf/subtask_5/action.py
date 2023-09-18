import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the ski on the shelf
    ski_88 = registry(env,"ski_88")
    shelf_njwsoa_1 = registry(env,"shelf_njwsoa_1")
    put_ontop(robot, ski_88, shelf_njwsoa_1)
    donothing(env)
