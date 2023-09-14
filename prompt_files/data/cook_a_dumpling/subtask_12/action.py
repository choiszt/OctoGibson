import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the tupperware down
    tupperware = registry(env,"tupperware_156")
    put_ontop(robot, tupperware, sink_czyfhq_0)
    donothing(env)
