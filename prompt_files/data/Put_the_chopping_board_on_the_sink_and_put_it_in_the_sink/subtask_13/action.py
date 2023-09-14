import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the sink.
    sink_czyfhq_0 = registry(env,"sink_czyfhq_0")
    MoveBot(env, robot, sink_czyfhq_0, camera)
    donothing(env)
