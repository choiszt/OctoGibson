import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    griddle = registry(env,"griddle_157")
    bacon = registry(env,"bacon_150")
    put_ontop(robot, bacon, griddle)
    donothing(env)
