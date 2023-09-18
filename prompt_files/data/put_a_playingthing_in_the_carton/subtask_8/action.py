import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the teddy bear inside the carton
    teddy_bear_88 = registry(env,"teddy_bear_88")
    carton_96 = registry(env,"carton_96")
    put_inside(robot, teddy_bear_88, carton_96)
    donothing(env)
