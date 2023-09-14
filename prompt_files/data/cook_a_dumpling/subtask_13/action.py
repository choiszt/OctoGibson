import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Register the sink
    sink = registry(env,"sink_czyfhq_0")
    # Subtask 7: Put the tupperware down on the sink
    tupperware = registry(env,"tupperware_156")
    put_ontop(robot, tupperware, sink)
    donothing(env)
