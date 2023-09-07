import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    griddle = registry(env,"griddle_157")
    put_ontop(robot, "bacon_150", griddle)
    donothing(env)
