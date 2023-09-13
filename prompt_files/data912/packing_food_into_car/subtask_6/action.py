import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Pick up the cheese tart from the breakfast table
    cheese_tart = registry(env, "cheese_tart_280")
    EasyGrasp(robot, cheese_tart)
    donothing(env)
