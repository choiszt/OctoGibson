import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the chopping board on the sink.
    chopping_board_85 = registry(env,"chopping_board_85")
    sink_czyfhq_0 = registry(env,"sink_czyfhq_0")
    put_ontop(robot, chopping_board_85, sink_czyfhq_0)
    donothing(env)
