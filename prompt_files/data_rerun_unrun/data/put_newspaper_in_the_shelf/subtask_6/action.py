import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the newspaper in the shelf
    newspaper = registry(env, "newspaper_89")
    shelf = registry(env, "shelf_njwsoa_0")
    put_inside(robot, newspaper, shelf)
    donothing(env)
