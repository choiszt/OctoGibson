import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the plate in the sink
    plate_88 = registry(env,"plate_88")
    sink_czyfhq_0 = registry(env,"sink_czyfhq_0")
    put_inside(robot, plate_88, sink_czyfhq_0)
    donothing(env)
