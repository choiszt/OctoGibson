import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the bulb in the bowl
    daffodil_bulb_170 = registry(env,"daffodil_bulb_170")
    mixing_bowl_173 = registry(env,"mixing_bowl_173")
    put_inside(robot, daffodil_bulb_170, mixing_bowl_173)
    donothing(env)
