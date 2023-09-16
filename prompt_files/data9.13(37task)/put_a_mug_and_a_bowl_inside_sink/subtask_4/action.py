import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the mug inside the sink
    mug_201 = registry(env,"mug_201")
    sink_czyfhq_0 = registry(env,"sink_czyfhq_0")
    put_inside(robot, mug_201, sink_czyfhq_0)
    donothing(env)
