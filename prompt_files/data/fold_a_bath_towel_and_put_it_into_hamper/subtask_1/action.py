import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Take a bath towel out of the clothes dryer.
    bath_towel_192 = registry(env, "bath_towel_192")
    clothes_dryer_zlmnfg_0 = registry(env, "clothes_dryer_zlmnfg_0")
    EasyGrasp(robot, bath_towel_192)
    donothing(env)
