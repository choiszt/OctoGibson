import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Take out the butter
    fridge = registry(env,"fridge_dszchb_0")
    butter = registry(env,"butter_208")
    MoveBot(env, robot, fridge, camera)
    donothing(env)
    EasyGrasp(robot, butter)
    donothing(env)
