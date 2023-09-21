import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take out a bath towel from the clothes dryer.
    bath_towel = registry(env,"bath_towel_192")
    clothes_dryer = registry(env,"clothes_dryer_zlmnfg_0")
    open(robot, clothes_dryer)
    donothing(env)
    EasyGrasp(robot, bath_towel)
    donothing(env)
