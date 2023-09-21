import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the book in the shelf (shelf_njwsoa_0)
    hardback_91 = registry(env,"hardback_91")
    shelf_njwsoa_0 = registry(env,"shelf_njwsoa_0")
    put_ontop(robot, hardback_91, shelf_njwsoa_0)
    donothing(env)
